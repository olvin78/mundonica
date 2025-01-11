from django import forms
from .models import Abogado,Empresa
from .models import Perfil



class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu correo electrónico'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Tu mensaje',
            'rows': 5
        }),
        required=True,
        max_length=2000
    )



class AbogadoForm(forms.ModelForm):
    class Meta:
        model = Abogado
        fields = [
            'nombre', 'apellido', 'imagen', 'pais', 'ciudad', 'direccion',
            'precio', 'titulo', 'telefono', 'email', 'latitud', 'longitud',
            'descripcion', 'resumen', 'asesoriajuridicageneral',
            'redaccionyrevisiondedocumentos', 'representacionlegal', 'mediacionyarbitraje',
            'tramitesdevisasypermisosdetrabajo', 'procesosdenaturalizacion',
            'defensaencasosdedeportacion', 'asesoriaenreagrupacionfamiliar',
            'asesoriaencasosdedivorcioyseparacion', 'tramitesdepartidadenacimientoydefunciones',
            'asesoriaenherenciasytestamentos', 'negocioacionyredacciondecontratos',
            'asistenciaencasosdedespidos', 'asesoramientoparaemprendedores',
            'propiedadintelectual', 'asesoriaparaexportaciondeproductos',
            'defenzaencasospenales', 'asesoriaencasosdeviolenciaoabusos',
            'traduccionylegalizaciondedocumentos', 'capacitacionesytalleresjuridicos'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'resumen': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'asesoriajuridicageneral': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'redaccionyrevisiondedocumentos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'representacionlegal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'mediacionyarbitraje': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tramitesdevisasypermisosdetrabajo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'procesosdenaturalizacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'defensaencasosdedeportacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'asesoriaenreagrupacionfamiliar': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'asesoriaencasosdedivorcioyseparacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tramitesdepartidadenacimientoydefunciones': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'asesoriaenherenciasytestamentos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'negocioacionyredacciondecontratos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'asistenciaencasosdedespidos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'asesoramientoparaemprendedores': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'propiedadintelectual': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'asesoriaparaexportaciondeproductos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'defenzaencasospenales': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'asesoriaencasosdeviolenciaoabusos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'traduccionylegalizaciondedocumentos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'capacitacionesytalleresjuridicos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }



"""class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nombre', 'subtitulo', 'pais', 'ciudad', 'imagen', 'imagen_portada',
            'direccion', 'telefono', 'email', 'latitud', 'longitud', 'parrafo1',
            'descripcion', 'tipo_empresa'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la empresa'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el subtítulo'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'País de la empresa'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad de la empresa'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagen_portada': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Dirección completa'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitud'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Longitud'}),
            'parrafo1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'parrafo descriptivo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción breve'}),
            'tipo_empresa': forms.Select(attrs={'class': 'form-select'}),
        }
"""

class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nombre_de_la_empresa','titulo_header','subtitulo1_header','subtitulo2_header', 
            'imagen_logo_empresa','imagen_fondo_header','imagen_header','video_header',
            'quienes_somos_activo','titulo_sobrenosotros','parrafo1_sobrenosotros', 
            'parrafo2_sobrenosotros','parrafo3_sobrenosotros','parrafo4_sobrenosotros', 
            'parrafo5_sobrenosotros','imagen1_nosotros','imagen2_nosotros_fondo','video_nosotros',
            'menu_regalo_activo','menu_oferta1','menu_oferta2','menu_oferta3',
            'clientes_activo','platos_menu_activo','plato_menu1','plato_menu2', 
            'plato_menu3','plato_menu4','plato_menu5','plato_menu6',
            'comentarios_activo','parrafo1_comentario','parrafo2_comentario','parrafo3_comentario',
            'nombre1_comentario','nombre2_comentario','nombre3_comentario','eventos_activo',
            'chefs_activo','reservar_activo','titulo_servicios','imagen_servicio1', 
            'imagen_servicio2','imagen_servicio3','nombre_servicio1','nombre_servicio2', 
            'nombre_servicio3','parrafo_servicios1','parrafo_servicios2','parrafo_servicios3',
            'titulo_trabajadores','imagen_trabajador1','imagen_trabajador2','imagen_trabajador3', 
            'nombre_trabajador1','nombre_trabajador2','nombre_trabajador3','titulo_tarifa',
            'imagen_tarifa1','imagen_tarifa2','nombre_servicio1_tarifa','nombre_servicio2_tarifa', 
            'nombre_servicio3_tarifa','nombre_servicio4_tarifa','nombre_servicio5_tarifa', 
            'nombre_servicio6_tarifa','nombre_servicio7_tarifa','nombre_servicio8_tarifa', 
            'nombre_servicio9_tarifa','nombre_servicio10_tarifa','precio_servicio1_tarifa', 
            'precio_servicio2_tarifa','precio_servicio3_tarifa','precio_servicio4_tarifa', 
            'precio_servicio5_tarifa','precio_servicio6_tarifa','precio_servicio7_tarifa', 
            'precio_servicio8_tarifa','precio_servicio9_tarifa','precio_servicio10_tarifa',
            'galeria_activo','titulo1_galeria','imagen1_galeria','imagen2_galeria','imagen3_galeria', 
            'imagen4_galeria','imagen5_galeria','imagen6_galeria','imagen7_galeria', 
            'imagen8_galeria','imagen9_galeria','contactar_activo','horario','pais', 
            'ciudad','imagen','imagen_portada','direccion','telefono','email', 
            'latitud','longitud','tipo_empresa','nombreUrl'
        ]
        widgets = {

            # Campos de texto
            'nombre_de_la_empresa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la empresa'}),
            'titulo_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título del header'}),
            'subtitulo1_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Subtítulo 1 del header'}),
            'subtitulo2_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Subtítulo 2 del header'}),
            'video_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'URL del video del header'}),

            'direccion': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Dirección completa'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Teléfono de contacto'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Correo electrónico'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Latitud'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Longitud'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Slug único'}),
            


            'quienes_somos_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),

            'titulo_sobrenosotros': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título Sobre Nosotros'}),
            'parrafo1_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 1 Sobre Nosotros'}),
            'parrafo2_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 2 Sobre Nosotros'}),
            'parrafo3_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 3 Sobre Nosotros'}),
            'parrafo4_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 4 Sobre Nosotros'}),
            'parrafo5_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 5 Sobre Nosotros'}),
            'imagen1_nosotros': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_nosotros_fondo': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'video_nosotros': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'URL del Video Sobre Nosotros'}),

            #campo de los platos 
            'menu_regalo_activo': forms.Select(
                attrs={'class': 'form-select form-select-lg border-success'},
                choices=[
                    ('SI', 'Sí'),
                    ('NO', 'No'),
                    ('DK', 'Desconocido')
                ]
            ),

            'menu_oferta1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Detalle de la oferta del menú 1'}),
            'menu_oferta2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Detalle de la oferta del menú 2'}),
            'menu_oferta3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Detalle de la oferta del menú 3'}),
            'clientes_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),

            'platos_menu_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),

            'plato_menu1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 1'}),
            'plato_menu2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 2'}),
            'plato_menu3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 3'}),
            'plato_menu4': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 4'}),
            'plato_menu5': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 5'}),
            'plato_menu6': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 6'}),

            # Campos de archivo (TODOS configurados de manera uniforme)
            'imagen_logo_empresa': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_fondo_header': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_header': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen1_nosotros': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_nosotros_fondo': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            # Widgets para las tarifas
            'titulo_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título de la sección de tarifa'}),

            'imagen_tarifa1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_tarifa2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'nombre_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 1'}),
            'nombre_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 2'}),
            'nombre_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 3'}),
            'nombre_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 4'}),
            'nombre_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 5'}),
            'nombre_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 6'}),
            'nombre_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 7'}),
            'nombre_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 8'}),
            'nombre_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 9'}),
            'nombre_servicio10_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 10'}),
            'precio_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 1'}),
            'precio_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 2'}),
            'precio_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 3'}),
            'precio_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 4'}),
            'precio_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 5'}),
            'precio_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 6'}),
            'precio_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 7'}),
            'precio_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 8'}),
            'precio_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 9'}),
            'precio_servicio10_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 10'}),
            

            'comentarios_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),

            'parrafo1_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo comentario 1'}),
            'parrafo2_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo comentario 2'}),
            'parrafo3_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo comentario 3'}),
            'nombre1_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la persona que hace el comentario 1'}),
            'nombre2_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la persona que hace el comentario 2'}),
            'nombre3_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la persona que hace el comentario 3'}),
            
            'eventos_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),

            'chefs_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),

            'reservar_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]
        ),

            #trabajadores
            'titulo_trabajadores': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título para describir trabajadores'}),
            'imagen_trabajador1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'nombre_trabajador1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del trabajador 1'}),
            'nombre_trabajador2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del trabajador 2'}),
            'nombre_trabajador3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del trabajador 3'}),

            'titulo_servicios': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título para describir servicios'}),
            'imagen_servicio1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'nombre_servicio1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 1'}),
            'nombre_servicio2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 2'}),
            'nombre_servicio3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 3'}),
            'parrafo_servicios1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 1'}),
            'parrafo_servicios2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 2'}),
            'parrafo_servicios3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 3'}),


            # Widgets para Título y Galería
            'galeria_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]
        ),

            'titulo1_galeria': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título para describir la galería'}),
            'imagen1_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen3_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen4_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen5_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen6_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen7_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen8_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),

            'horario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese el horario'}),
            'pais': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese el país de la empresa'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese la ciudad'}),
            'imagen_portada': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),

            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            # Campos de selección
            'tipo_empresa': forms.Select(attrs={'class': 'form-select form-select-lg border-success'}),
            #mapa de ubicasion
            'titulo_ubicacion_mapa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese el parrafo sbre la seccion del mapa'}),


            'contactar_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]
        ),

            
        }


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'avatar'
        ]
        widgets = {

            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class PeluqueriaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nombre_de_la_empresa', 'titulo_header', 'subtitulo1_header', 'subtitulo2_header', 
            'imagen_logo_empresa', 'imagen_fondo_header','quienes_somos_activo', 'titulo_sobrenosotros', 'parrafo1_sobrenosotros', 
            'parrafo2_sobrenosotros', 'imagen1_nosotros', 'imagen2_nosotros_fondo',
            'comentarios_activo', 'parrafo1_comentario', 'parrafo2_comentario', 'parrafo3_comentario',
            'nombre1_comentario', 'nombre2_comentario', 'nombre3_comentario', 'eventos_activo','reservar_activo', 'titulo_servicios', 'imagen_servicio1', 
            'imagen_servicio2', 'imagen_servicio3', 'nombre_servicio1', 'nombre_servicio2', 
            'nombre_servicio3', 'parrafo_servicios1', 'parrafo_servicios2', 'parrafo_servicios3',
            'titulo_trabajadores', 'imagen_trabajador1', 'imagen_trabajador2', 'imagen_trabajador3', 
            'nombre_trabajador1', 'nombre_trabajador2', 'nombre_trabajador3', 'titulo_tarifa',
            'imagen_tarifa1', 'imagen_tarifa2', 'nombre_servicio1_tarifa', 'nombre_servicio2_tarifa', 
            'nombre_servicio3_tarifa', 'nombre_servicio4_tarifa', 'nombre_servicio5_tarifa', 
            'nombre_servicio6_tarifa', 'nombre_servicio7_tarifa', 'nombre_servicio8_tarifa', 
            'nombre_servicio9_tarifa', 'nombre_servicio10_tarifa', 'precio_servicio1_tarifa', 
            'precio_servicio2_tarifa', 'precio_servicio3_tarifa', 'precio_servicio4_tarifa', 
            'precio_servicio5_tarifa', 'precio_servicio6_tarifa', 'precio_servicio7_tarifa', 
            'precio_servicio8_tarifa', 'precio_servicio9_tarifa', 'precio_servicio10_tarifa', 
            'galeria_activo', 'titulo1_galeria','imagen1_galeria','imagen2_galeria', 'imagen3_galeria', 
            'imagen4_galeria', 'contactar_activo', 'horario', 'pais', 
            'ciudad', 'imagen', 'imagen_portada', 'direccion', 'telefono', 'email', 
            'latitud', 'longitud', 'tipo_empresa', 'nombreUrl'
        ]

        widgets = {
            'nombre_de_la_empresa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la empresa'}),
            'titulo_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título del header'}),
            'subtitulo1_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Subtítulo 1 del header'}),
            'subtitulo2_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Subtítulo 2 del header'}),
            #sellecioinar el tipo de empresa
            'tipo_empresa': forms.Select(attrs={'class': 'form-select form-select-lg border-success'}),
            #sobre nosotros
            'titulo_sobrenosotros': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título Sobre Nosotros'}),
            'parrafo1_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 1 Sobre Nosotros'}),
            'parrafo2_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 2 Sobre Nosotros'}),
            'parrafo3_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 3 Sobre Nosotros'}),
            'imagen1_nosotros': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_nosotros_fondo': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            #servicios
            'titulo_servicios': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título para describir servicios que se ofrecen'}),
            'imagen_servicio1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'nombre_servicio1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 1'}),
            'nombre_servicio2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 2'}),
            'nombre_servicio3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 3'}),
            'parrafo_servicios1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 1'}),
            'parrafo_servicios2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 2'}),
            'parrafo_servicios3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 3'}),
            #trabajadores
            'titulo_trabajadores': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título para describir trabajadores'}),
            'imagen_trabajador1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'nombre_trabajador1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del trabajador 1'}),
            'nombre_trabajador2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del trabajador 2'}),
            'nombre_trabajador3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del trabajador 3'}),
            # Widgets para las tarifas
            'titulo_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título de la sección de tarifa'}),
            'imagen_tarifa1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_tarifa2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'nombre_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 1'}),
            'nombre_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 2'}),
            'nombre_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 3'}),
            'nombre_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 4'}),
            'nombre_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 5'}),
            'nombre_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 6'}),
            'nombre_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 7'}),
            'nombre_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 8'}),
            'nombre_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 9'}),
            'nombre_servicio10_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 10'}),
            'precio_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 1'}),
            'precio_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 2'}),
            'precio_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 3'}),
            'precio_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 4'}),
            'precio_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 5'}),
            'precio_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 6'}),
            'precio_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 7'}),
            'precio_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 8'}),
            'precio_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 9'}),
            'precio_servicio10_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 10'}),
            #galeria
            'titulo1_galeria': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título de la galería'}),
            'imagen1_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'image2_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'image3_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'image4_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            #comentario
            'parrafo1_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo comentario 1'}),
            'parrafo2_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo comentario 2'}),
            'parrafo3_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo comentario 3'}),
            'nombre1_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la persona que hace el comentario 1'}),
            'nombre2_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la persona que hace el comentario 2'}),
            'nombre3_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la persona que hace el comentario 3'}),
            #mapa de ubicasion
            'titulo_ubicacion_mapa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese el parrafo sobre la seccion del mapa'}),
            'subtitulo_ubicacion_mapa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Subtítulo para descripcion del mapa'}),
            #contacto
            'direccion': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Dirección completa'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Teléfono de contacto'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Correo electrónico'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Latitud'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Longitud'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Slug único'}),



        }

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
                'nombre_de_la_empresa', 'titulo_header', 'subtitulo1_header', 'subtitulo2_header', 
                'imagen_logo_empresa', 'imagen_fondo_header', 'imagen_header', 'video_header',
                'quienes_somos_activo', 'titulo_sobrenosotros', 'parrafo1_sobrenosotros', 
                'parrafo2_sobrenosotros', 'parrafo3_sobrenosotros', 'parrafo4_sobrenosotros', 
                'parrafo5_sobrenosotros', 'imagen1_nosotros', 'imagen2_nosotros_fondo', 'video_nosotros',
                'menu_regalo_activo', 'menu_oferta1', 'menu_oferta2', 'menu_oferta3',
                'clientes_activo', 'platos_menu_activo', 'plato_menu1', 'plato_menu2', 
                'plato_menu3', 'plato_menu4', 'plato_menu5', 'plato_menu6',
                'comentarios_activo', 'parrafo1_comentario', 'parrafo2_comentario', 'parrafo3_comentario',
                'nombre1_comentario', 'nombre2_comentario', 'nombre3_comentario', 'eventos_activo',
                'chefs_activo', 'reservar_activo', 'titulo_servicios', 
                'imagen_servicio2', 'imagen_servicio3', 'nombre_servicio1', 'nombre_servicio2','propietario_sitio_web',
                'nombre_servicio3', 'parrafo_servicios1', 'parrafo_servicios2', 'parrafo_servicios3',
                'titulo_trabajadores', 'imagen_trabajador1', 'imagen_trabajador2', 'imagen_trabajador3', 
                'nombre_trabajador1', 'nombre_trabajador2', 'nombre_trabajador3', 'titulo_tarifa',
                'imagen_tarifa1', 'imagen_tarifa2', 'nombre_servicio1_tarifa', 'nombre_servicio2_tarifa', 
                'nombre_servicio3_tarifa', 'nombre_servicio4_tarifa', 'nombre_servicio5_tarifa', 
                'nombre_servicio6_tarifa', 'nombre_servicio7_tarifa', 'nombre_servicio8_tarifa', 
                'nombre_servicio9_tarifa', 'nombre_servicio10_tarifa', 'precio_servicio1_tarifa', 
                'precio_servicio2_tarifa', 'precio_servicio3_tarifa', 'precio_servicio4_tarifa', 
                'precio_servicio5_tarifa', 'precio_servicio6_tarifa', 'precio_servicio7_tarifa', 
                'precio_servicio8_tarifa', 'precio_servicio9_tarifa', 'precio_servicio10_tarifa', 
                'galeria_activo', 'titulo1_galeria','imagen1_galeria','imagen2_galeria', 'imagen3_galeria', 
                'imagen4_galeria', 'imagen5_galeria', 'imagen6_galeria', 'imagen7_galeria', 
                'imagen8_galeria', 'imagen9_galeria', 'contactar_activo', 'horario', 'pais', 
                'ciudad', 'imagen_portada', 'direccion', 'telefono', 'email', 
                'latitud', 'longitud', 'tipo_empresa', 'nombreUrl'
            ]
        widgets = {

            # Campos de texto
            'nombre_de_la_empresa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la empresa'}),
            'titulo_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título del header'}),
            'subtitulo1_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Subtítulo 1 del header'}),
            'subtitulo2_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Subtítulo 2 del header'}),
            'video_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'URL del video del header'}),

            'direccion': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Dirección completa'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Teléfono de contacto'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Correo electrónico'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Latitud'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Longitud'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Slug único'}),
            

            'nombre_servicio1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 1'}),
            'nombre_servicio2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 2'}),
            'nombre_servicio3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 3'}),
            'parrafo_servicios1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 1'}),
            'parrafo_servicios2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 2'}),
            'parrafo_servicios3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 3'}),

            'quienes_somos_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),

            'titulo_sobrenosotros': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título Sobre Nosotros'}),
            'parrafo1_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 1 Sobre Nosotros'}),
            'parrafo2_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 2 Sobre Nosotros'}),
            'parrafo3_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 3 Sobre Nosotros'}),
            'parrafo4_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 4 Sobre Nosotros'}),
            'parrafo5_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 5 Sobre Nosotros'}),
            'imagen1_nosotros': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_nosotros_fondo': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'video_nosotros': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'URL del Video Sobre Nosotros'}),

            #campo de los platos 
            'menu_regalo_activo': forms.Select(
                attrs={'class': 'form-select form-select-lg border-success'},
                choices=[
                    ('SI', 'Sí'),
                    ('NO', 'No'),
                    ('DK', 'Desconocido')
                ]
            ),

            'menu_oferta1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Detalle de la oferta del menú 1'}),
            'menu_oferta2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Detalle de la oferta del menú 2'}),
            'menu_oferta3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Detalle de la oferta del menú 3'}),
            'clientes_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),

            'platos_menu_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),

            'plato_menu1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 1'}),
            'plato_menu2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 2'}),
            'plato_menu3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 3'}),
            'plato_menu4': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 4'}),
            'plato_menu5': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 5'}),
            'plato_menu6': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 6'}),

            # Campos de archivo (TODOS configurados de manera uniforme)
            'imagen_logo_empresa': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_fondo_header': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_header': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen1_nosotros': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_nosotros_fondo': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            # Widgets para las tarifas
            'titulo_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título de la sección de tarifa'}),

            'imagen_tarifa1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_tarifa2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'nombre_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 1'}),
            'nombre_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 2'}),
            'nombre_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 3'}),
            'nombre_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 4'}),
            'nombre_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 5'}),
            'nombre_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 6'}),
            'nombre_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 7'}),
            'nombre_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 8'}),
            'nombre_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 9'}),
            'nombre_servicio10_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 10'}),
            'precio_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 1'}),
            'precio_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 2'}),
            'precio_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 3'}),
            'precio_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 4'}),
            'precio_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 5'}),
            'precio_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 6'}),
            'precio_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 7'}),
            'precio_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 8'}),
            'precio_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 9'}),
            'precio_servicio10_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 10'}),
            

            'comentarios_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),

            'parrafo1_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo comentario 1'}),
            'parrafo2_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo comentario 2'}),
            'parrafo3_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo comentario 3'}),
            'nombre1_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la persona que hace el comentario 1'}),
            'nombre2_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la persona que hace el comentario 2'}),
            'nombre3_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la persona que hace el comentario 3'}),
            
            'eventos_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),

            'chefs_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),

            'reservar_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]
        ),

            #trabajadores
            'titulo_trabajadores': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título para describir trabajadores'}),
            'imagen_trabajador1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'nombre_trabajador1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del trabajador 1'}),
            'nombre_trabajador2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del trabajador 2'}),
            'nombre_trabajador3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del trabajador 3'}),

            'titulo_servicios': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título para describir servicios'}),
            'imagen_servicio1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'nombre_servicio1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 1'}),
            'nombre_servicio2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 2'}),
            'nombre_servicio3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 3'}),
            'parrafo_servicios1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 1'}),
            'parrafo_servicios2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 2'}),
            'parrafo_servicios3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 3'}),


            # Widgets para Título y Galería
            'galeria_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]
        ),

            'titulo1_galeria': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título para describir la galería'}),
            'imagen1_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen3_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen4_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen5_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen6_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen7_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen8_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen9_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            
            'horario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese el horario'}),
            'pais': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese el país de la empresa'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese la ciudad'}),
            'imagen_portada': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),

            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            # Campos de selección
            'tipo_empresa': forms.Select(attrs={'class': 'form-select form-select-lg border-success'}),
            #mapa de ubicasion
            'titulo_ubicacion_mapa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese el parrafo sbre la seccion del mapa'}),


            'contactar_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]
        ),

            
        }


class ComercioForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
                'nombre_de_la_empresa', 'titulo_header', 'imagen_logo_empresa', 'imagen_fondo_header',
                'quienes_somos_activo', 'parrafo1_sobrenosotros', 'parrafo2_sobrenosotros', 
                'parrafo3_sobrenosotros', 'parrafo4_sobrenosotros', 'parrafo5_sobrenosotros', 
                'imagen1_nosotros', 'imagen2_nosotros_fondo', 'imagen3_nosotros',
                'comentarios_activo', 'parrafo1_comentario', 'parrafo2_comentario', 
                'parrafo3_comentario', 'nombre1_comentario', 'nombre2_comentario', 
                'nombre3_comentario', 'imagen1_comentario', 'imagen2_comentario', 'imagen3_comentario',
                'nombre_servicio1_tarifa', 'nombre_servicio2_tarifa', 'nombre_servicio3_tarifa', 
                'nombre_servicio4_tarifa', 'nombre_servicio5_tarifa', 'nombre_servicio6_tarifa', 
                'nombre_servicio7_tarifa', 'nombre_servicio8_tarifa', 'nombre_servicio9_tarifa', 
                'nombre_servicio10_tarifa', 'precio_servicio1_tarifa', 'precio_servicio2_tarifa', 
                'precio_servicio3_tarifa', 'precio_servicio4_tarifa', 'precio_servicio5_tarifa', 
                'precio_servicio6_tarifa', 'precio_servicio7_tarifa', 'precio_servicio8_tarifa',
                'galeria_activo', 'titulo1_galeria', 'imagen1_galeria', 'imagen2_galeria', 
                'imagen3_galeria', 'imagen4_galeria', 'imagen5_galeria', 'imagen6_galeria', 
                'imagen7_galeria', 'imagen8_galeria', 'imagen9_galeria', 'imagen10_galeria', 
                'imagen11_galeria', 'contactar_activo', 'pais', 'ciudad', 'direccion', 
                'telefono', 'email', 'latitud', 'longitud', 'tipo_empresa', 'nombreUrl'
            ]

        widgets = {

            # Campos de texto
            'nombre_de_la_empresa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la empresa'}),
            'titulo_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título del header'}),
            # Campos de archivo (TODOS configurados de manera uniforme)
            'imagen_logo_empresa': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_fondo_header': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_header': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            
            #servicio
            'titulo_servicios': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título para describir servicios'}),
            'nombre_servicio1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 1'}),
            'nombre_servicio2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 2'}),
            'nombre_servicio3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 3'}),
            'parrafo_servicios1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 1'}),
            'parrafo_servicios2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 2'}),
            'parrafo_servicios3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 3'}),


            #sobre nosotros
            'quienes_somos_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),

            'parrafo1_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 1 Sobre Nosotros'}),
            'parrafo2_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 2 Sobre Nosotros'}),
            'parrafo3_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 3 Sobre Nosotros'}),
            'parrafo4_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 4 Sobre Nosotros'}),
            'parrafo5_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Párrafo 5 Sobre Nosotros'}),
            
            'imagen1_nosotros': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_nosotros_fondo': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen3_nosotros': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'URL del Video Sobre Nosotros'}),

            # Widgets para las tarifas
            'nombre_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 1'}),
            'nombre_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 2'}),
            'nombre_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 3'}),
            'nombre_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 4'}),
            'nombre_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 5'}),
            'nombre_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 6'}),
            'nombre_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 7'}),
            'nombre_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 8'}),
            'nombre_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 9'}),
            'nombre_servicio10_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 10'}),
            
            'precio_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 1'}),
            'precio_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 2'}),
            'precio_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 3'}),
            'precio_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 4'}),
            'precio_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 5'}),
            'precio_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 6'}),
            'precio_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 7'}),
            'precio_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 8'}),
            'precio_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 9'}),
            'precio_servicio10_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 10'}),
            

            'comentarios_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),
            'nombre1_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la persona que hace el comentario 1'}),
            'nombre2_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la persona que hace el comentario 2'}),
            'nombre3_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la persona que hace el comentario 3'}),
            'parrafo1_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo comentario 1'}),
            'parrafo2_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo comentario 2'}),
            'parrafo3_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo comentario 3'}),
            'imagen1_comentario': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_comentario': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen3_comentario': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),


            # Widgets para Título y Galería
            'galeria_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]
        ),

            'titulo1_galeria': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título para describir sus productos'}),
            'imagen1_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen3_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen4_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen5_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen6_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen7_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen8_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen9_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen10_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            
            'horario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese el horario'}),
            'pais': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese el país de la empresa'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese la ciudad'}),
            'imagen_portada': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),

            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            # Campos de selección
            'tipo_empresa': forms.Select(attrs={'class': 'form-select form-select-lg border-success'}),
            #mapa de ubicasion
            'titulo_ubicacion_mapa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese el parrafo sbre la seccion del mapa'}),


            'contactar_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]
        ),

            'direccion': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Dirección completa'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Teléfono de contacto'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Correo electrónico'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Latitud'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Longitud'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Slug único'}),
            



            
        }