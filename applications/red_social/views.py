from django.shortcuts import render
from typing import Any

from django.core.mail import send_mail
from django.http import HttpResponse

from django.db.models.query import QuerySet
from django.contrib.auth.mixins import LoginRequiredMixin
from applications.home.models import Consulado,Embajada,Abogado,Blog,Empresa,Post
from django.contrib.auth.models import User
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView
)


class RedSocialListView(ListView):
    template_name = "red_social/index.html"
    model = Post
    context_object_name = 'datos'

    def get_queryset(self):
        # Retorna el queryset original para los posts
        return super().get_queryset().order_by('-id')

    def get_context_data(self, **kwargs):
        # Obtén el contexto base de la clase ListView
        context = super().get_context_data(**kwargs)
        
        # Agrega los datos de la tabla User al contexto
        context['usuarios'] = User.objects.all().order_by('-date_joined')[:5]
        
        return context
