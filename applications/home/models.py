from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

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
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Tipo de Empresa")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    class Meta:
        verbose_name = "Tipo de Empresa"
        verbose_name_plural = "Tipos de Empresa"

    def __str__(self):
        return self.nombre





    ################# modelo de empresa unificar los modelos  ##################
    ############################################################################


class Empresa(models.Model):

        ##############   Header de empresa #############
    propietario_sitio_web = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Propietario", null=True, blank=True)
    
    nombre_de_la_empresa = models.CharField(max_length=100, verbose_name="Nombre de la Empresa")
    tipo_empresa = models.ForeignKey(TipoEmpresa,on_delete=models.CASCADE,related_name="empresas",verbose_name="Elija el tipo de Empresa",null=True, blank=True,default=1)
    nombreUrl = models.SlugField(max_length=150, unique=True, null=True, blank=True,verbose_name="Elija el nombre de la URl sin espacios")
    #Header titulo en la página como texto principal h1
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
    quienes_somos_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección Sobre Nosotros")
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
    menu_regalo_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección para vender menu de regalo")

    #esto es el campo para incluir lo que ofrece el menu para una persona en el apartado de menu de regalo numero 1
    #menu_regalo1 = models.CharField(max_length=500, verbose_name="menu_regalo1", null=True, blank=True)

    #esto es el campo para incluir lo que ofrece el menu para una persona en el apartado de menu de regalo numero 1
    menu_oferta1 = HTMLField(blank=True,null=True)
    menu_oferta2= HTMLField(blank=True,null=True)
    menu_oferta3 = HTMLField(blank=True,null=True)

    #activar el aparatado de la galería, para poder agregarlo o que no aparezca
    clientes_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección para ver clientes")

    #activar el aparatado de la galería, para poder agregarlo o que no aparezca
    platos_menu_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de platos")


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
    comentarios_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de comentarios")
    
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
    eventos_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de enventos")

    chefs_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de chefs")

    imagen_chef1 = models.ImageField(upload_to='empresas/imagenes/chefs/', verbose_name="Agregar imagen Chef 1", blank=True, null=True)
    imagen_chef2 = models.ImageField(upload_to='empresas/imagenes/chefs/', verbose_name="Agregar imagen Chef 2", blank=True, null=True)
    imagen_chef3 = models.ImageField(upload_to='empresas/imagenes/chefs/', verbose_name="Agregar imagen Chef 3", blank=True, null=True)
    
    nombre_chef1 = models.CharField(max_length=255, verbose_name="Introduzca el nombre del Chef 1", blank=True, null=True)
    nombre_chef2 = models.CharField(max_length=255, verbose_name="Introduzca el nombre del Chef 2", blank=True, null=True)
    nombre_chef3 = models.CharField(max_length=255, verbose_name="Introduzca el nombre del Chef 3", blank=True, null=True)

    reservar_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección para reservas")


        ##############  Sobre los Servicios ################
        ######################################################


    #titulo para describir sobre los servicios
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
    galeria_activo = models.BooleanField(blank=True, verbose_name="Agregar sección Galería")

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
    contactar_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección para contactar")

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

    # Campos adicionales para extender la funcionalidadsss
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='usuario/avatars', blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario}"




class Receta(models.Model):
    """Modelo para entradas de recetas."""

    fecha_hora = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    titulo = models.CharField(max_length=255,blank=True,null=True)
    categoria = models.CharField(max_length=255,blank=True,null=True)
    imagen = models.ImageField(upload_to='assets/img/recetas', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = HTMLField()
    resumen = HTMLField( blank=True,null=True)



    def __str__(self):
        """Devuelve el título del post como representación en cadena."""
        return self.titulo

    def get_summary(self):
        """Devuelve un resumen del cuerpo del post (primeras 200 palabras)."""
        return self.cuerpo[:200]

