from unittest.mock import patch
from smtplib import SMTPException

import requests

from django.contrib.messages import get_messages
from django.core import mail
from django.test import Client, TestCase, override_settings
from django.urls import reverse

from .models import HistoriaPropuesta


@override_settings(
	EMAIL_HOST_USER='smtp-login@example.test',
	EMAIL_HOST_PASSWORD='test-password',
	DEFAULT_FROM_EMAIL='info@mundonica.org',
	MUNDONICA_NOTIFICATION_EMAIL='info@mundonica.org',
)
class ContactFormularioTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.url = reverse('home_app:formulario_contactar')
		self.data = {
			'name': 'Persona de prueba',
			'email': 'persona@example.com',
			'message': 'Este es un mensaje de prueba para Mundónica.',
		}

	@patch('applications.home.views.send_mail', return_value=1)
	def test_success_sends_to_configured_recipient_and_confirms(self, send_mail_mock):
		response = self.client.post(self.url, self.data)

		self.assertEqual(response.status_code, 302)
		self.assertEqual(
			send_mail_mock.call_args.kwargs['recipient_list'],
			['info@mundonica.org'],
		)
		shown_messages = [str(message) for message in get_messages(response.wsgi_request)]
		self.assertIn(
			'Hemos recibido tu mensaje y te responderemos pronto.',
			shown_messages,
		)
		self.assertNotIn('contact_form_draft', self.client.session)

	@patch('applications.home.views.send_mail', side_effect=SMTPException('SMTP unavailable'))
	def test_smtp_failure_keeps_data_and_shows_honest_message(self, send_mail_mock):
		response = self.client.post(self.url, self.data)

		self.assertEqual(response.status_code, 302)
		shown_messages = [str(message) for message in get_messages(response.wsgi_request)]
		self.assertIn(
			'No hemos podido enviar tu mensaje en este momento. '
			'Tus datos siguen en el formulario para que puedas revisarlos '
			'o intentarlo de nuevo.',
			shown_messages,
		)
		self.assertEqual(self.client.session['contact_form_draft'], self.data)
		send_mail_mock.assert_called_once()

		with patch(
			'applications.home.views.requests.get',
			side_effect=requests.RequestException('offline'),
		):
			home_response = self.client.get(reverse('home_app:home'))

		self.assertEqual(home_response.status_code, 200)
		self.assertEqual(home_response.context['form'].initial, self.data)


@override_settings(
	EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
	EMAIL_HOST_USER='smtp-login@example.test',
	EMAIL_HOST_PASSWORD='test-password',
	DEFAULT_FROM_EMAIL='info@mundonica.org',
	MUNDONICA_NOTIFICATION_EMAIL='info@mundonica.org',
)
class HistoriasViewTests(TestCase):
	def setUp(self):
		self.client = Client(enforce_csrf_checks=True)
		self.url = reverse('home_app:historias')
		self.data = {
			'nombre': 'María de prueba',
			'ciudad_pais': 'Madrid, España',
			'email': 'maria@example.com',
			'telefono': '',
			'historia': 'Una historia suficientemente larga para explicar la propuesta.',
			'preferencia_contacto': 'email',
			'preferencia_grabacion': 'sabado_manana',
			'lugar_grabacion': 'estudio_mundonica',
			'website': '',
		}

	def csrf_token(self, public_origin=False):
		headers = {'HTTP_HOST': 'localhost'}
		if public_origin:
			headers.update({
				'HTTP_HOST': 'mundonica.org',
				'HTTP_X_FORWARDED_PROTO': 'https',
			})
		response = self.client.get(self.url, **headers)
		self.assertContains(response, 'csrfmiddlewaretoken')
		return response.cookies['csrftoken'].value

	def test_valid_post_with_csrf_saves_and_notifies_info(self):
		token = self.csrf_token(public_origin=True)

		response = self.client.post(
			self.url,
			{**self.data, 'csrfmiddlewaretoken': token},
			HTTP_HOST='mundonica.org',
			HTTP_ORIGIN='https://mundonica.org',
			HTTP_X_FORWARDED_PROTO='https',
			follow=True,
		)

		self.assertContains(response, 'Enviado correctamente')
		self.assertEqual(HistoriaPropuesta.objects.count(), 1)
		propuesta = HistoriaPropuesta.objects.get()
		self.assertEqual(propuesta.preferencia_grabacion, 'sabado_manana')
		self.assertEqual(propuesta.lugar_grabacion, 'estudio_mundonica')
		self.assertEqual(len(mail.outbox), 1)
		self.assertEqual(mail.outbox[0].to, ['info@mundonica.org'])
		self.assertIn('Preferencia de grabación: Sábado por la mañana', mail.outbox[0].body)
		self.assertIn(
			'Lugar de grabación: En el estudio de Mundónica, en Oiartzun (Gipuzkoa, España)',
			mail.outbox[0].body,
		)

	def test_recording_preferences_are_required_and_show_initial_option(self):
		response = self.client.get(self.url, HTTP_HOST='localhost')
		self.assertContains(response, 'Selecciona una opción', count=2)

		token = response.cookies['csrftoken'].value
		invalid_data = {
			**self.data,
			'preferencia_grabacion': '',
			'lugar_grabacion': '',
			'csrfmiddlewaretoken': token,
		}
		response = self.client.post(self.url, invalid_data, HTTP_HOST='localhost')

		self.assertEqual(response.status_code, 200)
		self.assertIn('preferencia_grabacion', response.context['form'].errors)
		self.assertIn('lugar_grabacion', response.context['form'].errors)
		self.assertEqual(HistoriaPropuesta.objects.count(), 0)

	def test_post_without_csrf_is_rejected(self):
		response = self.client.post(self.url, self.data, HTTP_HOST='localhost')

		self.assertEqual(response.status_code, 403)
		self.assertEqual(HistoriaPropuesta.objects.count(), 0)

	def test_invalid_post_renders_errors_without_saving_or_notifying(self):
		token = self.csrf_token()
		invalid_data = {**self.data, 'historia': '', 'csrfmiddlewaretoken': token}

		response = self.client.post(self.url, invalid_data, HTTP_HOST='localhost')

		self.assertEqual(response.status_code, 200)
		self.assertIn('historia', response.context['form'].errors)
		self.assertEqual(HistoriaPropuesta.objects.count(), 0)
		self.assertEqual(len(mail.outbox), 0)

	@patch('applications.home.views.EmailMessage.send', side_effect=SMTPException('SMTP unavailable'))
	def test_smtp_failure_keeps_saved_proposal(self, email_send_mock):
		token = self.csrf_token()

		response = self.client.post(
			self.url,
			{**self.data, 'csrfmiddlewaretoken': token},
			HTTP_HOST='localhost',
			follow=True,
		)

		self.assertContains(response, 'Propuesta guardada con aviso pendiente')
		self.assertContains(response, 'No hace falta que la envíes de nuevo.')
		self.assertEqual(HistoriaPropuesta.objects.count(), 1)
		email_send_mock.assert_called_once()
