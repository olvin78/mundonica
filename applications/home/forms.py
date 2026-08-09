from django import forms
from .models import Abogado,Empresa,Receta
from .models import Perfil
from django.utils.html import strip_tags


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
            'header_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'servicios_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'trabajadores_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tarifa_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

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
            'header_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'servicios_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'trabajadores_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tarifa_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

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
            'imagen_header','video_header',
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
        'header_activo', 'servicios_activo', 'trabajadores_activo', 'tarifa_activo']

        widgets = {
            'header_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'servicios_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'trabajadores_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tarifa_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),


            # Campos de texto
            'nombre_de_la_empresa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Restaurante La Cazuela'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: restaurante-la-cazuela'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            'titulo_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Disfruta de la mejor comida casera'}),
            'subtitulo1_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Platos tradicionales con ingredientes frescos'}),
            'subtitulo2_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Sabores que enamoran'}),
            'imagen_header': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'video_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'URL del video del header'}),

            'quienes_somos_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'titulo_sobrenosotros': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Más de 15 años de experiencia'}),
            'parrafo1_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: En La Cazuela cocinamos recetas tradicionales con productos frescos de temporada.'}),
            'parrafo2_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: Nuestro equipo elabora cada plato al momento para que disfrutes de todo el sabor.'}),
            'parrafo3_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: Trabajamos con productores locales para ofrecerte la mejor calidad.'}),
            'parrafo4_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: Ambiente acogedor, atención cercana y precios justos.'}),
            'parrafo5_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: Ven y comprueba por qué somos el restaurante favorito de la ciudad.'}),
            'imagen1_nosotros': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_nosotros_fondo': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'video_nosotros': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'URL del Video Sobre Nosotros'}),

            #campo de los platos 
            'menu_regalo_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'menu_oferta1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Menú degustación para una persona con entrada, plato principal y postre.'}),
            'menu_oferta2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Menú especial para parejas con maridaje incluido.'}),
            'menu_oferta3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Cena completa para cuatro personas con bebidas.'}),

            'clientes_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'platos_menu_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'nombre1_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Ternera Estofada'}),
            'nombre2_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Pollo al Horno'}),
            'nombre3_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Sopa de Mariscos'}),
            'nombre4_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Pescado a la Plancha'}),
            'nombre5_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Gallo Pinto'}),
            'nombre6_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Indio Viejo'}),
            'nombre7_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Vigoron'}),
            'nombre8_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Baho'}),
            'nombre9_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Nacatamal'}),
            'nombre10_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Postre Casero'}),

            'imagen1_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del plato 1'}),
            'imagen2_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del plato 2'}),
            'imagen3_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del plato 3'}),
            'imagen4_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del plato 4'}),
            'imagen5_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del plato 5'}),
            'imagen6_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del plato 6'}),
            'imagen7_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del plato 7'}),
            'imagen8_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del plato 8'}),
            'imagen9_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del plato 9'}),
            'imagen10_plato_menu': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del plato 10'}),

            'descriptcion1_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Ternera cocinada a fuego lento con verduras y especias.'}),
            'descriptcion2_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Pollo jugoso al horno con guarnición y ensalada.'}),
            'descriptcion3_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Sopa de mariscos frescos con sabor a mar.'}),
            'descriptcion4_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Pescado fresco a la plancha con limón y vegetales.'}),
            'descriptcion5_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: El desayuno tradicional nica con arroz y frijoles.'}),
            'descriptcion6_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Plato típico nicaragüense de maíz y carne.'}),
            'descriptcion7_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Chicharrón con yuca y ensalada de repollo.'}),
            'descriptcion8_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Carne, plátano y yuca cocinados al vapor.'}),
            'descriptcion9_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Tamal de maíz relleno de cerdo y arroz.'}),
            'descriptcion10_plato_menu':forms.TextInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Ej: Postre casero del día, pregunta al mesero'}),

            'precio1_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 12.50'}),
            'precio2_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 9.00'}),
            'precio3_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 10.00'}),
            'precio4_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 11.00'}),
            'precio5_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 5.00'}),
            'precio6_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 8.00'}),
            'precio7_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 6.00'}),
            'precio8_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 7.00'}),
            'precio9_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 6.50'}),
            'precio10_plato_menu': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 3.50'}),


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
            'titulo_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Nuestros precios'}),

            'imagen_tarifa1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_tarifa2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),

            'nombre_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Menú Ejecutivo'}),
            'nombre_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Plato del Día'}),
            'nombre_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Menú Infantil'}),
            'nombre_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Menú Parejas'}),
            'nombre_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Carta a la Carta'}),
            'nombre_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Menú Degustación'}),
            'nombre_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Menú Celiacos'}),
            'nombre_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Postre Casero'}),
            'nombre_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Bebida'}),
            'nombre_servicio10_tarifa':forms.TextInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Ej: Café'}),

            'precio_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 12'}),
            'precio_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 9'}),
            'precio_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 7'}),
            'precio_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 22'}),
            'precio_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 15'}),
            'precio_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 28'}),
            'precio_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 13'}),
            'precio_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 4'}),
            'precio_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 2.5'}),
            'precio_servicio10_tarifa': forms.TextInput(attrs={'class':'form-control form-control-lg border-success', 'placeholder': 'Ej: 1.5'}),
            
            'comentarios_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'parrafo1_comentario': forms.Textarea(attrs={'class':'form-control form-control-lg border-success','rows': 4,'placeholder':'Ej: La comida está deliciosa, parece comida de casa. Volveré seguro.'}),
            'parrafo2_comentario': forms.Textarea(attrs={'class':'form-control form-control-lg border-success','rows': 4,'placeholder':'Ej: El mejor restaurante de la zona, atención excelente y precios justos.'}),
            'parrafo3_comentario': forms.Textarea(attrs={'class':'form-control form-control-lg border-success','rows': 4,'placeholder':'Ej: Recomendado al 100%. El menú del día es una maravilla.'}),
            'nombre1_comentario': forms.TextInput(attrs={'class':'form-control form-control-lg border-success','placeholder':'Ej: Laura Gómez'}),
            'nombre2_comentario': forms.TextInput(attrs={'class':'form-control form-control-lg border-success','placeholder':'Ej: Miguel Torres'}),
            'nombre3_comentario': forms.TextInput(attrs={'class':'form-control form-control-lg border-success','placeholder':'Ej: Ana Ruiz'}),
            'imagen1_comentario': forms.ClearableFileInput(attrs={'class':'form-control form-control-lg border-success','placeholder':'Selecciona una imagen para el comentario 1'}),
            'imagen2_comentario': forms.ClearableFileInput(attrs={'class':'form-control form-control-lg border-success','placeholder':'Selecciona una imagen para el comentario 2'}),
            'imagen3_comentario': forms.ClearableFileInput(attrs={'class':'form-control form-control-lg border-success','placeholder':'Selecciona una imagen para el comentario 3'}),



            'chefs_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'imagen_chef1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Selecciona una imagen para el Chef 1'}),
            'imagen_chef2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Selecciona una imagen para el Chef 2'}),
            'imagen_chef3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Selecciona una imagen para el Chef 3'}),
            
            'nombre_chef1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Ej: Chef María López'}),
            'nombre_chef2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Ej: Chef José Ramírez'}),
            'nombre_chef3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success','placeholder': 'Ej: Chef Carlos Mendoza'}),

            'reservar_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'titulo_servicios': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Los mejores platos que te ofrecemos'}),

            'imagen_servicio1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio4': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),

            'nombre_servicio1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Cocina Tradicional'}),
            'nombre_servicio2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Comida Rápida Casera'}),
            'nombre_servicio3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Menú del Día'}),
            'nombre_servicio4': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Servicio a Domicilio'}),

            'parrafo_servicios1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Platos de toda la vida elaborados con recetas de la abuela.'}),
            'parrafo_servicios2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Hamburguesas y bocadillos hechos al momento.'}),
            'parrafo_servicios3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Menú completo con entrada, principal y postre.'}),
            'parrafo_servicios4': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Recibimos tus pedidos y te lo llevamos a casa.'}),


            # Widgets para Título y Galería
            'galeria_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'eventos_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'titulo1_galeria': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Algunas imágenes de nuestro restaurante'}),
            'imagen1_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen3_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen4_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen5_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen6_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen7_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen8_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),

            'horario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Lunes a Domingo, 11:00 am - 9:00 pm'}),
            'pais': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Nicaragua'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Managua'}),
            'imagen_portada': forms.ClearableFileInput(attrs={'class':'form-control form-control-lg border-success'}),
            'imagen_portada_reserva': forms.ClearableFileInput(attrs={'class':'form-control form-control-lg border-success','placeholder': 'Selecciona una imagen para la portada de reservas'}),
  
            # Campos de selección
            'tipo_empresa': forms.Select(attrs={'class': 'form-select form-select-lg border-success'}),
            #mapa de ubicasion
            'titulo_ubicacion_mapa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Encuéntranos en el centro de la ciudad'}),


            'contactar_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'direccion': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Del costado norte del parque, 1 cuadra al este'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: +505 8888 0000'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Correo electrónico'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Latitud'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Longitud'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: restaurante-la-cazuela'}),
            
        }


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'telefono',  # Incluye el campo telefono en el formulario
            'avatar'
        ]

        widgets = {
            'header_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'servicios_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'trabajadores_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tarifa_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'})  # Asegúrate de tener el estilo adecuado
        }


class PeluqueriaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nombre_de_la_empresa', 'nombreUrl', 'titulo_header', 'subtitulo1_header', 'subtitulo2_header', 
            'imagen_fondo_header','quienes_somos_activo', 'titulo_sobrenosotros', 'parrafo1_sobrenosotros', 
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
        'header_activo', 'servicios_activo', 'trabajadores_activo', 'tarifa_activo']

        widgets = {
            'header_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'servicios_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'trabajadores_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tarifa_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'nombre_de_la_empresa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Barbería Patrick Porter'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: barberia-patrick-porter'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            'imagen_fondo_header': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'titulo_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Cortes que te hacen lucir elegante'}),
            'subtitulo1_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Con Patrick Porter'}),
            'subtitulo2_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Siéntete más seguro'}),
            #sellecioinar el tipo de empresa
            'tipo_empresa': forms.Select(attrs={'class': 'form-select form-select-lg border-success'}),
            #sobre nosotros
             #sobre nosotros
            'quienes_somos_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'titulo_sobrenosotros': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Más de 10 años de experiencia'}),
            'parrafo1_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: En Patrick Porter ofrecemos cortes de cabello y barba con los mejores profesionales.'}),
            'parrafo2_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: Nuestro equipo te asesora para que salgas con el look perfecto.'}),
            'parrafo3_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: Usamos productos de alta calidad y técnicas actualizadas.'}),
            'imagen1_nosotros': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_nosotros_fondo': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'comentarios_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'eventos_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'reservar_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                    # Widgets para Título y Galería
            'galeria_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            #servicios
            'titulo_servicios': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Los mejores servicios que te ofrecemos'}),
            'imagen_servicio1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'nombre_servicio1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Corte Clásico'}),
            'nombre_servicio2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Corte Moderno'}),
            'nombre_servicio3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Arreglo de Barba'}),
            'parrafo_servicios1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Corte tradicional con tijera y máquina, lavado incluido.'}),
            'parrafo_servicios2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Estilos actuales con degradado, para que luzcas moderno.'}),
            'parrafo_servicios3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Perfilado y afeitado de barba con productos premium.'}),
            #trabajadores
            'titulo_trabajadores': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Nuestro equipo de barberos para ti'}),
            'imagen_trabajador1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'nombre_trabajador1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Patrick Porter'}),
            'nombre_trabajador2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Carlos Ruiz'}),
            'nombre_trabajador3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Miguel Flores'}),
            # Widgets para las tarifas
            'titulo_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Nuestros precios'}),
            'imagen_tarifa1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_tarifa2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'nombre_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Corte de Cabello'}),
            'nombre_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Corte + Barba'}),
            'nombre_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Afeitado Clásico'}),
            'nombre_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Tinte de Cabello'}),
            'nombre_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Corte Infantil'}),
            'nombre_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Diseño de Cejas'}),
            'nombre_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Tratamiento Capilar'}),
            'nombre_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Mascarilla Facial'}),
            'nombre_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Alisado'}),
            'nombre_servicio10_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Corte a Domicilio'}),
            'precio_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 5'}),
            'precio_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 8'}),
            'precio_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 4'}),
            'precio_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 15'}),
            'precio_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 4'}),
            'precio_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 2'}),
            'precio_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 10'}),
            'precio_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 6'}),
            'precio_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 20'}),
            'precio_servicio10_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 10'}),
            #galeria
            'titulo1_galeria': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Algunos de nuestros cortes'}),
            'imagen1_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen3_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen4_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            #comentario
            'parrafo1_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: El mejor corte de mi vida, atención excelente.'}),
            'parrafo2_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Ambiente agradable y barberos muy profesionales.'}),
            'parrafo3_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Sali con el look perfecto, súper recomendado.'}),
            'nombre1_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Juan Pérez'}),
            'nombre2_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Roberto Díaz'}),
            'nombre3_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Andrés López'}),

            #mapa de ubicasion
            'titulo_ubicacion_mapa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Encuéntranos en el barrio de siempre'}),
            'subtitulo_ubicacion_mapa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Ven y conoce nuestras instalaciones'}),
            #contacto
            'contactar_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'horario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Martes a Domingo, 9:00 am - 7:00 pm'}),
            'pais': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Nicaragua'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Managua'}),

            'direccion': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: De la Rotonda, 2 cuadras al sur'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: +505 8888 1111'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Correo electrónico'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: barberia-patrick-porter'}),



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
            'header_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'servicios_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'trabajadores_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tarifa_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),


            # Campos de texto
            'nombre_de_la_empresa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Tienda Mundo Nica'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: tienda-mundo-nica'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            
            'titulo_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Encuentra todo lo que necesitas'}),
            'subtitulo1_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Productos de calidad al mejor precio'}),
            'subtitulo2_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Tu tienda de confianza'}),
            'video_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'URL del video del header'}),

            'direccion': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Del costado este del mall, 1 cuadra al norte'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: +505 8888 2222'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Correo electrónico'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            
            

            'nombre_servicio1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Ropa y Moda'}),
            'nombre_servicio2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Electrónica'}),
            'nombre_servicio3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Hogar y Decoración'}),
            'parrafo_servicios1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Prendas actuales para toda la familia con las mejores marcas.'}),
            'parrafo_servicios2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Equipos y accesorios tecnológicos con garantía.'}),
            'parrafo_servicios3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Todo para tu casa con estilos modernos y funcionales.'}),

            'quienes_somos_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'titulo_sobrenosotros': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Más de 20 años de experiencia'}),
            'parrafo1_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: En Tienda Mundo Nica ofrecemos la mejor relación calidad-precio.'}),
            'parrafo2_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: Nuestro equipo te asesora para encontrar lo que buscas.'}),
            'parrafo3_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: Contamos con las mejores marcas y atención personalizada.'}),
            'parrafo4_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: Entrega rápida, garantía y facilidades de pago.'}),
            'parrafo5_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: Ven y comprueba por qué somos la tienda favorita de la ciudad.'}),
            'imagen1_nosotros': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_nosotros_fondo': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'video_nosotros': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'URL del Video Sobre Nosotros'}),

            #campo de los platos 
            'menu_regalo_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'menu_oferta1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Oferta 2x1 en toda la ropa de temporada.'}),
            'menu_oferta2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Descuento del 20% en electrónica seleccionada.'}),
            'menu_oferta3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Envío gratis en compras mayores a $50.'}),
            'clientes_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'platos_menu_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'plato_menu1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del producto 1'}),
            'plato_menu2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del producto 2'}),
            'plato_menu3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del producto 3'}),
            'plato_menu4': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del producto 4'}),
            'plato_menu5': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del producto 5'}),
            'plato_menu6': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona una imagen del producto 6'}),

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
            'titulo_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Nuestros precios'}),

            'imagen_tarifa1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_tarifa2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'nombre_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Ropa Premium'}),
            'nombre_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Zapatos'}),
            'nombre_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Accesorios'}),
            'nombre_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Tecnología'}),
            'nombre_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Decoración'}),
            'nombre_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Ropa Infantil'}),
            'nombre_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Perfumería'}),
            'nombre_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Ropa Deportiva'}),
            'nombre_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Bolsos'}),
            'nombre_servicio10_tarifa':forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Calzado Casual'}),
            'precio_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 25'}),
            'precio_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 35'}),
            'precio_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 10'}),
            'precio_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 50'}),
            'precio_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 15'}),
            'precio_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 18'}),
            'precio_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 22'}),
            'precio_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 30'}),
            'precio_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 28'}),
            'precio_servicio10_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 32'}),
            

            'comentarios_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'parrafo1_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Excelente atención y productos de gran calidad.'}),
            'parrafo2_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Todo lo que buscaba y a muy buen precio.'}),
            'parrafo3_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Buen servicio y variedad de productos.'}),
            'nombre1_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Pedro Salazar'}),
            'nombre2_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Marta Delgado'}),
            'nombre3_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Luis Vargas'}),
            
            'eventos_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'chefs_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'reservar_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            #trabajadores
            'titulo_trabajadores': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Nuestro equipo para ti'}),
            'imagen_trabajador1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_trabajador3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'nombre_trabajador1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Sofía Herrera'}),
            'nombre_trabajador2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Andrés Castro'}),
            'nombre_trabajador3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Lucía Navarro'}),

            'titulo_servicios': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Los mejores productos que te ofrecemos'}),
            'imagen_servicio1': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio2': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_servicio3': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'nombre_servicio1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Ropa y Moda'}),
            'nombre_servicio2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Electrónica'}),
            'nombre_servicio3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Hogar y Decoración'}),
            'parrafo_servicios1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Prendas actuales para toda la familia con las mejores marcas.'}),
            'parrafo_servicios2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Equipos y accesorios tecnológicos con garantía.'}),
            'parrafo_servicios3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Todo para tu casa con estilos modernos y funcionales.'}),


            # Widgets para Título y Galería
            'galeria_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'titulo1_galeria': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Algunas imágenes de nuestra tienda'}),
            'imagen1_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen3_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen4_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen5_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen6_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen7_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen8_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen9_galeria': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            
            'horario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Lunes a Sábado, 9:00 am - 7:00 pm'}),
            'pais': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Nicaragua'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Managua'}),

            # Campos de selección
            'tipo_empresa': forms.Select(attrs={'class': 'form-select form-select-lg border-success'}),
            #mapa de ubicasion
            'titulo_ubicacion_mapa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Encuéntranos en el centro comercial'}),


            'contactar_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            
        }


class ComercioForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
                'nombre_de_la_empresa', 'nombreUrl', 'titulo_header', 'subtitulo1_header', 'subtitulo2_header',
                'imagen_logo_empresa', 'imagen_fondo_header',
                'titulo_servicios', 'nombre_servicio1', 'parrafo_servicios1', 
                'nombre_servicio2', 'parrafo_servicios2', 'nombre_servicio3', 'parrafo_servicios3',
                'quienes_somos_activo', 'titulo_sobrenosotros', 'parrafo1_sobrenosotros', 'parrafo2_sobrenosotros', 
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
                'precio_servicio9_tarifa', 'precio_servicio10_tarifa',
                'galeria_activo', 'titulo1_galeria', 'imagen1_galeria', 'imagen2_galeria', 
                'imagen3_galeria', 'imagen4_galeria', 'imagen5_galeria', 'imagen6_galeria', 
                'imagen7_galeria', 'imagen8_galeria', 'imagen9_galeria', 'imagen10_galeria', 
                'contactar_activo', 'pais', 'ciudad', 'direccion',
                'telefono', 'email', 'horario', 'latitud', 'longitud', 'tipo_empresa',
            'header_activo', 'servicios_activo', 'trabajadores_activo', 'tarifa_activo']

        widgets = {
            'header_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'servicios_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'trabajadores_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tarifa_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),


            # Campos de texto
            'nombre_de_la_empresa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Tienda Mundo Nica'}),
            'nombreUrl': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: tienda-mundo-nica'}),

            'titulo_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Encuentra todo lo que necesitas'}),
            'subtitulo1_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Productos de calidad al mejor precio'}),
            'subtitulo2_header': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Tu tienda de confianza'}),
            # Campos de archivo (TODOS configurados de manera uniforme)
            'imagen_logo_empresa': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_fondo_header': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen_header': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            
            #servicio
            'titulo_servicios': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Los mejores productos que te ofrecemos'}),
            'nombre_servicio1': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Ropa y Moda'}),
            'nombre_servicio2': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Electrónica'}),
            'nombre_servicio3': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Hogar y Decoración'}),
            'parrafo_servicios1': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Prendas actuales para toda la familia con las mejores marcas.'}),
            'parrafo_servicios2': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Equipos y accesorios tecnológicos con garantía.'}),
            'parrafo_servicios3': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Todo para tu casa con estilos modernos y funcionales.'}),


            #sobre nosotros
            'quienes_somos_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'titulo_sobrenosotros': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Más de 20 años de experiencia'}),

            'parrafo1_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: En Tienda Mundo Nica ofrecemos la mejor relación calidad-precio.'}),
            'parrafo2_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: Nuestro equipo te asesora para encontrar lo que buscas.'}),
            'parrafo3_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: Contamos con las mejores marcas y atención personalizada.'}),
            'parrafo4_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: Entrega rápida, garantía y facilidades de pago.'}),
            'parrafo5_sobrenosotros': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 3, 'placeholder': 'Ej: Ven y comprueba por qué somos la tienda favorita de la ciudad.'}),
            
            'imagen1_nosotros': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            
            'imagen2_nosotros_fondo': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen3_nosotros': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'URL del Video Sobre Nosotros'}),
          

            # Widgets para las tarifas
            'nombre_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Ropa Premium'}),
            'nombre_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Zapatos'}),
            'nombre_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Accesorios'}),
            'nombre_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Tecnología'}),
            'nombre_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Decoración'}),
            'nombre_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Ropa Infantil'}),
            'nombre_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Perfumería'}),
            'nombre_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Ropa Deportiva'}),
            'nombre_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Bolsos'}),
            'nombre_servicio10_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Calzado Casual'}),
            
            'precio_servicio1_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 25'}),
            'precio_servicio2_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 35'}),
            'precio_servicio3_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 10'}),
            'precio_servicio4_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 50'}),
            'precio_servicio5_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 15'}),
            'precio_servicio6_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 18'}),
            'precio_servicio7_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 22'}),
            'precio_servicio8_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 30'}),
            'precio_servicio9_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 28'}),
            'precio_servicio10_tarifa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: 32'}),
            

            'comentarios_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nombre1_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Pedro Salazar'}),
            'nombre2_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Marta Delgado'}),
            'nombre3_comentario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Luis Vargas'}),
            'parrafo1_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Excelente atención y productos de gran calidad.'}),
            'parrafo2_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Todo lo que buscaba y a muy buen precio.'}),
            'parrafo3_comentario': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Buen servicio y variedad de productos.'}),
            'imagen1_comentario': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen2_comentario': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),
            'imagen3_comentario': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success'}),


            # Widgets para Título y Galería
            'galeria_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'titulo1_galeria': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Algunas imágenes de nuestros productos'}),
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
            
            'horario': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Lunes a Sábado, 9:00 am - 7:00 pm'}),
            'pais': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Nicaragua'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Managua'}),
            'titulo_ubicacion_mapa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Encuéntranos aquí'}),
            'imagen_portada': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Selecciona la imagen de fondo de reserva'}),

            # Campos de selección
            'tipo_empresa': forms.Select(attrs={'class': 'form-select form-select-lg border-success'}),
            #mapa de ubicasion
            'titulo_ubicacion_mapa': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: Encuéntranos en el centro comercial'}),


            'contactar_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'direccion': forms.Textarea(attrs={'class': 'form-control form-control-lg border-success', 'rows': 4, 'placeholder': 'Ej: Del costado este del mall, 1 cuadra al norte'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Ej: +505 8888 2222'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'Correo electrónico'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control form-control-lg border-success', 'placeholder': 'este campos se rrellenan automáticamente al hacer click en el mapa'}),
           
            
        }



class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'categoria', 'imagen', 'resumen', 'cuerpo']
        widgets = {
            'header_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'servicios_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'trabajadores_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tarifa_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),  # 🔹 Se convierte en <select>
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

    def clean_resumen(self):
        resumen = self.cleaned_data.get('resumen', '')
        return strip_tags(resumen)  # Elimina etiquetas HTML antes de guardar

    def clean_cuerpo(self):
        cuerpo = self.cleaned_data.get('cuerpo', '')
        return strip_tags(cuerpo)  # Elimina etiquetas HTML antes de guardar