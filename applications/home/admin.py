from django.contrib import admin
from applications.home.models import (
    Consulado,
    Embajada,
   Abogado,Blog,TipoEmpresa,
    Empresa,Post,Perfil
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
class TipoEmpresaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "id")

admin.site.register(TipoEmpresa,TipoEmpresaAdmin )


# comercios your models here.
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "pais", "tipo_empresa", "id")

admin.site.register(Empresa,EmpresaAdmin )


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
    list_display = ("avatar","usuario","fecha_nacimiento",)

admin.site.register(Perfil,PerfilAdmin)
