from typing import Any
#actualizar el campo de perfil de abogados 
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from .models import Abogado,Perfil
#importaciones para contactar
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
import requests
from django.conf import settings
#impraciones para cpntactar
from django.http import HttpResponse
from .forms import ContactForm,AbogadoForm,EmpresaForm,UsuarioForm,PeluqueriaForm

from django.utils.text import slugify
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from applications.home.models import Consulado,Embajada,Abogado,Blog,Empresa,Post,Peluqueria
from django.contrib.auth.models import User
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView
)


################################### formulario para contactar ###################################
#############################################################################################################

def formulario_contactar(request):
    print("Formulario de contactar")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        message = "Nombre: " + name + " Email: " + " Mensaje: " + message
        
        print(name, email, message)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['duarteolvin30@gmail.com','olvind78@gmail.com']
        print(email, message, from_email, recipient_list)
        send_mail(email, message, from_email, recipient_list)
        messages.add_message(request, messages.INFO, "Hemos recibido el email, en breve nos pondremos en contacto. | Emaila jaso dugu, laster harremanetan jarriko gara.")

    return render(request, "home/index.html")

#fin formulario contacar


################################### este es el apartado de ListView ###################################
#############################################################################################################

class HomePageView(ListView):
    template_name = "index.html"
    model = Blog
    context_object_name = 'datos'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()

    def get_context_data(self, **kwargs):
        # Obtén el contexto predeterminado del ListView
        context = super().get_context_data(**kwargs)
        # Añade el formulario al contexto
        context['form'] = ContactForm()  # Instancia del formulario

        # Agrega los datos de otros modelos al contexto paa ver el mapa en el iindex
        context['comercios'] = Empresa.objects.filter(tipo_empresa__nombre='Comercio')
        context['restaurantes'] = Empresa.objects.filter(tipo_empresa__nombre='Restaurante')
        context['embajadas'] = Embajada.objects.all()
        context['consulados'] = Consulado.objects.all()
        # Obtén el contexto predeterminado
        


            



            # URL de las APIs para obtener las tasas de cambio
        url = 'https://open.er-api.com/v6/latest/NIO'
        url2 = 'https://open.er-api.com/v6/latest/EUR'

        try:
            # Petición a la API para USD
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            # Extrae las tasas de cambio para NIO desde USD
            usd_to_nio = 500*(data.get('rates', {}).get('USD', None))
            if usd_to_nio:
                context['usd_rate'] = round(usd_to_nio, 2)
            else:
                context['usd_rate'] = 'No disponible'
        except requests.RequestException as e:
            context['usd_rate'] = 'Error al conectar con la API'

        try:
            # Petición a la API para EUR
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

           # Extrae las tasas de cambio para NIO desde USD
            eur_to_nio = 500*(data.get('rates', {}).get('EUR', None))
            if eur_to_nio:
                context['eur_rate'] = round(eur_to_nio, 2)
            else:
                context['eur_rate'] = 'No disponible'
        except requests.RequestException as e:
            context['eur_rate'] = 'Error al conectar con la API'

        try:
            # Petición a la API para EUR
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # Extrae las tasas de cambio para NIO desde USD
            crc_to_nio = 500*(data.get('rates', {}).get('CRC', None))
            if crc_to_nio:
                context['crc_rate'] = round(crc_to_nio, 2)
            else:
                context['crc_rate'] = 'No disponible'


        except requests.RequestException as e:
            context['crc_rate'] = 'Error al conectar con la API'


        try:
            # Petición a la API para EUR
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # Extrae las tasas de cambio para NIO desde USD
            gtq_to_nio = 500*(data.get('rates', {}).get('GTQ', None))
            if gtq_to_nio:
                context['gtq_rate'] = round(gtq_to_nio, 2)
            else:
                context['gtq_rate'] = 'No disponible'


        except requests.RequestException as e:
            context['gtq_rate'] = 'Error al conectar con la API'

        return context
















class EmbajadasView(ListView):
    template_name = "generalmap.html"

    model = Embajada
    context_object_name = 'datos'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()


class ConsuladosView(ListView):
    template_name = "generalmap.html"

    model = Consulado
    context_object_name = 'datos'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()

#fin de clase

class EmpresasView(ListView):
    template_name = "empresas_mapa.html"

    model = Empresa
    context_object_name = 'datos'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()


class AbogadosListView(ListView):
    template_name = "abogados.html"

    model = Abogado
    context_object_name = 'datos'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()




class BlogView(ListView):
    template_name = "blog.html"

    model = Blog
    context_object_name = 'datos'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()



class MapaListView(ListView):
    template_name = 'mapa.html'  # Asegúrate de tener este template
    context_object_name = 'consulados'  # Vassriable principal para el primer modelo

    def get_queryset(self):
        # El queryset principal puede ser el modelo Empresa
        return Consulado.objects.all()

    def get_context_data(self, **kwargs):
        # Llama al método original para obtener el contexto base
        context = super().get_context_data(**kwargs)
        
        # Agrega los datos de otros modelos al contexto
        context['comercios'] = Empresa.objects.filter(tipo_empresa__nombre='Comercio')
        context['restaurantes'] = Empresa.objects.filter(tipo_empresa__nombre='Restaurante')
        context['embajadas'] = Embajada.objects.all()
        return context

################################### este es el apartad de los listView ###################################
#############################################################################################################



################################### apartado de CreateView ###################################
#############################################################################################################

class CrearEmpresaCreateView(LoginRequiredMixin, CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa_crear.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Asigna el usuario actual
        nombre_url = form.cleaned_data.get('nombreUrl', '')
        nombre_url = nombre_url.lower()     #obtener el valor del campo nombreUrl ingresado por l usuario
        slugify_url = slugify(nombre_url)                       #usa slugify para convertirlo en un slugy valido
        form.instance.nombreUrl = slugify_url                   #asignar el valor trasformado al campo nombreUrl
        return super().form_valid(form)



class CrearAbogadoCreateView(LoginRequiredMixin, CreateView):
    model = Abogado
    template_name = 'abogado_crear.html'
    form_class = AbogadoForm

    def from_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CrearPeluqueriaCreateView(LoginRequiredMixin, CreateView):
    model = Peluqueria
    template_name = 'empresa_crear.html'
    form_class = PeluqueriaForm

    def from_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)





################################### apartado de CreateView ###################################
#############################################################################################################



################################### este es el apartado de los templateview ###################################
#############################################################################################################


class PreguntasView(TemplateView):
    template_name = "preguntas.html"


class AvisolegalView(TemplateView):
    template_name = "aviso_legal.html"


class PoliticasdeprivacidadView(TemplateView):
    template_name = "politicas_de_privacidad.html"


class Politicas_de_cookiesView(TemplateView):
    template_name = "politicas_de_cookies.html"


class CredencialusuarioView(TemplateView):
    template_name = "credencial_usuario.html"



################################### este es el apartado de los templateview ###################################
#############################################################################################################



################################### detail este es el apartado de los DetailView ###################################
#############################################################################################################


class AbogadosDetailView(DetailView):
    model = Abogado # Especifica el modelo Blog
    template_name = 'abogado_detalle.html' # Define el template "articulo_completo.html"
    context_object_name = 'detalle'



class BlogDetailView(DetailView):
    model = Blog # Especifica el modelo Blog
    template_name = 'articulo_completo.html' # Define el template "articulo_completo.html"
    context_object_name = 'articulo'



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Procesar los datos
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Enviar correo electrónico
            send_mail(
                subject=f"Nuevo mensaje de {name}",
                message=message,
                from_email='duarteolvin30@gmail.com',  # Usa el remitente verificado
                recipient_list=['euskodev@gmail.com','retegi84@gmail.com'],  # Cambia esto por el correo del destinatario
            )
           
            return HttpResponse('Gracias por contactarnos. Te responderemos pronto.')
    else:
        form = ContactForm()  # Instancia del formulario

    return render(request, 'index.html', {'form': form})




class EmpresaDetailView(DetailView):
    model = Empresa # Especifica el modelo Restaurante
    template_name = 'empresas/yummy-red/index.html' # Define el template "articulo_completo.html"
    context_object_name = 'datos'
    slug_field = 'nombreUrl'
    slug_url_kwarg = 'nombreUrl'



################################### detail este es el apartado de los DetailView ###################################
#############################################################################################################




################################### este es el apartado de los updateview ###################################
#############################################################################################################

class ActualizarperfilUpdateView(UpdateView):  # Actualizar el perfil de abogados
    model = User
    form_class = UsuarioForm  # Especifica el formulario personalizado
    template_name = "actualizar_usuario.html"

    def get_success_url(self):
        return reverse_lazy("home_app:credencial_usuario", kwargs={"pk": self.object.pk})



class AbogadoUpdateView(UpdateView):  # Actualizar el perfil de abogados
    model = Abogado
    form_class = AbogadoForm  # Especifica el formulario personalizado
    template_name = "abogado_actualizar.html"

    def get_success_url(self):
        return reverse_lazy("home_app:abogado_detalle", kwargs={"pk": self.object.pk})


################################### este es el apartado de los updateview ###################################
#############################################################################################################