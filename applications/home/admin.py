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
    Receta
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
    list_display = ("nombre_de_la_empresa","tipo_empresa","id")

admin.site.register(Empresa,EmpresaAdmin )

class TipoEmpresaAdmin(admin.ModelAdmin):
    list_display = ("nombre","descripcion", "id")

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