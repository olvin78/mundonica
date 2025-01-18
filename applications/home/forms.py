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
            'nombre_de_la_empresa', 'nombreUrl','titulo_header','subtitulo1_header','subtitulo2_header', 
            'imagen_logo_empresa','imagen_fondo_header','imagen_header','video_header',
            'quienes_somos_activo','titulo_sobrenosotros','parrafo1_sobrenosotros', 
            'parrafo2_sobrenosotros','parrafo3_sobrenosotros','parrafo4_sobrenosotros', 
            'parrafo5_sobrenosotros','imagen1_nosotros','imagen2_nosotros_fondo','video_nosotros',
            'menu_regalo_activo','menu_oferta1','menu_oferta2','menu_oferta3',
            'clientes_activo','platos_menu_activo',

            'nombre1_plato_menu','nombre2_plato_menu','nombre3_plato_menu','nombre4_plato_menu',
            'nombre5_plato_menu','nombre6_plato_menu','nombre7_plato_menu','nombre8_plato_menu',
            'nombre9_plato_menu','nombre10_plato_menu',

            'imagen1_plato_menu','imagen2_plato_menu','imagen3_plato_menu','imagen4_plato_menu',
            'imagen5_plato_menu','imagen6_plato_menu','imagen7_plato_menu','imagen8_plato_menu',
            'imagen9_plato_menu','imagen10_plato_menu',

            'descriptcion1_plato_menu','descriptcion2_plato_menu','descriptcion3_plato_menu',
            'descriptcion4_plato_menu','descriptcion5_plato_menu','descriptcion6_plato_menu',
            'descriptcion7_plato_menu','descriptcion8_plato_menu','descriptcion9_plato_menu',
            'descriptcion10_plato_menu',

            'precio1_plato_menu','precio2_plato_menu','precio3_plato_menu','precio4_plato_menu',
            'precio5_plato_menu','precio6_plato_menu','precio7_plato_menu','precio8_plato_menu',
            'precio9_plato_menu','precio10_plato_menu',

             # Comentarios
            'comentarios_activo', 
            'parrafo1_comentario','parrafo2_comentario','parrafo3_comentario','nombre1_comentario',
            'nombre2_comentario','nombre3_comentario','imagen1_comentario','imagen2_comentario',
            'imagen3_comentario',

            # Eventos y Chefs
            'eventos_activo','chefs_activo', 

            'nombre_chef1','nombre_chef2','nombre_chef3',
            'imagen_chef1','imagen_chef2','imagen_chef3',
            # Reservar
            'reservar_activo',

            # Servicios
            'titulo_servicios',
            'imagen_servicio1','imagen_servicio2','imagen_servicio3','imagen_servicio4',
            'nombre_servicio1','nombre_servicio2','nombre_servicio3','nombre_servicio4',
            'parrafo_servicios1','parrafo_servicios2','parrafo_servicios3','parrafo_servicios4',

            # Tarifas
            'titulo_tarifa',
            'imagen_tarifa1','imagen_tarifa2',
            'nombre_servicio1_tarifa','nombre_servicio2_tarifa','nombre_servicio3_tarifa',
            'nombre_servicio4_tarifa','nombre_servicio5_tarifa','nombre_servicio6_tarifa',
            'nombre_servicio7_tarifa','nombre_servicio8_tarifa','nombre_servicio9_tarifa',
            'nombre_servicio10_tarifa',
            'precio_servicio1_tarifa','precio_servicio2_tarifa','precio_servicio3_tarifa',
            'precio_servicio4_tarifa','precio_servicio5_tarifa','precio_servicio6_tarifa',
            'precio_servicio7_tarifa','precio_servicio8_tarifa','precio_servicio9_tarifa',
            'precio_servicio10_tarifa',

            # Galería
            'galeria_activo', 
            'titulo1_galeria',
            'imagen1_galeria','imagen2_galeria','imagen3_galeria','imagen4_galeria',
            'imagen5_galeria','imagen6_galeria','imagen7_galeria','imagen8_galeria',

            # Contacto
            'contactar_activo','imagen_portada_reserva',
            'horario','pais','ciudad','direccion', 
            'imagen_portada',
            'telefono','email','latitud','longitud',

            # Empresa
            'tipo_empresa',
        ]

        widgets = {

            # Campos de texto
            'nombre_de_la_empresa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la empresa'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'introduzca el nombre de la url sin espacios'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            'titulo_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título del header'}),
            'subtitulo1_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Subtítulo 1 del header'}),
            'subtitulo2_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Subtítulo 2 del header'}),
            'imagen_header': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'video_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'URL del video del header'}),

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
            'menu_regalo_activo': forms.Select(attrs={'class': 'form-select form-select-lg border-success'},choices=[('SI', 'Sí'),('NO', 'No'),('DK', 'Desconocido')]),

            'menu_oferta1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Detalle del menú 1'}),
            'menu_oferta2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Detalle del menú 2'}),
            'menu_oferta3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Detalle del menú 3'}),

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

            'nombre1_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del plato 1'}),
            'nombre2_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del plato 2'}),
            'nombre3_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del plato 3'}),
            'nombre4_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del plato 4'}),
            'nombre5_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del plato 5'}),
            'nombre6_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del plato 6'}),
            'nombre7_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del plato 7'}),
            'nombre8_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del plato 8'}),
            'nombre9_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del plato 9'}),
            'nombre10_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del plato 10'}),

            'imagen1_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 1'}),
            'imagen2_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 2'}),
            'imagen3_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 3'}),
            'imagen4_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 4'}),
            'imagen5_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 5'}),
            'imagen6_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 6'}),
            'imagen7_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 7'}),
            'imagen8_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 8'}),
            'imagen9_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 9'}),
            'imagen10_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen del plato 10'}),

            'descriptcion1_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingredientes del plato 1'}),
            'descriptcion2_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingredientes del plato 2'}),
            'descriptcion3_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingredientes del plato 3'}),
            'descriptcion4_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingredientes del plato 4'}),
            'descriptcion5_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingredientes del plato 5'}),
            'descriptcion6_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingredientes del plato 6'}),
            'descriptcion7_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingredientes del plato 7'}),
            'descriptcion8_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingredientes del plato 8'}),
            'descriptcion9_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingredientes del plato 9'}),
            'descriptcion10_plato_menu':forms.TextInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Ingredientes del plato 10'}),

            'precio1_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del plato 1'}),
            'precio2_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del plato 2'}),
            'precio3_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del plato 3'}),
            'precio4_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del plato 4'}),
            'precio5_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del plato 5'}),
            'precio6_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del plato 6'}),
            'precio7_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del plato 7'}),
            'precio8_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del plato 8'}),
            'precio9_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del plato 9'}),
            'precio10_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del plato 10'}),


            # Campos de archivo (TODOS configurados de manera uniforme)
            'imagen_logo_empresa': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_fondo_header': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            #'imagen_header': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
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
            'nombre_servicio10_tarifa':forms.TextInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Nombre del servicio 10'}),

            'precio_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 1'}),
            'precio_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 2'}),
            'precio_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 3'}),
            'precio_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 4'}),
            'precio_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 5'}),
            'precio_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 6'}),
            'precio_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 7'}),
            'precio_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 8'}),
            'precio_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 9'}),
            'precio_servicio10_tarifa': forms.TextInput(attrs={'class':'form-control form-control-lg border-success', 'placeholder': 'Precio del servicio 10'}),
            
            'comentarios_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),

            'parrafo1_comentario': forms.Textarea(attrs={'class':'form-control form-control-lg border-success','rows': 4,'placeholder':'Párrafo comentario 1'}),
            'parrafo2_comentario': forms.Textarea(attrs={'class':'form-control form-control-lg border-success','rows': 4,'placeholder':'Párrafo comentario 2'}),
            'parrafo3_comentario': forms.Textarea(attrs={'class':'form-control form-control-lg border-success','rows': 4,'placeholder':'Párrafo comentario 3'}),
            'nombre1_comentario': forms.TextInput(attrs={'class':'form-control form-control-lg border-success','placeholder':'Nombre de la persona que hace el comentario 1'}),
            'nombre2_comentario': forms.TextInput(attrs={'class':'form-control form-control-lg border-success','placeholder':'Nombre de la persona que hace el comentario 2'}),
            'nombre3_comentario': forms.TextInput(attrs={'class':'form-control form-control-lg border-success','placeholder':'Nombre de la persona que hace el comentario 3'}),
            'imagen1_comentario': forms.ClearableFileInput(attrs={'class':'form-control form-control-lg border-success','placeholder':'Selecciona una imagen para el comentario 1'}),
            'imagen2_comentario': forms.ClearableFileInput(attrs={'class':'form-control form-control-lg border-success','placeholder':'Selecciona una imagen para el comentario 2'}),
            'imagen3_comentario': forms.ClearableFileInput(attrs={'class':'form-control form-control-lg border-success','placeholder':'Selecciona una imagen para el comentario 3'}),



            'chefs_activo': forms.Select(attrs={'class': 'form-select form-select-lg border-success'},choices=[('SI', 'Sí'),('NO', 'No'),('DK', 'Desconocido')]),

            'imagen_chef1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Selecciona una imagen para el Chef 1'}),
            'imagen_chef2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Selecciona una imagen para el Chef 2'}),
            'imagen_chef3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Selecciona una imagen para el Chef 3'}),
            
            'nombre_chef1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Nombre del Chef 1'}),
            'nombre_chef2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Nombre del Chef 2'}),
            'nombre_chef3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Nombre del Chef 3'}),

            'reservar_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]
        ),

            'titulo_servicios': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título para describir servicios'}),

            'imagen_servicio1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio4': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),

            'nombre_servicio1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 1'}),
            'nombre_servicio2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 2'}),
            'nombre_servicio3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 3'}),
            'nombre_servicio4': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 4'}),

            'parrafo_servicios1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 1'}),
            'parrafo_servicios2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 2'}),
            'parrafo_servicios3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 3'}),
            'parrafo_servicios4': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Párrafo para describir servicio 4'}),


            # Widgets para Título y Galería
            'galeria_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]
        ),
            'eventos_activo': forms.Select(attrs={'class': 'form-select form-select-lg border-success'},choices=[ ('SI', 'Sí'),('NO', 'No'),('DK', 'Desconocido')]),

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
            'imagen_portada': forms.ClearableFileInput(attrs={'class':'form-control form-control-lg border-success'}),
            'imagen_portada_reserva': forms.ClearableFileInput(attrs={'class':'form-control form-control-lg border-success','placeholder': 'Selecciona una imagen para la portada de reservas'}),
  
            # Campos de selección
            'tipo_empresa': forms.Select(attrs={'class': 'form-select form-select-lg border-success'}),
            #mapa de ubicasion
            'titulo_ubicacion_mapa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese el parrafo sbre la seccion del mapa'}),


            'contactar_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[('SI', 'Sí'),('NO', 'No'),('DK', 'Desconocido')]),

            'direccion': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Dirección completa'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Recuerde agregar el dígito de su teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Correo electrónico'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Latitud'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Longitud'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-co    #producto servicio y su tarifa 5ntrol-lg border-success', 'placeholder': 'Escrib el nombre de la url sin espacios'}),
            
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
            'nombre_de_la_empresa', 'nombreUrl', 'titulo_header', 'subtitulo1_header', 'subtitulo2_header', 
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
            'ciudad','direccion', 'telefono', 'email', 
            'latitud', 'longitud', 'tipo_empresa',
        ]

        widgets = {
            'nombre_de_la_empresa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la empresa'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'introduzca el nombre de la url sin espacios'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            'imagen_logo_empresa': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_fondo_header': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'titulo_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título del header'}),
            'subtitulo1_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Subtítulo 1 del header'}),
            'subtitulo2_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Subtítulo 2 del header'}),
            #sellecioinar el tipo de empresa
            'tipo_empresa': forms.Select(attrs={'class': 'form-select form-select-lg border-success'}),
            #sobre nosotros
             #sobre nosotros
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
            'imagen1_nosotros': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_nosotros_fondo': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'comentarios_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]),

            'eventos_activo': forms.Select(
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
                    # Widgets para Título y Galería
            'galeria_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]
        ),
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
            'imagen2_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen3_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen4_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
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
            'contactar_activo': forms.Select(
            attrs={'class': 'form-select form-select-lg border-success'},
            choices=[
                ('SI', 'Sí'),
                ('NO', 'No'),
                ('DK', 'Desconocido')
            ]
        ),

            'horario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese el horario'}),
            'pais': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese el país de la empresa'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ingrese la ciudad'}),

            'direccion': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Dirección completa'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Teléfono de contacto'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Correo electrónico'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Slug único'}),



        }


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
                'nombre_de_la_empresa', 'nombreUrl', 'titulo_header', 'subtitulo1_header', 'subtitulo2_header', 
                'imagen_logo_empresa', 'imagen_fondo_header', 'imagen_header', 'video_header',
                'quienes_somos_activo', 'titulo_sobrenosotros', 'parrafo1_sobrenosotros', 
                'parrafo2_sobrenosotros', 'parrafo3_sobrenosotros', 'parrafo4_sobrenosotros', 
                'parrafo5_sobrenosotros', 'imagen1_nosotros', 'imagen2_nosotros_fondo', 'video_nosotros',
                'menu_regalo_activo', 'menu_oferta1', 'menu_oferta2', 'menu_oferta3',
                'clientes_activo', 'platos_menu_activo',
                'comentarios_activo', 'parrafo1_comentario', 'parrafo2_comentario', 'parrafo3_comentario',
                'nombre1_comentario', 'nombre2_comentario', 'nombre3_comentario', 'eventos_activo',
                'chefs_activo', 'reservar_activo', 'titulo_servicios', 
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
                'imagen4_galeria', 'imagen5_galeria', 'imagen6_galeria', 'imagen7_galeria', 
                'imagen8_galeria', 'imagen9_galeria', 'contactar_activo', 'horario', 'pais', 
                'ciudad','direccion', 'telefono', 'email', 
                'latitud', 'longitud', 'tipo_empresa',
            ]
        widgets = {

            # Campos de texto
            'nombre_de_la_empresa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la empresa'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'introduzca el nombre de la url sin espacios'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            
            'titulo_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Título del header'}),
            'subtitulo1_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Subtítulo 1 del header'}),
            'subtitulo2_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Subtítulo 2 del header'}),
            'video_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'URL del video del header'}),

            'direccion': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Dirección completa'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Teléfono de contacto'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Correo electrónico'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            
            

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
            'menu_regalo_activo': forms.Select( attrs={'class': 'form-select form-select-lg border-success'},choices=[('SI', 'Sí'),('NO', 'No'), ('DK', 'Desconocido')]),

            'menu_oferta1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Detalle de la oferta del menú 1'}),
            'menu_oferta2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Detalle de la oferta del menú 2'}),
            'menu_oferta3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Detalle de la oferta del menú 3'}),
            'clientes_activo': forms.Select(attrs={'class': 'form-select form-select-lg border-success'},choices=[('SI', 'Sí'),('NO', 'No'),('DK', 'Desconocido')]),

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
            'nombre_servicio10_tarifa':forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre del servicio 10'}),
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
                'nombre_de_la_empresa', 'nombreUrl', 'titulo_header', 'imagen_logo_empresa', 'imagen_fondo_header',
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
                'telefono', 'email', 'latitud', 'longitud', 'tipo_empresa',
            ]

        widgets = {

            # Campos de texto
            'nombre_de_la_empresa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Nombre de la empresa'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Introduzca el nombre de url sin espacios'}),

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
            'imagen_portada': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Imagen para el fondo de reserva'}),

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
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
           
            
        }