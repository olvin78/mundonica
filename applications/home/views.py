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
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils.decorators import method_decorator
from .forms import ContactForm,AbogadoForm,RestauranteForm,UsuarioForm,PeluqueriaForm,EmpresaForm,ComercioForm,RecetaForm
from django.views.generic.edit import UpdateView
from django.http import Http404
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.text import slugify
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from applications.home.models import Consulado,Embajada,Abogado,Blog,Empresa,Post,Receta,Favorito,Valoracion,TipoEmpresa
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Avg, Count, Q, F
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    View,
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
        # Carrusel de negocios destacados (los más recientes en unirse a la plataforma)
        context['empresas_destacadas'] = (
            Empresa.objects.select_related('tipo_empresa')
            .annotate(rating_avg=Avg('valoraciones__puntuacion'), rating_count=Count('valoraciones', distinct=True))
            .order_by('-id')[:12]
        )
        # Marca los negocios más recientes como "Nuevo" (mismo orden -id de arriba, sin inventar fechas)
        context['ids_nuevos'] = set(
            Empresa.objects.order_by('-id').values_list('id', flat=True)[:2]
        )

        # Estadísticas REALES (no cifras de marketing infladas): conteo en vivo de la BD.
        # Meta de fundadores: es una meta pública declarada, no un dato actual disfrazado de real.
        context['total_negocios'] = Empresa.objects.count()
        context['total_ciudades'] = (
            Empresa.objects.exclude(ciudad__isnull=True).exclude(ciudad__exact='')
            .values('ciudad').distinct().count()
        )
        context['meta_fundadores'] = 50
        # IDs de empresas que el usuario ya guardó en "Me gusta", para pintar el corazón lleno
        if self.request.user.is_authenticated:
            context['favoritos_ids'] = set(
                Favorito.objects.filter(usuario=self.request.user).values_list('empresa_id', flat=True)
            )
            context['mis_valoraciones'] = dict(
                Valoracion.objects.filter(usuario=self.request.user).values_list('empresa_id', 'puntuacion')
            )
        else:
            context['favoritos_ids'] = set()
            context['mis_valoraciones'] = {}
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
            return ComercioForm


        else:
            raise Http404("Formulario no encontrado para este tipo de empresa")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tipo_empresa'] = self.kwargs.get('tipo_empresa', 'peluqueria')
        return ctx

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
            return ['empresas/leadmark/index.html']  # Template por defecto


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

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        empresa = get_object_or_404(Empresa, pk=self.kwargs['pk'])
        slug = {
            'Peluquería': 'peluqueria',
            'Restaurante': 'restaurante',
            'Empresa': 'empresa',
            'Comercio': 'comercio',
        }.get(empresa.tipo_empresa.nombre, 'peluqueria')
        ctx['tipo_empresa'] = slug
        return ctx

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


################################### Favoritos (Me gusta estilo TripAdvisor) ###################################
##################################################################################################################


class ToggleFavoritoView(LoginRequiredMixin, View):
    """Guarda/quita una empresa de los favoritos del usuario. Responde en JSON si la llamada es AJAX."""

    def post(self, request, pk):
        empresa = get_object_or_404(Empresa, pk=pk)
        favorito, created = Favorito.objects.get_or_create(usuario=request.user, empresa=empresa)
        if created:
            liked = True
        else:
            favorito.delete()
            liked = False

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'liked': liked})

        return redirect(request.META.get('HTTP_REFERER', reverse_lazy('home_app:home')))


class MisFavoritosView(LoginRequiredMixin, ListView):
    model = Empresa
    template_name = 'mis_favoritos.html'
    context_object_name = 'empresas'

    def get_queryset(self):
        return (
            Empresa.objects.filter(favoritos__usuario=self.request.user)
            .select_related('tipo_empresa')
            .annotate(rating_avg=Avg('valoraciones__puntuacion'), rating_count=Count('valoraciones', distinct=True))
            .order_by('-favoritos__fecha')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favoritos_ids'] = set(
            Favorito.objects.filter(usuario=self.request.user).values_list('empresa_id', flat=True)
        )
        context['mis_valoraciones'] = dict(
            Valoracion.objects.filter(usuario=self.request.user).values_list('empresa_id', 'puntuacion')
        )
        context['ids_nuevos'] = set()  # el badge "Nuevo" solo aplica al carrusel de la portada
        return context


################################### Fin de Favoritos ###################################
##################################################################################################################


################################### Valoraciones (estrellas estilo TripAdvisor) ###################################
######################################################################################################################


class RateEmpresaView(LoginRequiredMixin, View):
    """Crea o actualiza la valoración (1-5 estrellas) del usuario sobre un negocio."""

    def post(self, request, pk):
        empresa = get_object_or_404(Empresa, pk=pk)
        try:
            puntuacion = int(request.POST.get('puntuacion', 0))
        except (TypeError, ValueError):
            puntuacion = 0

        if puntuacion < 1 or puntuacion > 5:
            return JsonResponse({'error': 'Puntuación inválida'}, status=400)

        Valoracion.objects.update_or_create(
            usuario=request.user, empresa=empresa,
            defaults={'puntuacion': puntuacion},
        )

        agregados = Valoracion.objects.filter(empresa=empresa).aggregate(
            avg=Avg('puntuacion'), count=Count('id')
        )

        data = {
            'rating_avg': round(agregados['avg'] or 0, 1),
            'rating_count': agregados['count'],
            'rating_percent': round(((agregados['avg'] or 0) / 5) * 100, 1),
            'mi_puntuacion': puntuacion,
        }

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(data)

        return redirect(request.META.get('HTTP_REFERER', reverse_lazy('home_app:home')))


################################### Fin de Valoraciones ###################################
######################################################################################################################


################################### Directorio de negocios (estilo TripAdvisor/Booking) ###################################
###############################################################################################################################


class ExplorarNegociosView(ListView):
    """Directorio completo de negocios: buscador, filtro por categoría y orden, con paginación."""
    model = Empresa
    template_name = 'negocios.html'
    context_object_name = 'empresas'
    paginate_by = 12

    def get_queryset(self):
        queryset = (
            Empresa.objects.select_related('tipo_empresa')
            .annotate(rating_avg=Avg('valoraciones__puntuacion'), rating_count=Count('valoraciones', distinct=True))
        )

        tipo = self.request.GET.get('tipo', '').strip()
        if tipo:
            queryset = queryset.filter(tipo_empresa__nombre=tipo)

        q = self.request.GET.get('q', '').strip()
        if q:
            queryset = queryset.filter(
                Q(nombre_de_la_empresa__icontains=q) | Q(ciudad__icontains=q) | Q(pais__icontains=q)
            )

        orden = self.request.GET.get('orden', 'recientes')
        if orden == 'valorados':
            queryset = queryset.order_by(F('rating_avg').desc(nulls_last=True), '-id')
        elif orden == 'nombre':
            queryset = queryset.order_by('nombre_de_la_empresa')
        else:
            queryset = queryset.order_by('-id')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = TipoEmpresa.objects.annotate(total=Count('empresas')).order_by('nombre')
        context['total_negocios'] = Empresa.objects.count()
        context['tipo_actual'] = self.request.GET.get('tipo', '')
        context['q_actual'] = self.request.GET.get('q', '')
        context['orden_actual'] = self.request.GET.get('orden', 'recientes')

        # Dividir empresas para renderizado estilo TripAdvisor (Destacadas vs Normales)
        empresas_list = list(context['empresas'])
        context['empresas_destacadas'] = [e for e in empresas_list if e.rating_avg and e.rating_avg >= 4.0]
        context['empresas_normales'] = [e for e in empresas_list if not e.rating_avg or e.rating_avg < 4.0]

        if self.request.user.is_authenticated:
            context['favoritos_ids'] = set(
                Favorito.objects.filter(usuario=self.request.user).values_list('empresa_id', flat=True)
            )
        else:
            context['favoritos_ids'] = set()

        context['ids_nuevos'] = set(
            Empresa.objects.order_by('-id').values_list('id', flat=True)[:2]
        )
        return context


class PublicarNuevoView(LoginRequiredMixin, TemplateView):
    template_name = "publicar_nuevo.html"


@method_decorator(xframe_options_sameorigin, name='dispatch')
class PreviewPlantillaView(LoginRequiredMixin, TemplateView):
    """Renders a business template with empty context so |default: values show.
    Used inside an iframe in the creation form for real-time phone preview."""

    def get_template_names(self):
        tipo = self.kwargs.get('tipo_empresa', 'peluqueria')
        templates = {
            'peluqueria': 'empresas/brber-master/index.html',
            'restaurante': 'empresas/yummy-red/index.html',
            'comercio': 'empresas/leadmark/index.html',
            'empresa': 'empresas/leadmark/index.html',
        }
        return [templates.get(tipo, 'empresas/brber-master/index.html')]

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        tipo = self.kwargs.get('tipo_empresa', 'peluqueria')
        # Objeto de ejemplo completo para que la plantilla se vea entera en el móvil
        ctx['datos'] = datos_de_ejemplo(tipo)
        return ctx


def datos_de_ejemplo(tipo_empresa='peluqueria'):
    """Devuelve un objeto con todas las secciones de las plantillas rellenadas
    con contenido de ejemplo, para que la vista previa del móvil se vea completa.
    El contenido básico (nombre, lema, textos del header) se adapta al tipo de
    negocio para que cada plantilla se vea coherente en la vista previa."""
    from types import SimpleNamespace

    img = lambda: None

    if tipo_empresa == 'restaurante':
        nombre = 'Restaurante La Cazuela'
        nombreUrl = 'restaurante-la-cazuela'
        email = 'info@lacazuela.com'
        titulo_header = 'Disfruta de la mejor comida casera'
        subtitulo1_header = 'Platos tradicionales con ingredientes frescos'
        subtitulo2_header = 'Sabores que enamoran'
        parrafo1 = 'En La Cazuela cocinamos recetas tradicionales con productos frescos de temporada y un toque casero único.'
        parrafo2 = 'Nuestro equipo de cocina elabora cada plato al momento para que disfrutes de todo el sabor.'
        parrafo3 = 'Trabajamos con productores locales para ofrecerte la mejor calidad en cada bocado.'
        parrafo4 = 'Ambiente acogedor, atención cercana y precios justos para toda la familia.'
        parrafo5 = 'Ven y comprueba por qué somos el restaurante favorito de la ciudad.'
        titulo_servicios = 'Los mejores platos que te ofrecemos'
        titulo_tarifa = 'Nuestros precios'
        nombre_servicio1 = 'Cocina Tradicional'
        parrafo_servicios1 = 'Platos de toda la vida elaborados con recetas de la abuela y productos frescos.'
        nombre_servicio2 = 'Comida Rápida Casera'
        parrafo_servicios2 = 'Hamburguesas y bocadillos hechos al momento con ingredientes de calidad.'
        nombre_servicio3 = 'Menú del Día'
        parrafo_servicios3 = 'Menú completo a un precio inmejorable con entrada, principal y postre.'
        nombre_servicio4 = 'Servicio a Domicilio'
        titulo_trabajadores = 'Nuestro equipo de cocina para ti'
        nombre_trabajador1 = 'María López'
        nombre_trabajador2 = 'José Ramírez'
        nombre_trabajador3 = 'Carlos Mendoza'
        titulo1_galeria = 'Algunas imágenes de nuestro restaurante'
        nombre_servicio1_tarifa = 'Menú Ejecutivo'
        precio_servicio1_tarifa = '12'
        nombre_servicio2_tarifa = 'Plato del Día'
        precio_servicio2_tarifa = '9'
        nombre_servicio3_tarifa = 'Menú Infantil'
        precio_servicio3_tarifa = '7'
        nombre_servicio4_tarifa = 'Menú Parejas'
        precio_servicio4_tarifa = '22'
        nombre_servicio5_tarifa = 'Carta a la Carta'
        precio_servicio5_tarifa = '15'
        nombre_servicio6_tarifa = 'Menú Degustación'
        precio_servicio6_tarifa = '28'
        nombre_servicio7_tarifa = 'Menú Celiacos'
        precio_servicio7_tarifa = '13'
        nombre_servicio8_tarifa = 'Postre Casero'
        precio_servicio8_tarifa = '4'
        nombre_servicio9_tarifa = 'Bebida'
        precio_servicio9_tarifa = '2.5'
        nombre_servicio10_tarifa = 'Café'
        precio_servicio10_tarifa = '1.5'
        nombre1_comentario = 'Laura Gómez'
        parrafo1_comentario = 'La comida está deliciosa, parece comida de casa. Volveré seguro.'
        nombre2_comentario = 'Miguel Torres'
        parrafo2_comentario = 'El mejor restaurante de la zona, atención excelente y precios justos.'
        nombre3_comentario = 'Ana Ruiz'
        parrafo3_comentario = 'Recomendado al 100%. El menú del día es una maravilla.'
    elif tipo_empresa in ('comercio', 'empresa'):
        nombre = 'Tienda Mundo Nica'
        nombreUrl = 'tienda-mundo-nica'
        email = 'info@tiendamundonica.com'
        titulo_header = 'Encuentra todo lo que necesitas'
        subtitulo1_header = 'Productos de calidad al mejor precio'
        subtitulo2_header = 'Tu tienda de confianza'
        parrafo1 = 'En Tienda Mundo Nica ofrecemos una amplia variedad de productos con la mejor relación calidad-precio.'
        parrafo2 = 'Nuestro equipo te asesora para que encuentres exactamente lo que buscas.'
        parrafo3 = 'Contamos con las mejores marcas y atención personalizada.'
        parrafo4 = 'Entrega rápida, garantía y facilidades de pago.'
        parrafo5 = 'Ven y comprueba por qué somos la tienda favorita de la ciudad.'
        titulo_servicios = 'Los mejores productos que te ofrecemos'
        titulo_tarifa = 'Nuestros precios'
        nombre_servicio1 = 'Ropa y Moda'
        parrafo_servicios1 = 'Prendas de vestir actuales para toda la familia con las mejores marcas.'
        nombre_servicio2 = 'Electrónica'
        parrafo_servicios2 = 'Equipos y accesorios tecnológicos con garantía y precios competitivos.'
        nombre_servicio3 = 'Hogar y Decoración'
        parrafo_servicios3 = 'Todo para tu casa con estilos modernos y funcionales.'
        nombre_servicio4 = 'Atención al Cliente'
        titulo_trabajadores = 'Nuestro equipo para ti'
        nombre_trabajador1 = 'Sofía Herrera'
        nombre_trabajador2 = 'Andrés Castro'
        nombre_trabajador3 = 'Lucía Navarro'
        titulo1_galeria = 'Algunas imágenes de nuestra tienda'
        nombre_servicio1_tarifa = 'Ropa Premium'
        precio_servicio1_tarifa = '25'
        nombre_servicio2_tarifa = 'Zapatos'
        precio_servicio2_tarifa = '35'
        nombre_servicio3_tarifa = 'Accesorios'
        precio_servicio3_tarifa = '10'
        nombre_servicio4_tarifa = 'Tecnología'
        precio_servicio4_tarifa = '50'
        nombre_servicio5_tarifa = 'Decoración'
        precio_servicio5_tarifa = '15'
        nombre_servicio6_tarifa = 'Ropa Infantil'
        precio_servicio6_tarifa = '18'
        nombre_servicio7_tarifa = 'Perfumería'
        precio_servicio7_tarifa = '22'
        nombre_servicio8_tarifa = 'Ropa Deportiva'
        precio_servicio8_tarifa = '30'
        nombre_servicio9_tarifa = 'Bolsos'
        precio_servicio9_tarifa = '28'
        nombre_servicio10_tarifa = 'Calzado Casual'
        precio_servicio10_tarifa = '32'
        nombre1_comentario = 'Pedro Salazar'
        parrafo1_comentario = 'Excelente atención y productos de gran calidad. Muy recomendable.'
        nombre2_comentario = 'Marta Delgado'
        parrafo2_comentario = 'Todo lo que buscaba y a muy buen precio. Volveré a comprar.'
        nombre3_comentario = 'Luis Vargas'
        parrafo3_comentario = 'Buen servicio y variedad de productos. La mejor tienda de la zona.'
    else:
        nombre = 'Barbería Patrick Porter'
        nombreUrl = 'barberia-patrick-porter'
        email = 'info@patrickporter.com'
        titulo_header = 'Cortes que te hacen lucir elegante'
        subtitulo1_header = 'Con Patrick Porter'
        subtitulo2_header = 'Siéntete más seguro'
        parrafo1 = 'En Patrick Porter ofrecemos cortes de cabello, barba y estilos modernos con los mejores profesionales del sector.'
        parrafo2 = 'Nuestro equipo te asesora para que salgas con el look perfecto, sin cita previa y a los mejores precios.'
        parrafo3 = 'Usamos productos de alta calidad y técnicas actualizadas para el cuidado de tu cabello y barba.'
        parrafo4 = 'Atención personalizada, ambiente agradable y resultados garantizados.'
        parrafo5 = 'Ven y comprueba por qué somos la barbería favorita de la ciudad.'
        titulo_servicios = 'Los mejores servicios que te ofrecemos'
        titulo_tarifa = 'Nuestros precios'
        nombre_servicio1 = 'Corte de Cabello'
        parrafo_servicios1 = 'Corte de cabello clásico o moderno según tu estilo, con acabados profesionales.'
        nombre_servicio2 = 'Masaje Facial'
        parrafo_servicios2 = 'Masaje relajante para el cuidado de tu piel y barba con productos naturales.'
        nombre_servicio3 = 'Arreglo de Barba'
        parrafo_servicios3 = 'Perfilado y arreglo de barba con precisión para un look impecable.'
        nombre_servicio4 = 'Paquetes Especiales'
        titulo_trabajadores = 'Nuestros premiados expertos para ti'
        nombre_trabajador1 = 'Guy C. Pulido'
        nombre_trabajador2 = 'Steve L. Nolan'
        nombre_trabajador3 = 'Edgar P. Mathis'
        titulo1_galeria = 'Algunas imágenes de nuestra barbería'
        nombre_servicio1_tarifa = 'Corte'
        precio_servicio1_tarifa = '15'
        nombre_servicio2_tarifa = 'Corte + Barba'
        precio_servicio2_tarifa = '25'
        nombre_servicio3_tarifa = 'Corte + Tinte'
        precio_servicio3_tarifa = '35'
        nombre_servicio4_tarifa = 'Onda permanente'
        precio_servicio4_tarifa = '40'
        nombre_servicio5_tarifa = 'Corte + Estilo'
        precio_servicio5_tarifa = '20'
        nombre_servicio6_tarifa = 'Combo Completo'
        precio_servicio6_tarifa = '45'
        nombre_servicio7_tarifa = 'Corte + Tinte'
        precio_servicio7_tarifa = '35'
        nombre_servicio8_tarifa = 'Solo Barba'
        precio_servicio8_tarifa = '10'
        nombre_servicio9_tarifa = 'Afeitado'
        precio_servicio9_tarifa = '12'
        nombre_servicio10_tarifa = 'Recorte de barba'
        precio_servicio10_tarifa = '10'
        nombre1_comentario = 'Saul Goodman'
        parrafo1_comentario = 'Excelente servicio y trato increíble. Salió tal y como quería mi corte.'
        nombre2_comentario = 'Sara Wilsson'
        parrafo2_comentario = 'El mejor lugar para arreglarse la barba. Recomendado al 100%.'
        nombre3_comentario = 'Jena Karlis'
        parrafo3_comentario = 'Ambiente genial y profesionales que saben lo que hacen.'

    return SimpleNamespace(
        # ── Básicos / Header ──
        header_activo=True,
        servicios_activo=True,
        trabajadores_activo=True,
        tarifa_activo=True,
        id=1,
        nombre_de_la_empresa=nombre,
        nombreUrl=nombreUrl,
        titulo_header=titulo_header,
        subtitulo1_header=subtitulo1_header,
        subtitulo2_header=subtitulo2_header,
        video_header='https://www.youtube.com/watch?v=ejemplo',
        telefono='+34 612 345 678',
        email=email,
        correo=email,
        direccion='Calle Mayor 12, Madrid',
        ciudad='Madrid',
        pais='España',
        latitud=40.4168,
        longitud=-3.7038,
        horario='9AM - 20PM',
        titulo_ubicacion_mapa='Encuéntranos aquí',

        # ── Logo e imágenes ──
        imagen_logo_empresa=img(),
        imagen_header=img(),
        imagen_fondo_header=img(),
        imagen_servicio1=img(),
        imagen_servicio2=img(),
        imagen_servicio3=img(),
        imagen1_nosotros=img(),
        imagen2_nosotros_fondo=img(),
        imagen3_nosotros=img(),
        imagen1_galeria=img(),
        imagen2_galeria=img(),
        imagen3_galeria=img(),
        imagen4_galeria=img(),
        imagen5_galeria=img(),
        imagen6_galeria=img(),
        imagen7_galeria=img(),
        imagen8_galeria=img(),

        # ── Sobre Nosotros ──
        quienes_somos_activo=True,
        titulo_sobrenosotros='Más de 15 años de experiencia',
        parrafo1_sobrenosotros=parrafo1,
        parrafo2_sobrenosotros=parrafo2,
        parrafo3_sobrenosotros=parrafo3,
        parrafo4_sobrenosotros=parrafo4,
        parrafo5_sobrenosotros=parrafo5,
        video_nosotros='https://www.youtube.com/watch?v=ejemplo',

        # ── Servicios ──
        titulo_servicios=titulo_servicios,
        nombre_servicio1=nombre_servicio1,
        parrafo_servicios1=parrafo_servicios1,
        nombre_servicio2=nombre_servicio2,
        parrafo_servicios2=parrafo_servicios2,
        nombre_servicio3=nombre_servicio3,
        parrafo_servicios3=parrafo_servicios3,
        nombre_servicio4=nombre_servicio4,

        # ── Equipo ──
        titulo_trabajadores=titulo_trabajadores,
        nombre_trabajador1=nombre_trabajador1,
        nombre_trabajador2=nombre_trabajador2,
        nombre_trabajador3=nombre_trabajador3,
        imagen_trabajador1=img(),
        imagen_trabajador2=img(),
        imagen_trabajador3=img(),

        # ── Tarifas / Precios ──
        titulo_tarifa=titulo_tarifa,
        nombre_servicio1_tarifa=nombre_servicio1_tarifa,
        precio_servicio1_tarifa=precio_servicio1_tarifa,
        nombre_servicio2_tarifa=nombre_servicio2_tarifa,
        precio_servicio2_tarifa=precio_servicio2_tarifa,
        nombre_servicio3_tarifa=nombre_servicio3_tarifa,
        precio_servicio3_tarifa=precio_servicio3_tarifa,
        nombre_servicio4_tarifa=nombre_servicio4_tarifa,
        precio_servicio4_tarifa=precio_servicio4_tarifa,
        nombre_servicio5_tarifa=nombre_servicio5_tarifa,
        precio_servicio5_tarifa=precio_servicio5_tarifa,
        nombre_servicio6_tarifa=nombre_servicio6_tarifa,
        precio_servicio6_tarifa=precio_servicio6_tarifa,
        nombre_servicio7_tarifa=nombre_servicio7_tarifa,
        precio_servicio7_tarifa=precio_servicio7_tarifa,
        nombre_servicio8_tarifa=nombre_servicio8_tarifa,
        precio_servicio8_tarifa=precio_servicio8_tarifa,
        nombre_servicio9_tarifa=nombre_servicio9_tarifa,
        precio_servicio9_tarifa=precio_servicio9_tarifa,
        nombre_servicio10_tarifa=nombre_servicio10_tarifa,
        precio_servicio10_tarifa=precio_servicio10_tarifa,

        # ── Galería ──
        titulo1_galeria=titulo1_galeria,

        # ── Menú / Platos (restaurante) ──
        platos_menu_activo=True,
        nombre1_plato_menu='Ternera Estofada',
        descriptcion1_plato_menu='Ternera cocinada a fuego lento con verduras frescas.',
        precio1_plato_menu='12.50',
        nombre2_plato_menu='Pollo Asado',
        descriptcion2_plato_menu='Pollo asado al horno con especias y guarnición.',
        precio2_plato_menu='9.95',
        nombre3_plato_menu='Pasta Alfredo',
        descriptcion3_plato_menu='Pasta fresca con salsa cremosa Alfredo y queso parmesano.',
        precio3_plato_menu='10.50',
        nombre4_plato_menu='Ensalada César',
        descriptcion4_plato_menu='Lechuga fresca, pollo, crutones y aderezo César.',
        precio4_plato_menu='7.95',
        nombre5_plato_menu='Filete a la Plancha',
        descriptcion5_plato_menu='Filete de ternera a la plancha con patatas.',
        precio5_plato_menu='14.50',
        nombre6_plato_menu='Salmón a la Parrilla',
        descriptcion6_plato_menu='Salmón fresco a la parrilla con limón y hierbas.',
        precio6_plato_menu='15.95',
        imagen1_plato_menu=img(),
        imagen2_plato_menu=img(),
        imagen3_plato_menu=img(),
        imagen4_plato_menu=img(),
        imagen5_plato_menu=img(),
        imagen6_plato_menu=img(),

        # ── Comentarios ──
        comentarios_activo=True,
        nombre1_comentario=nombre1_comentario,
        parrafo1_comentario=parrafo1_comentario,
        nombre2_comentario=nombre2_comentario,
        parrafo2_comentario=parrafo2_comentario,
        nombre3_comentario=nombre3_comentario,
        parrafo3_comentario=parrafo3_comentario,
        imagen1_comentario=img(),
        imagen2_comentario=img(),
        imagen3_comentario=img(),

        # ── Eventos ──
        eventos_activo=True,
        imagen_portada_reserva=img(),
        imagen_chef1=img(),
        imagen_chef2=img(),
        imagen_chef3=img(),

        # ── Chefs ──
        chefs_activo=True,
        nombre_chef1='Walter White',
        nombre_chef2='Sarah Jhonson',
        nombre_chef3='William Anderson',

        # ── Otras secciones ──
        menu_regalo_activo=True,
        menu_oferta1='<p>Menú degustación para una persona con entrada, plato principal y postre.</p>',
        menu_oferta2='<p>Menú especial para parejas con maridaje incluido.</p>',
        menu_oferta3='<p>Cena completa para cuatro personas con bebidas.</p>',
        clientes_activo=True,
        reservar_activo=True,
        galeria_activo=True,
        contactar_activo=True,
        propietario_sitio_web=None,
    )


################################### Fin Directorio de negocios ###################################
###############################################################################################################################