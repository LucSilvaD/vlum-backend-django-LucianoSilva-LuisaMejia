"""
URL configuration for vlum_project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from oauth2_provider import urls as oauth2_urls
from vlum.views import api_root

handler404 = 'vlum.views.custom_404'

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('o/', include(oauth2_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
