from os import name
from django.urls import include, path
from . import views
from django.conf.urls import handler404

from .views import contact_view
from .views import editar_recetaView,EliminarRecetaView,MisRecetasView
"""
{% url 'home_app:aviso_legal' %}
{% url 'home_app:politica_de_privacidad' %}
{% url 'home_app:politica_de_cookies' %}


"""

app_name = 'home_app'

handler404 ='applications.home.views.custom_404'

urlpatterns = [
    path('',
        views.HomePageView.as_view(),
        name='home',
    ),

    path('mapa/',
        views.MapaListView.as_view(),
        name='mapa',
    ),

    path('abogados/',
        views.AbogadosListView.as_view(),
        name='abogados',
    ),

    path('abogados/<int:pk>/',
        views.AbogadosDetailView.as_view(),
        name='abogado_detalle'
        
        ),

    path('crear_abogado/',
        views.CrearAbogadoCreateView.as_view(),
        name='abogado_crear',
    ),

    path('blog/',
        views.BlogView.as_view(),
        name='blog',
    ),

    path('blog/articulo/<int:pk>/',
        views.BlogDetailView.as_view(),
        name='articulo'
        
        ),


    path('preguntas/',
        views.PreguntasView.as_view(),
        name='preguntas',
    ),
    
    path('formulario/', views.formulario_contactar, name='formulario_contactar'),


#esta es la url para la empresa de catalogo la que solo es para mostrar productos

    path('<slug:nombreUrl>/',
        views.EmpresaDetailView.as_view(),
        name='empresa_detalle'
        
    ),


    path('crear_empresa/<str:tipo_empresa>/',
        views.CrearTipodeEmpresaView.as_view(),
        name='crear_tipo_empresa'
        
    ),

#esta  url tiene que estar de ultimo para evitar conflictos con los anteriores
#ya que si esta arriba puede tomarlo como una empresa y no como abogados
    path('actualizar_abogado/<int:pk>/',
        views.AbogadoUpdateView.as_view(),
        name='abogado_actualizar',
    ),

    path('editar-receta/<int:pk>/', editar_recetaView.as_view(), name='editar_receta'),

    path('aviso_legal',
        views.AvisolegalView.as_view(),
        name='aviso_legal',
    ),

    path('Politicas de cookies',
        views.Politicas_de_cookiesView.as_view(),
        name='politicas_de_cookies',
    ),

    path('Politicas de privacidad',
        views.PoliticasdeprivacidadView.as_view(),
        name='politicas_de_privacidad',
    ),

     path('barberia/template', 
        views.BrbermasterView.as_view(), 
        name='barberia_template'),

    path('tienda/template',
        views.LeadmarckView.as_view(),
        name='tienda_template'),
 
 
    path('credencial_usuario/<int:pk>/',
        views.CredencialusuarioView.as_view(),
        name='credencial_usuario',
    ),
 
    path('actualizar_usuario/<int:pk>/',
        views.ActualizarperfilUpdateView.as_view(),
        name='actualizar_usuario',
    ),
    
    path('actualizar_empresa/<int:pk>/',
        views.ActualizartipoEmpresaView.as_view(),
        name='actualizar_empresa',
    ),
    

    path('billetes/ver',
        views.BilletesView.as_view(),
        name='billetes',
    ),
    
    path('recetas/ver',
        views.RecetasView.as_view(),
        name='recetas',
    ),
    
    path('receta/<int:pk>/',
     views.RecetaDetailView.as_view(),
     name='recetas_detalle'),


    path('galeria',
        views.GaleriaView.as_view(),
        name='galeria',
    ),

    path('crear_receta',
        views.CrearRecetaCreateView.as_view(),
        name='crear_receta',
    ),

  path('receta/eliminar/<int:pk>/', EliminarRecetaView.as_view(), name='eliminar_receta'),

  path('recetas/mis_recetas', MisRecetasView.as_view(), name='mis_recetas'),




]