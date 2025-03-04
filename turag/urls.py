"""
URL configuration for turag project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib.sitemaps.views import sitemap
from resort.sitemap import RoomSitemap, ActivitySitemap, GallerySitemap, SocialSitemap, BlogSitemap

# Define the sitemaps dictionary
sitemaps = {
    'rooms': RoomSitemap,
    'activities': ActivitySitemap,
    'gallery': GallerySitemap,
    'social': SocialSitemap,
    'blog': BlogSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('resort.urls')),
    path('tinymce/', include('tinymce.urls')),

    # DRF-Spectacular Schema UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Sitemaps url path
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='views.sitemap'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
