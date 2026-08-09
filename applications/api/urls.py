from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = DefaultRouter()
router.register(r'usuarios', views.UserViewSet, basename='usuario')
router.register(r'perfiles', views.PerfilViewSet, basename='perfil')
router.register(r'consulados', views.ConsuladoViewSet, basename='consulado')
router.register(r'embajadas', views.EmbajadaViewSet, basename='embajada')
router.register(r'tipos-empresa', views.TipoEmpresaViewSet, basename='tipo-empresa')
router.register(r'empresas', views.EmpresaViewSet, basename='empresa')
router.register(r'abogados', views.AbogadoViewSet, basename='abogado')
router.register(r'blog', views.BlogViewSet, basename='blog')
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'recetas', views.RecetaViewSet, basename='receta')

urlpatterns = [
    path('auth/token/', obtain_auth_token, name='obtener-token'),
    path('', include(router.urls)),
]
