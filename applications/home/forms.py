from django import forms
from .models import Abogado,Empresa
from django import forms
from django_recaptcha.fields import ReCaptchaField

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()

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
            'descripcion', 'resumen', 'verificado', 'asesoriajuridicageneral',
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
            'verificado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
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

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nombre', 'subtitulo', 'descripcion', 'imagen_header', 'video_header',
            'quienes_somos_activo', 'parrafo1', 'parrafo2', 'parrafo3', 'parrafo4', 'parrafo5',
            'imagen_nosotros', 'imagen_nosotros_fondo', 'video_nosotros', 'menu_regalo_activo',
            'menu_oferta1', 'menu_oferta2', 'menu_oferta3', 'clientes_activo', 'platos_menu_activo',
            'plato_menu1', 'plato_menu2', 'plato_menu3', 'plato_menu4', 'plato_menu5', 'plato_menu6',
            'comentarios_activo', 'eventos_activo', 'chefs_activo', 'reservar_activo',
            'galeria_activo', 'imagen_galeria1', 'imagen_galeria2', 'imagen_galeria3', 'imagen_galeria4',
            'imagen_galeria5', 'imagen_galeria6', 'imagen_galeria7', 'imagen_galeria8',
            'contactar_activo', 'horario', 'pais', 'ciudad', 'imagen', 'imagen_portada',
            'direccion', 'telefono', 'email', 'latitud', 'longitud', 'tipo_empresa'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la empresa'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el subtítulo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción breve'}),
            'imagen_header': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video_header': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL del video del header'}),
            'parrafo1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Párrafo descriptivo'}),
            'parrafo2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Párrafo descriptivo'}),
            'parrafo3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Párrafo descriptivo'}),
            'parrafo4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Párrafo descriptivo'}),
            'parrafo5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Párrafo descriptivo'}),
            'imagen_nosotros': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagen_nosotros_fondo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video_nosotros': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL del video de nosotros'}),
            'menu_oferta1': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Oferta 1'}),
            'menu_oferta2': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Oferta 2'}),
            'menu_oferta3': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Oferta 3'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'País de la empresa'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad de la empresa'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagen_portada': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Dirección completa'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitud'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Longitud'}),
            'tipo_empresa': forms.Select(attrs={'class': 'form-select'}),
        }

