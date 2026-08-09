from django import template

register = template.Library()


@register.filter
def valoracion_estrellas(rating):
    """Devuelve el número de estrellas llenas (redondeo a la mitad superior).

    Ejemplos: 0 -> 0, 3.2 -> 3, 4.5 -> 5, 5 -> 5.
    """
    try:
        valor = float(rating)
    except (TypeError, ValueError):
        return 0
    return max(0, min(5, int(valor + 0.5)))


@register.filter
def rating_stars_list(rating):
    """Devuelve una lista de 5 elementos indicando el tipo de estrella para cada posición.
    Valores posibles en la lista: 'fill', 'half', 'empty'.
    """
    try:
        val = float(rating)
    except (TypeError, ValueError):
        val = 0.0
    
    stars = []
    for i in range(1, 6):
        if val >= i:
            stars.append('fill')
        elif val >= i - 0.5:
            stars.append('half')
        else:
            stars.append('empty')
    return stars
