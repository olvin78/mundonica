from rest_framework import viewsets, permissions, filters
from django.contrib.auth.models import User

from applications.home.models import (
    Consulado,
    Embajada,
    TipoEmpresa,
    Empresa,
    Abogado,
    Blog,
    Post,
    Perfil,
    Receta,
)
from .serializers import (
    UserSerializer,
    PerfilSerializer,
    ConsuladoSerializer,
    EmbajadaSerializer,
    TipoEmpresaSerializer,
    EmpresaSerializer,
    AbogadoSerializer,
    BlogSerializer,
    PostSerializer,
    RecetaSerializer,
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PerfilViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Perfil.objects.select_related('usuario').all()
    serializer_class = PerfilSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ConsuladoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Consulado.objects.all()
    serializer_class = ConsuladoSerializer
    permission_classes = [permissions.AllowAny]


class EmbajadaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Embajada.objects.all()
    serializer_class = EmbajadaSerializer
    permission_classes = [permissions.AllowAny]


class TipoEmpresaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoEmpresa.objects.all()
    serializer_class = TipoEmpresaSerializer
    permission_classes = [permissions.AllowAny]


class EmpresaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Empresa.objects.select_related('tipo_empresa', 'propietario_sitio_web').all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre_de_la_empresa', 'pais', 'ciudad', 'titulo_header', 'nombreUrl']
    ordering_fields = ['nombre_de_la_empresa', 'pais', 'ciudad']
    lookup_field = 'nombreUrl'
    lookup_url_kwarg = 'nombreUrl'

    def get_queryset(self):
        queryset = super().get_queryset()
        tipo = self.request.query_params.get('tipo')
        if tipo:
            queryset = queryset.filter(tipo_empresa__nombre__iexact=tipo)
        return queryset


class AbogadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Abogado.objects.all()
    serializer_class = AbogadoSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'apellido', 'pais', 'ciudad']
    ordering_fields = ['pais', 'ciudad', 'nombre']


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.select_related('autor').order_by('-fecha_hora')
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'categoria', 'resumen']
    ordering_fields = ['fecha_hora', 'titulo']


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.select_related('autor').order_by('-fecha_hora')
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


class RecetaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Receta.objects.select_related('autor').order_by('-fecha_hora')
    serializer_class = RecetaSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'categoria', 'resumen']
    ordering_fields = ['fecha_hora', 'titulo']

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria = self.request.query_params.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        return queryset
