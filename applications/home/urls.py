from os import name
from django.urls import include, path
from . import views
from django.conf.urls import handler404

from .views import contact_view
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

    path('registro_empresa/',
        views.CrearEmpresaCreateView.as_view(),
        name='empresa_crear',
    ),


    path('abogados/',
        views.AbogadosListView.as_view(),
        name='abogados',
    ),

    path('abogados/<int:pk>/',
        views.AbogadosDetailView.as_view(),
        name='abogado_detalle'
        
        ),


    path('registro_abogado/',
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

#esta  url tiene que estar de ultimo para evitar conflictos con los anteriores
#ya que si esta arriba puede tomarlo como una empresa y no como abogados
    path('<slug:nombreUrl>/',
        views.EmpresaDetailView.as_view(),
        name='empresa_detalle'
        
    ),


]