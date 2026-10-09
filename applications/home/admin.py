from django.contrib import admin
from applications.home.models import (
    Consulado,
    Embajada,
    Abogado,
    Blog,
    TipoEmpresa,
    Post,
    Perfil,
    Empresa,
    Receta,
    SeccionMenu,
    HistoriaPropuesta,
    HistoriaConfiguracion,
    ImportacionPerfil,
)

# consulados your models here.
class ConsuladoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "pais", "ciudad",)

admin.site.register(Consulado,ConsuladoAdmin )

# embajadas your models here.
class EmbajadaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "pais", "ciudad",)

admin.site.register(Embajada,EmbajadaAdmin )

# comercios your models here.

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nombre_de_la_empresa", "tipo_perfil", "tipo_empresa", "estado_publicacion", "estado_verificacion", "estado_reclamacion", "propietario_sitio_web", "id")
    list_filter = ("tipo_perfil", "tipo_empresa", "pais", "region", "provincia", "estado_publicacion", "estado_verificacion", "estado_reclamacion", "propietario_sitio_web")
    search_fields = ("nombre_de_la_empresa", "identificador_externo", "email", "telefono")
    readonly_fields = ("identificador_externo", "fecha_incorporacion", "fecha_actualizacion")
    actions = ("publicar_perfiles", "archivar_perfiles", "mover_a_borrador")

    def get_fieldsets(self, request, obj=None):
        groups = [
            ("Información pública", {"fields": ("nombre_de_la_empresa", "nombreUrl", "tipo_perfil", "tipo_empresa", "descripcion_directorio", "relacion_nicaragua")}),
            ("Localización", {"fields": ("pais", "region", "provincia", "ciudad", "codigo_postal", "direccion", "latitud", "longitud")}),
            ("Contacto público", {"fields": ("telefono", "email", "sitio_web")}),
            ("Publicación y gestión", {"fields": ("estado_publicacion", "estado_verificacion", "estado_reclamacion", "propietario_sitio_web")}),
            ("Importación y fechas", {"fields": ("identificador_externo", "fecha_incorporacion", "fecha_actualizacion"), "classes": ("collapse",)}),
        ]
        used = {name for _, options in groups for name in options["fields"]}
        excluded = used | {"id"}
        legacy = [field.name for field in self.model._meta.fields if field.name not in excluded]
        if legacy:
            groups.append(("Contenido especializado existente", {"fields": tuple(legacy), "classes": ("collapse",)}))
        return groups

    @admin.action(description="Publicar perfiles validados")
    def publicar_perfiles(self, request, queryset):
        publicables = []
        omitidos = 0
        for empresa in queryset:
            try:
                if empresa.importacion_perfil.resultado_validacion != "valid":
                    omitidos += 1
                    continue
            except ImportacionPerfil.DoesNotExist:
                pass
            publicables.append(empresa.pk)
        actualizados = Empresa.objects.filter(pk__in=publicables).update(estado_publicacion="published")
        self.message_user(request, f"{actualizados} perfil(es) publicados; {omitidos} omitido(s) por validación.")

    @admin.action(description="Archivar perfiles")
    def archivar_perfiles(self, request, queryset):
        self.message_user(request, f"{queryset.update(estado_publicacion='archived')} perfil(es) archivados.")

    @admin.action(description="Mover a borrador")
    def mover_a_borrador(self, request, queryset):
        self.message_user(request, f"{queryset.update(estado_publicacion='draft')} perfil(es) movidos a borrador.")

admin.site.register(Empresa, EmpresaAdmin)


@admin.register(ImportacionPerfil)
class ImportacionPerfilAdmin(admin.ModelAdmin):
    list_display = ("identificador_externo", "empresa", "hoja_origen", "resultado_validacion", "ultima_importacion")
    list_filter = ("resultado_validacion", "canal_contacto", "disponibilidad_contacto", "tipo_direccion", "precision_localizacion", "hoja_origen")
    search_fields = ("identificador_externo", "empresa__nombre_de_la_empresa", "url_origen", "notas_internas", "errores_validacion")
    readonly_fields = ("empresa", "identificador_externo", "fuente_informacion", "url_origen", "hoja_origen", "notas_internas", "canal_contacto", "disponibilidad_contacto", "tipo_direccion", "precision_localizacion", "verificacion_original", "hash_fila", "primera_importacion", "ultima_importacion", "resultado_validacion", "datos_ultima_importacion", "campos_en_conflicto", "errores_validacion")

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class TipoEmpresaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "plantilla_perfil", "descripcion", "id")
    list_editable = ("plantilla_perfil",)

admin.site.register(TipoEmpresa,TipoEmpresaAdmin )

# abogados your models here.
class AbogadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "telefono","verificado",)

admin.site.register(Abogado,AbogadoAdmin )

# blog your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "imagen",)

admin.site.register(Blog,BlogAdmin )



# blog your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("autor", "fecha_hora", "comentario",)

admin.site.register(Post,PostAdmin )



# comercios your models here.
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("usuario","id","telefono","direccion","fecha_nacimiento",)

admin.site.register(Perfil,PerfilAdmin)


# blog your models here.
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'id', 'autor', 'categoria', 'fecha_hora')

    def get_queryset(self, request):
        """Restringe que los usuarios solo vean y editen sus propias recetas"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # Los superusuarios pueden ver todo
            return qs
        return qs.filter(autor=request.user)

admin.site.register(Receta, RecetaAdmin)


# Secciones del menú (header): activar/desactivar enlaces sin tocar código.
class SeccionMenuAdmin(admin.ModelAdmin):
    list_display = ("nombre", "clave", "activo", "orden")
    list_editable = ("activo", "orden")  # se puede togglear directo desde la lista, sin abrir cada uno
    list_filter = ("activo",)
    ordering = ("orden",)

admin.site.register(SeccionMenu, SeccionMenuAdmin)


@admin.register(HistoriaPropuesta)
class HistoriaPropuestaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 'ciudad_pais', 'email', 'preferencia_grabacion',
        'lugar_grabacion', 'estado', 'recibida_en',
    )
    list_filter = (
        'estado', 'preferencia_contacto', 'preferencia_grabacion',
        'lugar_grabacion', 'recibida_en',
    )
    list_editable = ('estado',)
    search_fields = ('nombre', 'ciudad_pais', 'email', 'historia')
    readonly_fields = ('recibida_en', 'actualizada_en')
    ordering = ('-recibida_en',)


@admin.register(HistoriaConfiguracion)
class HistoriaConfiguracionAdmin(admin.ModelAdmin):
    fields = ('video_youtube_id',)

    def has_add_permission(self, request):
        return not HistoriaConfiguracion.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False