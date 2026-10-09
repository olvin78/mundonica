from rest_framework import serializers
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


def url_or_null(value, request):
    if not value:
        return None
    try:
        return request.build_absolute_uri(value.url)
    except Exception:
        return value.url


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class PerfilSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Perfil
        fields = ['id', 'usuario', 'telefono', 'direccion', 'fecha_nacimiento', 'avatar']

    def get_avatar(self, obj):
        return url_or_null(obj.avatar, self.context.get('request'))


class ConsuladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulado
        fields = '__all__'


class EmbajadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Embajada
        fields = '__all__'


class TipoEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEmpresa
        fields = ['id', 'nombre', 'descripcion']


class EmpresaSerializer(serializers.ModelSerializer):
    tipo_empresa = TipoEmpresaSerializer(read_only=True)
    direccion = serializers.SerializerMethodField()
    latitud = serializers.SerializerMethodField()
    longitud = serializers.SerializerMethodField()

    class Meta:
        model = Empresa
        fields = [
            "id", "nombre_de_la_empresa", "nombreUrl", "tipo_empresa", "tipo_perfil",
            "descripcion_directorio", "pais", "region", "provincia", "ciudad",
            "direccion", "codigo_postal", "telefono", "email", "sitio_web",
            "latitud", "longitud", "relacion_nicaragua", "imagen_logo_empresa",
            "imagen_header", "imagen", "imagen_portada", "titulo_header",
            "subtitulo1_header", "subtitulo2_header",
        ]

    def get_direccion(self, obj):
        return obj.direccion if obj.direccion_es_publica() else None

    def _coordenadas_publicables(self, obj):
        if not obj.direccion_es_publica() or not obj.coordenadas_validas():
            return False
        try:
            return obj.importacion_perfil.precision_localizacion == "address_unverified"
        except Exception:
            return True

    def get_latitud(self, obj):
        return obj.latitud if self._coordenadas_publicables(obj) else None

    def get_longitud(self, obj):
        return obj.longitud if self._coordenadas_publicables(obj) else None

    def get_imagen_logo_empresa(self, obj):
        return url_or_null(obj.imagen_logo_empresa, self.context.get('request'))

    def get_imagen_fondo_header(self, obj):
        return url_or_null(obj.imagen_fondo_header, self.context.get('request'))

    def get_imagen_header(self, obj):
        return url_or_null(obj.imagen_header, self.context.get('request'))

    def get_imagen1_nosotros(self, obj):
        return url_or_null(obj.imagen1_nosotros, self.context.get('request'))

    def get_imagen2_nosotros_fondo(self, obj):
        return url_or_null(obj.imagen2_nosotros_fondo, self.context.get('request'))

    def get_imagen3_nosotros(self, obj):
        return url_or_null(obj.imagen3_nosotros, self.context.get('request'))

    def get_imagen1_plato_menu(self, obj):
        return url_or_null(obj.imagen1_plato_menu, self.context.get('request'))

    def get_imagen2_plato_menu(self, obj):
        return url_or_null(obj.imagen2_plato_menu, self.context.get('request'))

    def get_imagen3_plato_menu(self, obj):
        return url_or_null(obj.imagen3_plato_menu, self.context.get('request'))

    def get_imagen4_plato_menu(self, obj):
        return url_or_null(obj.imagen4_plato_menu, self.context.get('request'))

    def get_imagen5_plato_menu(self, obj):
        return url_or_null(obj.imagen5_plato_menu, self.context.get('request'))

    def get_imagen6_plato_menu(self, obj):
        return url_or_null(obj.imagen6_plato_menu, self.context.get('request'))

    def get_imagen7_plato_menu(self, obj):
        return url_or_null(obj.imagen7_plato_menu, self.context.get('request'))

    def get_imagen8_plato_menu(self, obj):
        return url_or_null(obj.imagen8_plato_menu, self.context.get('request'))

    def get_imagen9_plato_menu(self, obj):
        return url_or_null(obj.imagen9_plato_menu, self.context.get('request'))

    def get_imagen10_plato_menu(self, obj):
        return url_or_null(obj.imagen10_plato_menu, self.context.get('request'))

    def get_imagen1_comentario(self, obj):
        return url_or_null(obj.imagen1_comentario, self.context.get('request'))

    def get_imagen2_comentario(self, obj):
        return url_or_null(obj.imagen2_comentario, self.context.get('request'))

    def get_imagen3_comentario(self, obj):
        return url_or_null(obj.imagen3_comentario, self.context.get('request'))

    def get_imagen_chef1(self, obj):
        return url_or_null(obj.imagen_chef1, self.context.get('request'))

    def get_imagen_chef2(self, obj):
        return url_or_null(obj.imagen_chef2, self.context.get('request'))

    def get_imagen_chef3(self, obj):
        return url_or_null(obj.imagen_chef3, self.context.get('request'))

    def get_imagen_servicio1(self, obj):
        return url_or_null(obj.imagen_servicio1, self.context.get('request'))

    def get_imagen_servicio2(self, obj):
        return url_or_null(obj.imagen_servicio2, self.context.get('request'))

    def get_imagen_servicio3(self, obj):
        return url_or_null(obj.imagen_servicio3, self.context.get('request'))

    def get_imagen_servicio4(self, obj):
        return url_or_null(obj.imagen_servicio4, self.context.get('request'))

    def get_imagen_trabajador1(self, obj):
        return url_or_null(obj.imagen_trabajador1, self.context.get('request'))

    def get_imagen_trabajador2(self, obj):
        return url_or_null(obj.imagen_trabajador2, self.context.get('request'))

    def get_imagen_trabajador3(self, obj):
        return url_or_null(obj.imagen_trabajador3, self.context.get('request'))

    def get_imagen_tarifa1(self, obj):
        return url_or_null(obj.imagen_tarifa1, self.context.get('request'))

    def get_imagen_tarifa2(self, obj):
        return url_or_null(obj.imagen_tarifa2, self.context.get('request'))

    def get_imagen1_galeria(self, obj):
        return url_or_null(obj.imagen1_galeria, self.context.get('request'))

    def get_imagen2_galeria(self, obj):
        return url_or_null(obj.imagen2_galeria, self.context.get('request'))

    def get_imagen3_galeria(self, obj):
        return url_or_null(obj.imagen3_galeria, self.context.get('request'))

    def get_imagen4_galeria(self, obj):
        return url_or_null(obj.imagen4_galeria, self.context.get('request'))

    def get_imagen5_galeria(self, obj):
        return url_or_null(obj.imagen5_galeria, self.context.get('request'))

    def get_imagen6_galeria(self, obj):
        return url_or_null(obj.imagen6_galeria, self.context.get('request'))

    def get_imagen7_galeria(self, obj):
        return url_or_null(obj.imagen7_galeria, self.context.get('request'))

    def get_imagen8_galeria(self, obj):
        return url_or_null(obj.imagen8_galeria, self.context.get('request'))

    def get_imagen9_galeria(self, obj):
        return url_or_null(obj.imagen9_galeria, self.context.get('request'))

    def get_imagen10_galeria(self, obj):
        return url_or_null(obj.imagen10_galeria, self.context.get('request'))

    def get_imagen11_galeria(self, obj):
        return url_or_null(obj.imagen11_galeria, self.context.get('request'))

    def get_imagen_portada_reserva(self, obj):
        return url_or_null(obj.imagen_portada_reserva, self.context.get('request'))

    def get_imagen(self, obj):
        return url_or_null(obj.imagen, self.context.get('request'))

    def get_imagen_portada(self, obj):
        return url_or_null(obj.imagen_portada, self.context.get('request'))


class AbogadoSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Abogado
        fields = '__all__'

    def get_imagen(self, obj):
        return url_or_null(obj.imagen, self.context.get('request'))


class BlogSerializer(serializers.ModelSerializer):
    autor = UserSerializer(read_only=True)
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'

    def get_imagen(self, obj):
        return url_or_null(obj.imagen, self.context.get('request'))


class PostSerializer(serializers.ModelSerializer):
    autor = UserSerializer(read_only=True)
    imagen = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_imagen(self, obj):
        return url_or_null(obj.imagen, self.context.get('request'))

    def get_video(self, obj):
        return url_or_null(obj.video, self.context.get('request'))


class RecetaSerializer(serializers.ModelSerializer):
    autor = UserSerializer(read_only=True)
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Receta
        fields = '__all__'

    def get_imagen(self, obj):
        return url_or_null(obj.imagen, self.context.get('request'))
