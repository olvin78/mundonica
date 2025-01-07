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


class Empresa(models.Model):
    #Nombre empresa header en el menu
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Empresa")
    #Header titulo en la página como texto principal h1
    subtitulo = models.CharField(max_length=100, verbose_name="Subtitulo", null=True, blank=True)
    #header subtitulo en la pagina debajo del texto principal como subtitulo
    descripcion = models.CharField(max_length=100, verbose_name="descripcion", null=True, blank=True)
    #imagen para el header a la par del subtitulo de presentacion
    imagen_header = models.ImageField(upload_to='empresas/imagenes/header', null=True, blank=True)
    #video de portada en el header solo se acepta enlace por el momento
    video_header = models.CharField(max_length=500, verbose_name="video_header", null=True, blank=True)

    #activar el aparatado de quienes somos, para poder agregarlo o que no aparezca
    quienes_somos_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección Sobre Nosotros")

    #titulo para describir sobre nosotros quienes somos como empresas
    parrafo1 = models.CharField(max_length=500, verbose_name="parrafo1", null=True, blank=True)
    #titulo para describir sobre nosotros quienes somos como empresas
    parrafo2 = models.CharField(max_length=500, verbose_name="parrafo2", null=True, blank=True)
    #titulo para describir sobre nosotros quienes somos como empresas
    parrafo3 = models.CharField(max_length=500, verbose_name="parrafo3", null=True, blank=True)
    #titulo para describir sobre nosotros quienes somos como empresas
    parrafo4 = models.CharField(max_length=500, verbose_name="parrafo4", null=True, blank=True)
    #titulo para describir sobre nosotros quienes somos como empresas
    parrafo5 = models.CharField(max_length=500, verbose_name="parrafo5", null=True, blank=True)
    #imagen para el apartado sobre nosotros  imagen mas grande
    imagen_nosotros = models.ImageField(upload_to='empresas/imagenes/nosotros', null=True, blank=True)
    #imagen para el apartado sobre nosotros imagen de fondo del video pequeño
    imagen_nosotros_fondo = models.ImageField(upload_to='empresas/imagenes/nosotros', null=True, blank=True)
    #video de portada en el header solo se acepta enlace por el momento
    video_nosotros = models.CharField(max_length=500, verbose_name="video_nosotros", null=True, blank=True)

    #activar el aparatado de vender menu de regalo, para poder agregarlo o que no aparezca
    menu_regalo_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección para vender menu de regalo")

    #esto es el campo para incluir lo que ofrece el menu para una persona en el apartado de menu de regalo numero 1
    #menu_regalo1 = models.CharField(max_length=500, verbose_name="menu_regalo1", null=True, blank=True)

    #esto es el campo para incluir lo que ofrece el menu para una persona en el apartado de menu de regalo numero 1
    menu_oferta1 = HTMLField(blank=True,null=True)
    #esto es el campo para incluir lo que ofrece el menu para una persona en el apartado de menu de regalo numero 2
    #menu_regalo2 = models.CharField(max_length=500, verbose_name="menu_regalo2", null=True, blank=True)

    #esto es el campo para incluir lo que ofrece el menu para una persona en el apartado de menu de regalo numero 2
    menu_oferta2= HTMLField(blank=True,null=True)
    #esto es el campo para incluir lo que ofrece el menu para una persona en el apartado de menu de regalo numero 3
    #menu_regalo3 = models.CharField(max_length=500, verbose_name="menu_regalo3", null=True, blank=True)
    
    #esto es el campo para incluir lo que ofrece el menu para una persona en el apartado de menu de regalo numero 3
    menu_oferta3 = HTMLField(blank=True,null=True)

    #activar el aparatado de la galería, para poder agregarlo o que no aparezca
    clientes_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección para ver clientes")

    #activar el aparatado de la galería, para poder agregarlo o que no aparezca
    platos_menu_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de platos")


    #imagen para el apartado de la galeria imagen numero 1
    plato_menu1 = models.ImageField(upload_to='empresas/imagenes/platos-menu', null=True, blank=True)

    #imagen para el apartado de la galeria imagen numero 1
    plato_menu2 = models.ImageField(upload_to='empresas/imagenes/platos-menu', null=True, blank=True)

    #imagen para el apartado de la galeria imagen numero 1
    plato_menu3 = models.ImageField(upload_to='empresas/imagenes/platos-menu', null=True, blank=True)

    #imagen para el apartado de la galeria imagen numero 1
    plato_menu4 = models.ImageField(upload_to='empresas/imagenes/Platos-menu', null=True, blank=True)

    #imagen para el apartado de la galeria imagen numero 1
    plato_menu5 = models.ImageField(upload_to='empresas/imagenes/Platos-menu', null=True, blank=True)

    #imagen para el apartado de la galeria imagen numero 1
    plato_menu6 = models.ImageField(upload_to='empresas/imagenes/platos-menu', null=True, blank=True)





    #activar el aparatado de la galería, para poder agregarlo o que no aparezca
    comentarios_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de comentarios")

     #activar el aparatado de la galería, para poder agregarlo o que no aparezca
    eventos_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de enventos")

    #activar el aparatado de la galería, para poder agregarlo o que no aparezca
    chefs_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección de chefs")

    #activar el aparatado de la galería, para poder agregarlo o que no aparezca
    reservar_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección para reservas")



    #activar el aparatado de la galería, para poder agregarlo o que no aparezca
    galeria_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección Galería")
    
    #imagen para el apartado de la galeria imagen numero 1
    imagen_galeria1 = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True)
    #imagen para el apartado de la galeria imagen numero 2
    imagen_galeria2 = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True)
    #imagen para el apartado de la galeria imagen numero 2
    imagen_galeria3 = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True)
    #imagen para el apartado de la galeria imagen numero 4
    imagen_galeria4 = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True)
    #imagen para el apartado de la galeria imagen numero 5
    imagen_galeria5 = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True)
    #imagen para el apartado de la galeria imagen numero 6
    imagen_galeria6 = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True)
    #imagen para el apartado de la galeria imagen numero 7
    imagen_galeria7 = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True)
    #imagen para el apartado de la galeria imagen numero 8
    imagen_galeria8 = models.ImageField(upload_to='empresas/imagenes/galeria', null=True, blank=True)


    #activar el aparatado de la galería, para poder agregarlo o que no aparezca
    contactar_activo = models.BooleanField(blank=True, null=True, verbose_name="Agregar sección para contactar")

    #horario para el apartado de contactar
    horario = models.CharField(max_length=500, verbose_name="horario", null=True, blank=True)
    pais = models.CharField(max_length=100, verbose_name="Pais de la Empresa")
    ciudad = models.CharField(max_length=100, verbose_name="Nombre de la Ciudad")
    imagen = models.ImageField(upload_to='empresas/imagenes/principal', null=True, blank=True)
    imagen_portada = models.ImageField(upload_to='empresas/imagenes/portada', null=True, blank=True)
    direccion = models.TextField(verbose_name="Direccion", null=True, blank=True)
    telefono = models.CharField(max_length=100, verbose_name="Numero de telefono", null=True, blank=True)
    email = models.EmailField(verbose_name="Correo electronico", null=True, blank=True)
    latitud = models.CharField(max_length=100,  verbose_name="Latitud", null=True, blank=True)
    longitud = models.CharField(max_length=100,  verbose_name="Longitud", null=True, blank=True)
    tipo_empresa = models.ForeignKey(TipoEmpresa,on_delete=models.CASCADE,related_name="empresas",verbose_name="Tipo de Empresa",null=True, blank=True)
    nombreUrl = models.SlugField(max_length=150, unique=True, null=True, blank=True)



    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ["pais", "ciudad"]


    def __str__(self):
        return f"{self.nombre} - {self.ciudad}, - {self.pais}"

######################### modelo de empresa peluqueria #########################
################################################################################


class Peluqueria(models.Model):
    #Nombre empresa header en el menu
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Empresa")
    #Header titulo en la página como texto principal h1
    subtitulo = models.CharField(max_length=100, verbose_name="Subtitulo", null=True, blank=True)
    #header subtitulo en la pagina debajo del texto principal como subtitulo
    descripcion = models.CharField(max_length=100, verbose_name="descripcion", null=True, blank=True)
    #imagen para el header a la par del subtitulo de presentacion
    imagen_header = models.ImageField(upload_to='empresas/imagenes/header', null=True, blank=True)
    


    class Meta:
        verbose_name = "Peluqueria"
        verbose_name_plural = "Peluquerias"
        ordering = ["nombre", "subtitulo"]


    def __str__(self):
        return f"{self.nombre} - {self.subtitulo}, - {self.descripcion}"





######################## este es el modelo de tipo de empresa de peluqueria ###################################
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
