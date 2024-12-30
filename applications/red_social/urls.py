from os import name
from django.urls import include, path
from . import views
from django.conf.urls import handler404



app_name = 'red_social_app'

handler404 ='applications.red_social.views.custom_404'

urlpatterns = [
    path('',
        views.RedSocialListView.as_view(),
        name='red_social',
    ),
];
