from typing import Any
#actualizar el campo de perfil de abogados 
from django.urls import reverse_lazy
from django.shortcuts import redirect
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
from .forms import ContactForm,AbogadoForm,RestauranteForm,UsuarioForm,PeluqueriaForm,EmpresaForm,ComercioForm,RecetaForm
from django.views.generic.edit import UpdateView
from django.http import Http404
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.text import slugify
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from applications.home.models import Consulado,Embajada,Abogado,Blog,Empresa,Post,Receta
from django.contrib.auth.models import User
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
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
        return queryset.order_by('-fecha_hora')[:3]
    def custom_404_view(request, exception):
        return render(request, '404.html', {}, status=404)

    def get_context_data(self, **kwargs):
        # Obtén el contexto predeterminado del ListView
        context = super().get_context_data(**kwargs)
        # Añade el formulario al contexto
        context['form'] = ContactForm()  # Instancia del formulario

        # Agrega los datos de otros modelos al contexto paa ver el mapa en el index
        context['empresas'] = Empresa.objects.filter(tipo_empresa__nombre='Empresa')
        context['embajadas'] = Embajada.objects.all()
        context['consulados'] = Consulado.objects.all()
        context['peluquerias'] = Empresa.objects.filter(tipo_empresa__nombre='Peluquería')
        context['comercios'] = Empresa.objects.filter(tipo_empresa__nombre='Comercio')
        # En tu vista filtrado de empresa por usuario
        if self.request.user.is_authenticated:
            context['empresasDeUsuario'] = Empresa.objects.filter(propietario_sitio_web=self.request.user)
        else:
            context['empresasDeUsuario'] = Empresa.objects.none()  # Devuelve un queryset vacío si no está autenticado

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
        return super().get_queryset().order_by('-fecha_hora')  # Ordena por fecha descendente



class MapaListView(ListView):
    template_name = 'mapa.html'  # Asegúrate de tener este template
    context_object_name = 'consulados'  # Vassriable principal para el primer modelo

    def get_queryset(self):
        # El queryset principal puede ser el modelo Empresa
        return Consulado.objects.all()

    def get_context_data(self, **kwargs):
        # Llama al método original para obtener el contexto base
        context = super().get_context_data(**kwargs)
        
        # Agrega los datos de otros modelos al contexto paa ver el mapa en el index
        context['empresas'] = Empresa.objects.all()
        context['embajadas'] = Embajada.objects.all()
        context['consulados'] = Consulado.objects.all()
        context['peluquerias'] = Empresa.objects.filter(tipo_empresa__nombre='Peluquería')
        context['comercios'] = Empresa.objects.filter(tipo_empresa__nombre='Comercio')

        return context

################################### este es el apartad de los listView ###################################
#############################################################################################################



################################### apartado de CreateView ###################################
#############################################################################################################


class CrearAbogadoCreateView(LoginRequiredMixin, CreateView):
    model = Abogado
    template_name = 'abogado_crear.html'
    form_class = AbogadoForm

    def from_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


#prueba para adjuntar las vistas de empresa en una sola

class CrearTipodeEmpresaView(LoginRequiredMixin, CreateView):
    model = Empresa
    template_name = 'empresa_crear.html'
    success_url = reverse_lazy('home_app:home')  # Cambia por la URL que necesites

    # Sobrescribimos el método para elegir el formulario dinámicamente
    def get_form_class(self):
        tipo_empresa = self.kwargs.get('tipo_empresa')  # Corrección: 'kwargs' en lugar de 'kwards'
        if tipo_empresa == 'peluqueria':
            return PeluqueriaForm
        elif tipo_empresa == 'restaurante':
            return RestauranteForm

        elif tipo_empresa == 'empresa':
            return EmpresaForm

        elif tipo_empresa == 'comercio':
            return EmpresaForm


        else:
            raise Http404("Formulario no encontrado para este tipo de empresa")

    # Sobrescribimos el método form_valid para asignar el usuario actual
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.propietario_sitio_web = self.request.user
        return super().form_valid(form)







class CrearRecetaCreateView(LoginRequiredMixin, CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = "crear_receta.html"
    success_url = reverse_lazy('home_app:recetas')  # 🔹 Usa reverse_lazy aquí

    def form_valid(self, form):
        form.instance.autor = self.request.user  # Asigna el usuario autenticado
        return super().form_valid(form)



class RecetasView(ListView):
    model = Receta
    template_name = "recetas.html"
    context_object_name = "recetas"

    def get_queryset(self):
        queryset = Receta.objects.all().order_by('-id')  # Ordena de más reciente a más antigua
        categoria = self.request.GET.get('categoria')  # Obtiene la categoría de la URL
        
        if categoria:  # Si hay una categoría en la URL, filtra
            queryset = queryset.filter(categoria=categoria)
        
        return queryset

# Vista para Editar Receta (Solo el Autor Puede Editar)
class EditarRecetaView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Receta
    fields = ['titulo', 'categoria', 'imagen', 'resumen', 'cuerpo']
    template_name = "editar_receta.html"

    def get_success_url(self):
        return reverse_lazy('home_app:recetas_detalle', kwargs={'pk': self.object.pk})

    def test_func(self):
        """Solo el autor de la receta puede editarla"""
        receta = self.get_object()
        return self.request.user == receta.autor


# Vista para Eliminar Receta (Solo el Autor Puede Eliminar)

class EliminarRecetaView(DeleteView):
    model = Receta
    template_name = "confirmar_eliminar.html"  # Puedes crear una plantilla de confirmación
    success_url = reverse_lazy('home_app:recetas')  # Redirige a la lista de recetas

    def get_queryset(self):
        """Asegura que solo el autor pueda eliminar su propia receta"""
        return Receta.objects.filter(autor=self.request.user)

class MisRecetasView(ListView):
    model = Receta
    template_name = "recetas.html"
    context_object_name = "recetas"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Receta.objects.filter(autor=self.request.user).order_by('-id')
            return queryset
        return Receta.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context['recetas']:  # Si no hay recetas del usuario
            context['no_recetas_message'] = "Lo siento, aún no has creado recetas."
        return context

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

class BrbermasterView(TemplateView):
    template_name = "empresas/brber-master/index.html"

class LeadmarckView(TemplateView):
    template_name = "empresas/leadmark/index.html"


class BilletesView(TemplateView):
    template_name = "billetes.html"

class GaleriaView(TemplateView):
    template_name = "galeria.html"


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


#esta es la vista de empresa de restaurante
#termina la vista de empresa de catalogo o para otras empresas


class EmpresaDetailView(DetailView):
    model = Empresa  # Especifica el modelo
    context_object_name = 'datos'
    slug_field = 'nombreUrl'
    slug_url_kwarg = 'nombreUrl'

    def get_template_names(self):
        # Obtén el objeto actual basado en el slug
        empresa = self.get_object()

        # Verifica el tipo de empresa y asigna el template correspondiente
        if empresa.tipo_empresa.nombre == 'Peluquería':  # Ajusta según el campo relacionado
            return ['empresas/brber-master/index.html']
        elif empresa.tipo_empresa.nombre == 'Restaurante':
            return ['empresas/yummy-red/index.html']
        elif empresa.tipo_empresa.nombre == 'Comercio':
            return ['empresas/leadmark/index.html']
        else:
            return ['empresas/default_detail.html']  # Template por defecto


class RecetaDetailView(DetailView):
    model = Receta # Especifica el modelo Blog
    template_name = 'receta_detalle.html' # Define el template "articulo_completo.html"
    context_object_name = 'datos'


################################### detail este es el apartado de los DetailView ###################################
#############################################################################################################




################################### este es el apartado de los updateview ###################################
#############################################################################################################


class ActualizarperfilUpdateView(LoginRequiredMixin, UpdateView):
    model = Perfil
    fields = ['telefono', 'avatar']
    template_name = "actualizar_usuario.html"

    def get_object(self, queryset=None):
        """
        Sobrescribe el método para asegurarse de que el usuario solo pueda editar su propio perfil.
        """
        try:
            return self.request.user.perfil  # Obtiene el perfil asociado al usuario logueado
        except Perfil.DoesNotExist:
            raise Http404("Perfil no encontrado")  # Si no existe, lanza una excepción 404

    def form_valid(self, form):
        """
        Maneja la subida de archivos y elimina el avatar anterior solo después de guardar el nuevo.
        """
        # Obtén el nuevo archivo subido
        new_avatar = self.request.FILES.get('avatar')

        # Si hay un nuevo archivo subido, procesa
        if new_avatar:
            # Almacena temporalmente el avatar actual antes de sobrescribirlo
            old_avatar = self.object.avatar

            # Asocia el nuevo archivo al objeto
            self.object.avatar = new_avatar

            # Guarda el nuevo avatar y procesa la respuesta
            response = super().form_valid(form)

            # Elimina el avatar anterior después de guardar el nuevo
            if old_avatar:
                old_avatar.delete(save=False)

            return response

        # Si no hay archivo nuevo, procede normalmente
        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirige a la página de perfil del usuario tras guardar los cambios.
        """
        return reverse_lazy('home_app:credencial_usuario', kwargs={'pk': self.object.pk})



        
class AbogadoUpdateView(UpdateView):  # Actualizar el perfil de abogados
    model = Abogado
    form_class = AbogadoForm  # Especifica el formulario personalizado
    template_name = "abogado_actualizar.html"

    def get_success_url(self):
        return reverse_lazy("home_app:abogado_detalle", kwargs={"pk": self.object.pk})


# este apartado es para crear la vista para poder modificar las empresas


class ActualizartipoEmpresaView(LoginRequiredMixin, UpdateView):
    model = Empresa
    template_name = 'empresa_crear.html'
    success_url = reverse_lazy('home_app:home')  # Cambia por la URL adecuada

    def get_form_class(self):
        # Obtener la instancia de la empresa usando el id (pk) proporcionado en la URL
        empresa = get_object_or_404(Empresa, pk=self.kwargs['pk'])
        print(empresa.tipo_empresa)
        # Seleccionar el formulario basado en el tipo de empresa
        if empresa.tipo_empresa.nombre == 'Peluquería':
            return PeluqueriaForm
        elif empresa.tipo_empresa.nombre == 'Restaurante':
            return RestauranteForm
        elif empresa.tipo_empresa.nombre == 'Empresa':
            return EmpresaForm
        elif empresa.tipo_empresa.nombre == 'Comercio':
            return ComercioForm
        else:
            raise Http404("Formulario no encontrado para este tipo de empresa")

    def form_valid(self, form):
        # Asignar el usuario actual antes de guardar
        form.instance.propietario_sitio_web = self.request.user
        return super().form_valid(form)



class editar_recetaView(UpdateView):
    model = Receta  # Especifica el modelo Receta
    form_class = RecetaForm  # Usa el formulario RecetaForm
    template_name = "editar_receta.html"  # Plantilla para editar la receta

    def get_success_url(self):
        # Asegúrate de usar "pk" en lugar de "id"
        return reverse_lazy("home_app:recetas_detalle", kwargs={"pk": self.object.pk})


################################### este es el apartado de los updateview ###################################
#############################################################################################################