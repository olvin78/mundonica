from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from urllib.parse import parse_qs, urlparse
import re


def normalizar_youtube_id(value):
    """Devuelve un ID de YouTube de 11 caracteres o lanza ValidationError."""
    from django.core.exceptions import ValidationError

    candidate = (value or '').strip()
    if re.fullmatch(r'[A-Za-z0-9_-]{11}', candidate):
        return candidate

    parsed = urlparse(candidate)
    hostname = (parsed.hostname or '').lower()
    if hostname == 'youtu.be':
        video_id = parsed.path.strip('/').split('/')[0]
    elif hostname in {'youtube.com', 'www.youtube.com', 'm.youtube.com'}:
        if parsed.path == '/watch':
            video_id = parse_qs(parsed.query).get('v', [''])[0]
        elif parsed.path.startswith('/shorts/') or parsed.path.startswith('/embed/'):
            video_id = parsed.path.split('/')[2]
        else:
            video_id = ''
    else:
        video_id = ''

    if not re.fullmatch(r'[A-Za-z0-9_-]{11}', video_id):
        raise ValidationError('Introduce una URL de YouTube válida o un ID de 11 caracteres.')
    return video_id

# Create your models here.
#stes es el molde de los consulados
class Consulado(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Consulado")
    pais = models.CharField(max_length=100, verbose_name="Pais del Consulado")
    ciudad = models.CharField(max_length=100, verbose_name="Nombre de la Ciudad")
    direccion = models.TextField(verbose_name="Direccion", null=True, blank=True)
    telefono = models.CharField(max_length=100, verbose_name="Numero de telefono", null=True, blank=True)
    email = models.EmailField(verbose_name="Correo electronico", null=True, blank=True)
    latitud = models.CharField(max_length=100,  verbose_name="Latitud", null=True, blank=True)
    longitud = models.CharField(max_length=100,  verbose_name="Longitud", null=True, blank=True)
    titulo = models.CharField(max_length=100, verbose_name="titulo", null=True, blank=True)
    descripcion = models.CharField(max_length=100, verbose_name="descripcion", null=True, blank=True)

    class Meta:
        verbose_name = "Consulado"
        verbose_name_plural = "Consulados"
        ordering = ["pais", "ciudad"]


    def __str__(self):
        return f"{self.nombre} - {self.ciudad}, - {self.pais}"
    


#este es el molde de las embajadas

class Embajada(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Embajada")
    pais = models.CharField(max_length=100, verbose_name="Pais del Embajada")
    ciudad = models.CharField(max_length=100, verbose_name="Nombre de la Ciudad")
    direccion = models.TextField(verbose_name="Direccion", null=True, blank=True)
    telefono = models.CharField(max_length=100, verbose_name="Numero de telefono", null=True, blank=True)
    email = models.EmailField(verbose_name="Correo electronico", null=True, blank=True)
    latitud = models.CharField(max_length=100,  verbose_name="Latitud", null=True, blank=True)
    longitud = models.CharField(max_length=100,  verbose_name="Longitud", null=True, blank=True)
    titulo = models.CharField(max_length=100, verbose_name="titulo", null=True, blank=True)
    descripcion = models.CharField(max_length=100, verbose_name="descripcion", null=True, blank=True)




    class Meta:
        verbose_name = "Embajada"
        verbose_name_plural = "Embajadas"
        ordering = ["pais", "ciudad"]


    def __str__(self):
        return f"{self.nombre} - {self.ciudad}, - {self.pais}"



class TipoEmpresa(models.Model):
    PLANTILLAS = [("generica", "Genérica"), ("restaurante", "Restaurante"), ("peluqueria", "Peluquería"), ("comercio", "Comercio")]

    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Tipo de Empresa")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    plantilla_perfil = models.CharField(max_length=20, choices=PLANTILLAS, default="generica", verbose_name="Plantilla de perfil")

    class Meta:
        verbose_name = "Tipo de Empresa"
        verbose_name_plural = "Tipos de Empresa"

    def __str__(self):
        return self.nombre





    ################# modelo de empresa unificar los modelos  ##################
    ############################################################################


class Empresa(models.Model):
    TIPOS_PERFIL = [("business", "Empresa o negocio"), ("organization", "Asociación u organización"), ("person", "Profesional o persona"), ("project", "Proyecto o iniciativa")]
    ESTADOS_PUBLICACION = [("draft", "Borrador"), ("published", "Publicado"), ("archived", "Archivado")]
    ESTADOS_VERIFICACION = [("pending", "Pendiente"), ("verified", "Verificado"), ("rejected", "Rechazado")]
    ESTADOS_RECLAMACION = [("unclaimed", "No reclamado"), ("claimed", "Reclamado"), ("under_review", "En revisión")]


        ##############   Header de empresa #############
    propietario_sitio_web = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Propietario", null=True, blank=True)
    
    nombre_de_la_empresa = models.CharField(max_length=100, verbose_name="Nombre de la Empresa")
    tipo_empresa = models.ForeignKey(TipoEmpresa,on_delete=models.CASCADE,related_name="empresas",verbose_name="Elija el tipo de Empresa",null=True, blank=True)
    nombreUrl = models.SlugField(max_length=150, unique=True, null=True, blank=True,verbose_name="Elija el nombre de la URl sin espacios")
    identificador_externo = models.CharField(max_length=50, unique=True, null=True, blank=True, db_index=True, verbose_name="Identificador externo")
    tipo_perfil = models.CharField(max_length=20, choices=TIPOS_PERFIL, default="business", db_index=True, verbose_name="Tipo de perfil")
    estado_publicacion = models.CharField(max_length=20, choices=ESTADOS_PUBLICACION, default="draft", db_index=True, verbose_name="Estado de publicación")
    descripcion_directorio = models.TextField(blank=True, verbose_name="Descripción del directorio")
    region = models.CharField(max_length=100, blank=True, verbose_name="Comunidad autónoma o región")
    provincia = models.CharField(max_length=100, blank=True, verbose_name="Provincia")
    codigo_postal = models.CharField(max_length=20, blank=True, verbose_name="Código postal")
    sitio_web = models.URLField(max_length=500, blank=True, verbose_name="Página web")
    relacion_nicaragua = models.TextField(blank=True, verbose_name="Relación con Nicaragua")
    estado_verificacion = models.CharField(max_length=20, choices=ESTADOS_VERIFICACION, default="pending", db_index=True, verbose_name="Estado de verificación")
    estado_reclamacion = models.CharField(max_length=20, choices=ESTADOS_RECLAMACION, default="unclaimed", db_index=True, verbose_name="Estado de reclamación")
    fecha_incorporacion = models.DateTimeField(default=timezone.now, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    #Header titulo en la página como texto principal h1
    header_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de Cabecera", default=True)
    titulo_header = models.CharField(max_length=100, verbose_name="titulo header", null=True, blank=True)
    #header subtitulo subtitulo numero uno
    subtitulo1_header = models.CharField(max_length=100, verbose_name="subtitulo 1 header", null=True, blank=True)
    #header subtitulo subtitulo numero dos 
    subtitulo2_header = models.CharField(max_length=100, verbose_name="subtitulo 2 header", null=True, blank=True)
    #esta es la foto del logo de el header
    imagen_logo_empresa = models.ImageField(upload_to='empresas/imagenes/logos/header', null=True, blank=True)
    #imagen para el header a la par del subtitulo de presentacion
    imagen_fondo_header = models.ImageField(upload_to='empresas/imagenes/header', null=True, blank=True)
    #imagen para el header 
    imagen_header = models.ImageField(upload_to='empresas/imagenes/header', null=True, blank=True)
    #video de portada en el header solo se acepta enlace por el momento
    video_header = models.CharField(max_length=500, verbose_name="video_header", null=True, blank=True)


        ##############  Sobre Nosotro ################
        ##############################################


    #activar el aparatado de quienes somos, para poder agregarlo o que no aparezca
    quienes_somos_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección Sobre Nosotros", default=True)
    #titulo para describir sobre nosotros quienes somos como empresas
    titulo_sobrenosotros = models.CharField(max_length=500, verbose_name="parrafo para describir sobrenosotros 1", null=True, blank=True)
    #titulo sobre nosotros para descripcion
    parrafo1_sobrenosotros = models.CharField(max_length=500, verbose_name="parrafo para describir sobrenosotros 1", null=True, blank=True)
    #titulo sobre nosotros para descripcion
    parrafo2_sobrenosotros = models.CharField(max_length=500, verbose_name="parrafo para describir sobrenosotros 2", null=True, blank=True)
    #titulo sobre nosotros para descripcion
    parrafo3_sobrenosotros = models.CharField(max_length=500, verbose_name="parrafo para describir sobrenosotros 3", null=True, blank=True)
    #titulo sobre nosotros para descripcion
    parrafo4_sobrenosotros = models.CharField(max_length=500, verbose_name="parrafo para describir sobrenosotros 4", null=True, blank=True)
    #titulo sobre nosotros para descripcion
    parrafo5_sobrenosotros = models.CharField(max_length=500, verbose_name="parrafo para describir sobrenosotros 5", null=True, blank=True)
    #imagen para el apartado sobre nosotros  imagen mas grande
    imagen1_nosotros = models.ImageField(upload_to='empresas/imagenes/nosotros', null=True, blank=True)
    #imagen para el apartado sobre nosotros imagen de fondo del video pequeño
    imagen2_nosotros_fondo = models.ImageField(upload_to='empresas/imagenes/nosotros', null=True, blank=True)
    #imagen para el apartado sobre nosotros imagen 
    imagen3_nosotros = models.ImageField(upload_to='empresas/imagenes/nosotros', null=True, blank=True)
    #video de portada en el header solo se acepta enlace por el momento
    video_nosotros = models.CharField(max_length=500, verbose_name="video_nosotros", null=True, blank=True)



        ##############  Sobre el menú ################
        ##############################################


    #activar el aparatado de vender menu de regalo, para poder agregarlo o que no aparezca
    menu_regalo_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección para vender menu de regalo", default=True)

    #esto es el campo para incluir lo que ofrece el menu para una persona en el apartado de menu de regalo numero 1
    #menu_regalo1 = models.CharField(max_length=500, verbose_name="menu_regalo1", null=True, blank=True)

    #esto es el campo para incluir lo que ofrece el menu para una persona en el apartado de menu de regalo numero 1
    menu_oferta1 = HTMLField(blank=True,null=True)
    menu_oferta2= HTMLField(blank=True,null=True)
    menu_oferta3 = HTMLField(blank=True,null=True)

    #activar el aparatado de la galería, para poder agregarlo o que no aparezca
    clientes_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección para ver clientes", default=True)

    #activar el aparatado de la galería, para poder agregarlo o que no aparezca
    platos_menu_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de platos", default=True)


    #apartado para la seccion de la exposixcino de platos , su descripciony su precio
    nombre1_plato_menu = models.CharField(max_length=255, verbose_name="Nombre Plato 1", blank=True, null=True)
    nombre2_plato_menu = models.CharField(max_length=255, verbose_name="Nombre Plato 2", blank=True, null=True)
    nombre3_plato_menu = models.CharField(max_length=255, verbose_name="Nombre Plato 3", blank=True, null=True)
    nombre4_plato_menu = models.CharField(max_length=255, verbose_name="Nombre Plato 4", blank=True, null=True)
    nombre5_plato_menu = models.CharField(max_length=255, verbose_name="Nombre Plato 5", blank=True, null=True)
    nombre6_plato_menu = models.CharField(max_length=255, verbose_name="Nombre Plato 6", blank=True, null=True)
    nombre7_plato_menu = models.CharField(max_length=255, verbose_name="Nombre Plato 7", blank=True, null=True)
    nombre8_plato_menu = models.CharField(max_length=255, verbose_name="Nombre Plato 8", blank=True, null=True)
    nombre9_plato_menu = models.CharField(max_length=255, verbose_name="Nombre Plato 9", blank=True, null=True)
    nombre10_plato_menu = models.CharField(max_length=255, verbose_name="Nombre Plato 10", blank=True, null=True)

    # Imágenes de los platos
    imagen1_plato_menu = models.ImageField(upload_to="empresas/imagenes/platos/", verbose_name="Imagen Plato 1", blank=True, null=True)
    imagen2_plato_menu = models.ImageField(upload_to="empresas/imagenes/platos/", verbose_name="Imagen Plato 2", blank=True, null=True)
    imagen3_plato_menu = models.ImageField(upload_to="empresas/imagenes/platos/", verbose_name="Imagen Plato 3", blank=True, null=True)
    imagen4_plato_menu = models.ImageField(upload_to="empresas/imagenes/platos/", verbose_name="Imagen Plato 4", blank=True, null=True)
    imagen5_plato_menu = models.ImageField(upload_to="empresas/imagenes/platos/", verbose_name="Imagen Plato 5", blank=True, null=True)
    imagen6_plato_menu = models.ImageField(upload_to="empresas/imagenes/platos/", verbose_name="Imagen Plato 6", blank=True, null=True)
    imagen7_plato_menu = models.ImageField(upload_to="empresas/imagenes/platos/", verbose_name="Imagen Plato 7", blank=True, null=True)
    imagen8_plato_menu = models.ImageField(upload_to="empresas/imagenes/platos/", verbose_name="Imagen Plato 8", blank=True, null=True)
    imagen9_plato_menu = models.ImageField(upload_to="empresas/imagenes/platos/", verbose_name="Imagen Plato 9", blank=True, null=True)
    imagen10_plato_menu = models.ImageField(upload_to="empresas/imagenes/platos/", verbose_name="Imagen Plato 10", blank=True, null=True)

    # Descripciones de los platos
    descriptcion1_plato_menu = models.TextField(verbose_name="Descripción Plato 1", blank=True, null=True)
    descriptcion2_plato_menu = models.TextField(verbose_name="Descripción Plato 2", blank=True, null=True)
    descriptcion3_plato_menu = models.TextField(verbose_name="Descripción Plato 3", blank=True, null=True)
    descriptcion4_plato_menu = models.TextField(verbose_name="Descripción Plato 4", blank=True, null=True)
    descriptcion5_plato_menu = models.TextField(verbose_name="Descripción Plato 5", blank=True, null=True)
    descriptcion6_plato_menu = models.TextField(verbose_name="Descripción Plato 6", blank=True, null=True)
    descriptcion7_plato_menu = models.TextField(verbose_name="Descripción Plato 7", blank=True, null=True)
    descriptcion8_plato_menu = models.TextField(verbose_name="Descripción Plato 8", blank=True, null=True)
    descriptcion9_plato_menu = models.TextField(verbose_name="Descripción Plato 9", blank=True, null=True)
    descriptcion10_plato_menu = models.TextField(verbose_name="Descripción Plato 10", blank=True, null=True)

    # Precios de los platos
    precio1_plato_menu = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Plato 1", blank=True, null=True)
    precio2_plato_menu = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Plato 2", blank=True, null=True)
    precio3_plato_menu = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Plato 3", blank=True, null=True)
    precio4_plato_menu = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Plato 4", blank=True, null=True)
    precio5_plato_menu = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Plato 5", blank=True, null=True)
    precio6_plato_menu = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Plato 6", blank=True, null=True)
    precio7_plato_menu = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Plato 7", blank=True, null=True)
    precio8_plato_menu = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Plato 8", blank=True, null=True)
    precio9_plato_menu = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Plato 9", blank=True, null=True)
    precio10_plato_menu = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Plato 10", blank=True, null=True)


        ##############  Sobre los Comentarios ################
        ######################################################


    #activar el aparatado de la galería, para poder agregarlo o que no aparezca
    comentarios_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de comentarios", default=True)
    
    #parrafo para el apartado de los comentarios
    parrafo1_comentario = models.CharField(max_length=500, verbose_name="parrafo comentario 1", null=True, blank=True)
    parrafo2_comentario = models.CharField(max_length=500, verbose_name="parrafo comentario 2", null=True, blank=True)
    parrafo3_comentario = models.CharField(max_length=500, verbose_name="parrafo comentario 3", null=True, blank=True)

    #nombre de la paersona que comenta en el apartado de testimosnios o comentarios
    nombre1_comentario = models.CharField(max_length=100, verbose_name="Nombre de la persona que hace el comentario 1", null=True, blank=True)
    nombre2_comentario = models.CharField(max_length=100, verbose_name="Nombre de la persona que hace el comentario 2", null=True, blank=True)
    nombre3_comentario = models.CharField(max_length=100, verbose_name="Nombre de la persona que hace el comentario 3", null=True, blank=True)

    #imagen para el apartado de los comentarios 1
    imagen1_comentario = models.ImageField(upload_to='empresas/imagenes/comentarios', null=True, blank=True)
    imagen2_comentario = models.ImageField(upload_to='empresas/imagenes/comentarios', null=True, blank=True)
    imagen3_comentario = models.ImageField(upload_to='empresas/imagenes/comentarios', null=True, blank=True)
    
     #activar el aparatado de la galería, para poder agregarlo o que no aparezca
    eventos_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de enventos", default=True)

    chefs_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de chefs", default=True)

    imagen_chef1 = models.ImageField(upload_to='empresas/imagenes/chefs/', verbose_name="Agregar imagen Chef 1", blank=True, null=True)
    imagen_chef2 = models.ImageField(upload_to='empresas/imagenes/chefs/', verbose_name="Agregar imagen Chef 2", blank=True, null=True)
    imagen_chef3 = models.ImageField(upload_to='empresas/imagenes/chefs/', verbose_name="Agregar imagen Chef 3", blank=True, null=True)
    
    nombre_chef1 = models.CharField(max_length=255, verbose_name="Introduzca el nombre del Chef 1", blank=True, null=True)
    nombre_chef2 = models.CharField(max_length=255, verbose_name="Introduzca el nombre del Chef 2", blank=True, null=True)
    nombre_chef3 = models.CharField(max_length=255, verbose_name="Introduzca el nombre del Chef 3", blank=True, null=True)

    reservar_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección para reservas", default=True)


        ##############  Sobre los Servicios ################
        ######################################################


    #titulo para describir sobre los servicios
    servicios_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de servicios", default=True)
    titulo_servicios = models.CharField(max_length=500, verbose_name="titulo servicios", null=True, blank=True)

    #imagen para el apartado de los servicios numero 1
    imagen_servicio1 = models.ImageField(upload_to='empresas/imagenes/servicios', null=True, blank=True)
    imagen_servicio2 = models.ImageField(upload_to='empresas/imagenes/servicios', null=True, blank=True)
    imagen_servicio3 = models.ImageField(upload_to='empresas/imagenes/servicios', null=True, blank=True)
    imagen_servicio4 = models.ImageField(upload_to='empresas/imagenes/servicios', null=True, blank=True)

    #nombre para describir sobre los servicios 1
    nombre_servicio1 = models.CharField(max_length=500, verbose_name="desacribir parrafo servicio 1", null=True, blank=True)
    nombre_servicio2 = models.CharField(max_length=500, verbose_name="desacribir parrafo servicio 2", null=True, blank=True)
    nombre_servicio3 = models.CharField(max_length=500, verbose_name="desacribir parrafo servicio 3", null=True, blank=True)
    nombre_servicio4 = models.CharField(max_length=500, verbose_name="desacribir parrafo servicio 4", null=True, blank=True)

    #titulo sobre nosotros para descripcion e servicios 1
    parrafo_servicios1 = models.CharField(max_length=500, verbose_name="describir el parrafo servicio 1", null=True, blank=True)
    parrafo_servicios2 = models.CharField(max_length=500, verbose_name="describir el parrafo servicio 2", null=True, blank=True)
    parrafo_servicios3 = models.CharField(max_length=500, verbose_name="describir el parrafo servicio 3", null=True, blank=True)
    parrafo_servicios4 = models.CharField(max_length=500, verbose_name="describir el parrafo servicio 4", null=True, blank=True)


        ##############  Sobre el equipo de trabajo ################
        ###############################################################


     #titulo para describir sobre los servicios
    trabajadores_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de trabajadores", default=True)
    titulo_trabajadores = models.CharField(max_length=500, verbose_name="parrafo1", null=True, blank=True)

    #imagen para el apartado de de equipo de trabajo numero 1
    imagen_trabajador1 = models.ImageField(upload_to='empresas/imagenes/trabajadores', null=True, blank=True)
    imagen_trabajador2 = models.ImageField(upload_to='empresas/imagenes/trabajadores', null=True, blank=True)
    imagen_trabajador3 = models.ImageField(upload_to='empresas/imagenes/trabajadores', null=True, blank=True)

    #nombre para describir sobre el equipo de trabajo numero 1
    nombre_trabajador1 = models.CharField(max_length=500, verbose_name="trabajador 1", null=True, blank=True)
    nombre_trabajador2 = models.CharField(max_length=500, verbose_name="trabajador 2", null=True, blank=True)
    nombre_trabajador3 = models.CharField(max_length=500, verbose_name="trabajador 3", null=True, blank=True)



        ##############  Sobre el precio y las ofertas de prductos ################
        ##########################################################################

    #titulo para describir las tarifas
    tarifa_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de tarifas/catálogo", default=True)
    titulo_tarifa = models.CharField(max_length=500, verbose_name="Titulo sccion de tarifa", null=True, blank=True)

    #imagen para el apartado de las tarifas numero 1
    imagen_tarifa1 = models.ImageField(upload_to='empresas/imagenes/servicios', null=True, blank=True)
    imagen_tarifa2 = models.ImageField(upload_to='empresas/imagenes/servicios', null=True, blank=True)

    #producto servicio y su tarifa 1
    nombre_servicio1_tarifa = models.CharField(max_length=500, verbose_name="Titulo tarifa 1", null=True, blank=True)
    nombre_servicio2_tarifa = models.CharField(max_length=500, verbose_name="Titulo tarifa 2", null=True, blank=True)
    nombre_servicio3_tarifa = models.CharField(max_length=500, verbose_name="Titulo tarifa 3", null=True, blank=True)
    nombre_servicio4_tarifa = models.CharField(max_length=500, verbose_name="Titulo tarifa 4", null=True, blank=True)
    nombre_servicio5_tarifa = models.CharField(max_length=500, verbose_name="Titulo tarifa 5", null=True, blank=True)
    nombre_servicio6_tarifa = models.CharField(max_length=500, verbose_name="Titulo tarifa 6", null=True, blank=True)
    nombre_servicio7_tarifa = models.CharField(max_length=500, verbose_name="Titulo tarifa 7", null=True, blank=True)
    nombre_servicio8_tarifa = models.CharField(max_length=500, verbose_name="Titulo tarifa 8", null=True, blank=True)
    nombre_servicio9_tarifa = models.CharField(max_length=500, verbose_name="Titulo tarifa 9", null=True, blank=True)
    nombre_servicio10_tarifa = models.CharField(max_length=500, verbose_name="Titulo tarifa 10", null=True, blank=True)
    
    #tarifa del precio 1
    precio_servicio1_tarifa = models.CharField(max_length=500, verbose_name="precio tarifa 1", null=True, blank=True)
    precio_servicio2_tarifa = models.CharField(max_length=500, verbose_name="precio tarifa 2", null=True, blank=True)
    precio_servicio3_tarifa = models.CharField(max_length=500, verbose_name="precio tarifa 3", null=True, blank=True)
    precio_servicio4_tarifa = models.CharField(max_length=500, verbose_name="precio tarifa 4", null=True, blank=True)
    precio_servicio5_tarifa = models.CharField(max_length=500, verbose_name="precio tarifa 5", null=True, blank=True)
    precio_servicio6_tarifa = models.CharField(max_length=500, verbose_name="precio tarifa 6", null=True, blank=True)
    precio_servicio7_tarifa = models.CharField(max_length=500, verbose_name="precio tarifa 7", null=True, blank=True)
    precio_servicio8_tarifa = models.CharField(max_length=500, verbose_name="precio tarifa 8", null=True, blank=True)
    precio_servicio9_tarifa = models.CharField(max_length=500, verbose_name="precio tarifa 9", null=True, blank=True)
    precio_servicio10_tarifa = models.CharField(max_length=500, verbose_name="precio tarifa 10", null=True, blank=True)


        ##############  Sobre la Galeria de la Empresa ################
        ###############################################################


    # Activar el apartado de la galería para agregarlo o que no aparezca
    galeria_activo = models.BooleanField(blank=True, verbose_name="Agregar sección Galería", default=True)

    # Título para el apartado de galería
    titulo1_galeria = models.CharField(max_length=500, verbose_name="Título de la galería", null=True, blank=True)

    # Imágenes para el apartado de la galería
    imagen1_galeria = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True, verbose_name="Imagen 1 de la galería")
    imagen2_galeria = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True, verbose_name="Imagen 2 de la galería")
    imagen3_galeria = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True, verbose_name="Imagen 3 de la galería")
    imagen4_galeria = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True, verbose_name="Imagen 4 de la galería")
    imagen5_galeria = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True, verbose_name="Imagen 5 de la galería")
    imagen6_galeria = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True, verbose_name="Imagen 6 de la galería")
    imagen7_galeria = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True, verbose_name="Imagen 7 de la galería")
    imagen8_galeria = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True, verbose_name="Imagen 8 de la galería")
    imagen9_galeria = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True, verbose_name="Imagen 9 de la galería")
    imagen10_galeria = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True, verbose_name="Imagen 10 de la galería")
    imagen11_galeria = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True, verbose_name="Imagen 11 de la galería")

        ##############  Espacio para Contactar ################
        #######################################################

    imagen_portada_reserva = models.ImageField(upload_to='reservas/',verbose_name="Imagen Portada Reserva",blank=True,null=True)

    #activar el aparatado de la galería, para poder agregarlo o que no aparezca
    contactar_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección para contactar", default=True)

    #horario para el apartado de contactar
    horario = models.CharField(max_length=500, verbose_name="horario", null=True, blank=True)
    pais = models.CharField(max_length=100, verbose_name="Pais de la Empresa",null=True, blank=True)
    ciudad = models.CharField(max_length=100, verbose_name="Nombre de la Ciudad",null=True, blank=True)
    imagen = models.ImageField(upload_to='empresas/imagenes/principal', null=True, blank=True)
    imagen_portada = models.ImageField(upload_to='empresas/imagenes/portada', null=True, blank=True)
    direccion = models.TextField(verbose_name="Direccion", null=True, blank=True)
    telefono = models.CharField(max_length=100, verbose_name="Numero de telefono", null=True, blank=True)
    email = models.EmailField(verbose_name="Correo electronico", null=True, blank=True)
    latitud = models.CharField(max_length=100,  verbose_name="Latitud", null=True, blank=True)
    longitud = models.CharField(max_length=100,  verbose_name="Longitud", null=True, blank=True)
  

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ["nombre_de_la_empresa", "titulo_header"]

    def __str__(self):
        return f"{self.nombre_de_la_empresa} - {self.titulo_header}, - {self.subtitulo2_header}"


    def esta_publicado(self):
        return self.estado_publicacion == "published"

    def coordenadas_validas(self):
        try:
            latitud = float((self.latitud or "").replace(",", "."))
            longitud = float((self.longitud or "").replace(",", "."))
        except (TypeError, ValueError):
            return False
        return -90 <= latitud <= 90 and -180 <= longitud <= 180

    def direccion_es_publica(self):
        try:
            return self.importacion_perfil.tipo_direccion == "business_or_public"
        except ImportacionPerfil.DoesNotExist:
            return True


class ImportacionPerfil(models.Model):
    TIPOS_DIRECCION = [("business_or_public", "Negocio o dirección pública"), ("institutional_contact", "Contacto institucional"), ("registry_not_for_visit", "Registral, no visitable"), ("not_provided", "No informada")]
    PRECISIONES = [("address_unverified", "Dirección sin verificar"), ("municipality_only", "Solo municipio"), ("unknown", "Desconocida")]
    RESULTADOS = [("valid", "Válido"), ("warnings", "Con advertencias"), ("error", "Error")]

    empresa = models.OneToOneField(Empresa, on_delete=models.CASCADE, related_name="importacion_perfil", null=True, blank=True)
    identificador_externo = models.CharField(max_length=50, unique=True)
    fuente_informacion = models.CharField(max_length=100, default="mundonica_perfiles.csv")
    url_origen = models.URLField(max_length=500, blank=True)
    hoja_origen = models.CharField(max_length=100, blank=True)
    notas_internas = models.TextField(blank=True)
    canal_contacto = models.CharField(max_length=50, blank=True)
    disponibilidad_contacto = models.CharField(max_length=50, blank=True)
    tipo_direccion = models.CharField(max_length=30, choices=TIPOS_DIRECCION, blank=True)
    precision_localizacion = models.CharField(max_length=30, choices=PRECISIONES, blank=True)
    verificacion_original = models.CharField(max_length=255, blank=True)
    hash_fila = models.CharField(max_length=64, blank=True, db_index=True)
    primera_importacion = models.DateTimeField(auto_now_add=True)
    ultima_importacion = models.DateTimeField(auto_now=True)
    resultado_validacion = models.CharField(max_length=20, choices=RESULTADOS, default="valid")
    datos_ultima_importacion = models.JSONField(default=dict, blank=True)
    campos_en_conflicto = models.JSONField(default=dict, blank=True)
    errores_validacion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Importación de perfil"
        verbose_name_plural = "Importaciones de perfiles"
        ordering = ["identificador_externo"]

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.empresa_id and self.empresa.identificador_externo != self.identificador_externo:
            raise ValidationError({"identificador_externo": "Debe coincidir con el identificador externo de la empresa."})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        nombre = self.empresa.nombre_de_la_empresa if self.empresa_id else "fila rechazada"
        return f"{self.identificador_externo} — {nombre}"

######################## este es el modelo de tipo de empresa de Catalogo ###################################
###############################################################################################################


class Abogado(models.Model):
    # Campos existentes
    nombre = models.CharField(max_length=100, verbose_name="Nombre del abogado")
    apellido = models.CharField(max_length=100, verbose_name="Apellido del abogado")
    imagen = models.ImageField(upload_to='images/abogados', null=True, blank=True)
    pais = models.CharField(max_length=100, verbose_name="País del abogado")
    ciudad = models.CharField(max_length=100, verbose_name="Nombre de la ciudad")
    direccion = models.TextField(verbose_name="Dirección", null=True, blank=True)
    precio = models.CharField(max_length=100, verbose_name="Precio", null=True, blank=True)
    titulo = models.CharField(max_length=100, verbose_name="Título", null=True, blank=True)
    telefono = models.CharField(max_length=100, verbose_name="Número de teléfono", null=True, blank=True)
    email = models.EmailField(verbose_name="Correo electrónico", null=True, blank=True)
    latitud = models.CharField(max_length=100, verbose_name="Latitud", null=True, blank=True)
    longitud = models.CharField(max_length=100, verbose_name="Longitud", null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    resumen = models.TextField(blank=True, null=True, verbose_name="Resumen")
    verificado = models.BooleanField(blank=True, null=True, default=False, verbose_name="¿Está verificado?")

    # Servicios Legales Generales
    asesoriajuridicageneral = models.BooleanField(blank=True, null=True, verbose_name="Asesoría Jurídica General")
    redaccionyrevisiondedocumentos = models.BooleanField(blank=True, null=True, verbose_name="Redacción y Revisión de Documentos")
    representacionlegal = models.BooleanField(blank=True, null=True, verbose_name="Representación Legal")
    mediacionyarbitraje = models.BooleanField(blank=True, null=True, verbose_name="Mediación y Arbitraje")

    # Derecho Migratorio
    tramitesdevisasypermisosdetrabajo = models.BooleanField(blank=True, null=True, verbose_name="Trámites de Visas y Permisos de Trabajo")
    procesosdenaturalizacion = models.BooleanField(blank=True, null=True, verbose_name="Procesos de Naturalización")
    defensaencasosdedeportacion = models.BooleanField(blank=True, null=True, verbose_name="Defensa en Casos de Deportación")
    asesoriaenreagrupacionfamiliar = models.BooleanField(blank=True, null=True, verbose_name="Asesoría en Reagrupación Familiar")

    # Derecho Civil y Familiar
    asesoriaencasosdedivorcioyseparacion = models.BooleanField(blank=True, null=True, verbose_name="Asesoría en Casos de Divorcio y Separación")
    tramitesdepartidadenacimientoydefunciones = models.BooleanField(blank=True, null=True, verbose_name="Trámites de Partida de Nacimiento y Defunciones")
    asesoriaenherenciasytestamentos = models.BooleanField(blank=True, null=True, verbose_name="Asesoría en Herencias y Testamentos")

    # Derecho Laboral
    negocioacionyredacciondecontratos = models.BooleanField(blank=True, null=True, verbose_name="Negociación y Redacción de Contratos")
    asistenciaencasosdedespidos = models.BooleanField(blank=True, null=True, verbose_name="Asistencia en Casos de Despidos")

    # Derecho Mercantil
    asesoramientoparaemprendedores = models.BooleanField(blank=True, null=True, verbose_name="Asesoramiento para Emprendedores")
    propiedadintelectual = models.BooleanField(blank=True, null=True, verbose_name="Propiedad Intelectual")
    asesoriaparaexportaciondeproductos = models.BooleanField(blank=True, null=True, verbose_name="Asesoría para Exportación de Productos")

    # Derecho Penal
    defenzaencasospenales = models.BooleanField(blank=True, null=True, verbose_name="Defensa en Casos Penales")
    asesoriaencasosdeviolenciaoabusos = models.BooleanField(blank=True, null=True, verbose_name="Asesoría en Casos de Violencia o Abusos")

    # Servicios Adicionales
    traduccionylegalizaciondedocumentos = models.BooleanField(blank=True, null=True, verbose_name="Traducción y Legalización de Documentos")
    capacitacionesytalleresjuridicos = models.BooleanField(blank=True, null=True, verbose_name="Capacitaciones y Talleres Jurídicos")



    class Meta:
        verbose_name = "Abogado"
        verbose_name_plural = "Abogados"
        ordering = ["pais", "ciudad"]


    def __str__(self):
        return f"{self.nombre} - {self.ciudad}, - {self.pais}"




class Blog(models.Model):
    """Modelo para entradas de blog."""

    fecha_hora = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    titulo = models.CharField(max_length=255,blank=True,null=True)
    categoria = models.CharField(max_length=255,blank=True,null=True)
    imagen = models.ImageField(upload_to='images/blog', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = HTMLField()
    resumen = HTMLField( blank=True,null=True)



    def __str__(self):
        """Devuelve el título del post como representación en cadena."""
        return self.titulo

    def get_summary(self):
        """Devuelve un resumen del cuerpo del post (primeras 200 palabras)."""
        return self.cuerpo[:200]





class Post(models.Model):
    """Modelo para entradas de blog."""
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    comentario = models.TextField(max_length=5000,blank=True,null=True)
    imagen = models.ImageField(upload_to='red_social/post/imagen', null=True, blank=True)
    likes = models.IntegerField(blank=True,null=True)
    video = models.FileField(upload_to='red_social/post/videos', null=True, blank=True)  # Para videos


    def __str__(self):
        """Devuelve el título del post como representación en cadena."""
        return self.comentario

    def get_summary(self):
        """Devuelve un resumen del cuerpo del post (primeras 200 palabras)."""
        return self.comentario[:200]



class Perfil(models.Model):
    # Relación uno a uno con la tabla User de Django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')

    # Campos adicionales para extender la funcionalidad
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='usuario/avatars', blank=True, null=True)
    
    def __str__(self):
        return f"Perfil de {self.usuario}"

# Crear un perfil automáticamente cuando se crea un usuario
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

# Guardar el perfil automáticamente cuando el usuario se guarda
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()



class Receta(models.Model):
    CATEGORIAS = [
        ('entradas', 'Entradas'),
        ('platos_principales', 'Platos Principales'),
        ('postres', 'Postres'),
        ('bebidas', 'Bebidas'),
        ('otros', 'Otros'),
    ]

    titulo = models.CharField(max_length=255)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='otros')  # 🔹 Convertido a desplegable
    imagen = models.ImageField(upload_to='recetas/', null=True, blank=True)
    resumen = models.TextField()
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(default=timezone.now, null=False)  # ✅ Fecha automática al crear

    def __str__(self):
        return self.titulo


class Favorito(models.Model):
    """Negocio (Empresa) que un usuario guardó en "Me gusta" (tipo TripAdvisor)."""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='favoritos')
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"
        unique_together = ('usuario', 'empresa')
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.usuario} ❤ {self.empresa}"


class Valoracion(models.Model):
    """Valoración de 1 a 5 estrellas de un usuario sobre un negocio (tipo TripAdvisor)."""
    PUNTUACIONES = [(i, i) for i in range(1, 6)]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='valoraciones')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='valoraciones')
    puntuacion = models.PositiveSmallIntegerField(choices=PUNTUACIONES, verbose_name="Puntuación (1-5)")
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Valoración"
        verbose_name_plural = "Valoraciones"
        unique_together = ('usuario', 'empresa')
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.usuario} valoró {self.empresa} con {self.puntuacion}★"


class HistoriaPropuesta(models.Model):
    ESTADOS = [
        ('nueva', 'Nueva'),
        ('contactada', 'Contactada'),
        ('conversacion', 'En conversación'),
        ('cerrada', 'Cerrada'),
    ]

    PREFERENCIAS_GRABACION = [
        ('laborable_manana', 'Lunes a viernes por la mañana'),
        ('laborable_tarde', 'Lunes a viernes por la tarde'),
        ('sabado_manana', 'Sábado por la mañana'),
        ('sabado_tarde', 'Sábado por la tarde'),
        ('domingo_manana', 'Domingo por la mañana'),
        ('domingo_tarde', 'Domingo por la tarde'),
        ('flexible', 'Tengo flexibilidad de fecha y hora'),
    ]

    LUGARES_GRABACION = [
        ('ubicacion_propia', 'En mi restaurante, bar, empresa u hogar'),
        ('estudio_mundonica', 'En el estudio de Mundónica, en Oiartzun (Gipuzkoa, España)'),
    ]

    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    ciudad_pais = models.CharField(max_length=150, verbose_name='Ciudad y país')
    email = models.EmailField(verbose_name='Correo electrónico')
    telefono = models.CharField(max_length=40, blank=True, verbose_name='Teléfono o WhatsApp')
    historia = models.TextField(max_length=2500, verbose_name='Historia')
    preferencia_contacto = models.CharField(
        max_length=20,
        choices=(
            ('email', 'Correo electrónico'),
            ('telefono', 'Teléfono o WhatsApp'),
            ('indiferente', 'Me es indiferente'),
        ),
        default='email',
        verbose_name='Preferencia de contacto',
    )
    preferencia_grabacion = models.CharField(
        max_length=20,
        choices=PREFERENCIAS_GRABACION,
        blank=True,
        default='',
        verbose_name='Preferencia para grabar el podcast o la entrevista',
    )
    lugar_grabacion = models.CharField(
        max_length=20,
        choices=LUGARES_GRABACION,
        blank=True,
        default='',
        verbose_name='¿Dónde prefieres que grabemos el podcast o la entrevista?',
    )
    estado = models.CharField(max_length=20, choices=ESTADOS, default='nueva', verbose_name='Estado')
    recibida_en = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de recepción')
    actualizada_en = models.DateTimeField(auto_now=True, verbose_name='Última actualización')

    class Meta:
        ordering = ['-recibida_en']
        verbose_name = 'Propuesta de historia'
        verbose_name_plural = 'Propuestas de historias'

    def __str__(self):
        return f'{self.nombre} - {self.ciudad_pais}'


class HistoriaConfiguracion(models.Model):
    video_youtube_id = models.CharField(
        max_length=200,
        default='3dJC1Z9Sl78',
        verbose_name='ID o URL del vídeo de YouTube',
        help_text='Pega una URL de YouTube o su ID. Se guardará únicamente el ID validado.',
    )

    class Meta:
        verbose_name = 'Configuración de Historias'
        verbose_name_plural = 'Configuración de Historias'

    def clean(self):
        self.video_youtube_id = normalizar_youtube_id(self.video_youtube_id)

    def save(self, *args, **kwargs):
        self.video_youtube_id = normalizar_youtube_id(self.video_youtube_id)
        self.pk = 1
        return super().save(*args, **kwargs)

    def __str__(self):
        return 'Vídeo de presentación de Historias'


class SeccionMenu(models.Model):
    """Controla qué enlaces del menú principal (header) se muestran en el sitio.

    Se administra desde el admin de Django: desactivar una sección aquí la oculta
    del menú en todas las páginas, sin tocar código. La "clave" identifica de forma
    estable a qué enlace del menú corresponde (ver base.html).
    """

    CLAVES = [
        ('inicio', 'Inicio'),
        ('historias', 'Historias'),
        ('blog', 'Blog'),
        ('mapa', 'Mapa'),
        ('galeria', 'Galería'),
        ('recetas', 'Recetas'),
        ('servicios', 'Servicios (Preguntas y Moneda)'),
        ('donativos', 'Donativos'),
        ('empresas', 'Empresas (Explorar negocios)'),
        ('extranjeros', 'Extranjeros (Consulados, Embajadas, Abogados)'),
        ('contacto', 'Contacto'),
    ]

    clave = models.CharField(max_length=50, choices=CLAVES, unique=True, verbose_name="Enlace del menú")
    nombre = models.CharField(max_length=100, verbose_name="Nombre visible en el menú")
    activo = models.BooleanField(default=True, verbose_name="Mostrar en el menú")
    orden = models.PositiveIntegerField(default=0, verbose_name="Orden")

    class Meta:
        verbose_name = "Sección del menú"
        verbose_name_plural = "Secciones del menú"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return f"{self.nombre} ({'visible' if self.activo else 'oculto'})"