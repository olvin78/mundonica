
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf.urls.static import static,settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')),
    path('red_social/', include('applications.red_social.urls')),
    path('accounts/', include('allauth.urls')),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


