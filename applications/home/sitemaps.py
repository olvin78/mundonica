from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Empresa


class EmpresaSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Empresa.objects.filter(estado_publicacion='published').exclude(nombreUrl__isnull=True).exclude(nombreUrl='')

    def location(self, obj):
        return reverse('home_app:empresa_detalle', kwargs={'nombreUrl': obj.nombreUrl})

    def lastmod(self, obj):
        return obj.fecha_actualizacion
