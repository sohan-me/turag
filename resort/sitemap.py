from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Room, Activity, Gallery, Social, Contact, Blog

#Sitemap for Blog model
class BlogSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Blog.objects.all()

    def location(self, obj):
        return reverse('blog-detail', args=[obj.slug])

# Sitemap for Room model
class RoomSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Room.objects.filter(is_available=True)  # Only include available rooms

    def location(self, obj):
        return reverse('room-detail', args=[obj.slug]) 

# Sitemap for Activity model
class ActivitySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Activity.objects.all()

    def location(self, obj):
        return reverse('activity-detail', args=[obj.slug]) 

# Sitemap for Gallery model
class GallerySitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Gallery.objects.all()

    def location(self, obj):
        return reverse('gallery-list') 

# Sitemap for Social model
class SocialSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5

    def items(self):
        return Social.objects.all()

    def location(self, obj):
        return reverse('social-list') 

