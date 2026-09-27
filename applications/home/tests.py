from unittest.mock import patch
from smtplib import SMTPException

from django.core import mail
from django.test import Client, TestCase, override_settings
from django.urls import reverse

from .models import HistoriaPropuesta


@override_settings(
	EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
	EMAIL_HOST_USER='smtp-login@example.test',
	EMAIL_HOST_PASSWORD='test-password',
	DEFAULT_FROM_EMAIL='info@mundonica.org',
	HISTORIAS_NOTIFICATION_EMAIL='euskodev@gmail.com',
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
		self.assertEqual(len(mail.outbox), 1)
		self.assertEqual(mail.outbox[0].to, ['euskodev@gmail.com'])

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

		self.assertContains(response, 'Enviado correctamente')
		self.assertEqual(HistoriaPropuesta.objects.count(), 1)
		email_send_mock.assert_called_once()
