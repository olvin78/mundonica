from .models import SeccionMenu, Empresa, Abogado


def menu_activo(request):
    """Disponible en TODAS las plantillas (base.html se usa en todo el sitio).

    Uso en template: {% if 'recetas' in menu_activo %}...{% endif %}
    Si la tabla todavía no tiene filas (antes de correr las migraciones/seed),
    no se oculta nada por defecto para no romper el menú.
    """
    claves_activas = set(
        SeccionMenu.objects.filter(activo=True).values_list('clave', flat=True)
    )
    context = {}
    if not claves_activas and not SeccionMenu.objects.exists():
        context['menu_activo'] = {clave for clave, _ in SeccionMenu.CLAVES}
    else:
        context['menu_activo'] = claves_activas

    # Datos del perfil de usuario globales para el menú dropdown de base.html
    if request.user.is_authenticated:
        context['empresasDeUsuario'] = Empresa.objects.filter(propietario_sitio_web=request.user)
        try:
            abogado = Abogado.objects.get(id=request.user.id)
            context['user_abogado_id'] = abogado.id
        except Abogado.DoesNotExist:
            context['user_abogado_id'] = None
    else:
        context['empresasDeUsuario'] = []
        context['user_abogado_id'] = None

    return context

