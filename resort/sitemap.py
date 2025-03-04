from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Room, Activity, Gallery


class RoomSitemap(Sitemap):
    changefreq = "weekly"  # How often the page is likely to change
    priority = 0.9  # Priority of this page (0.0 to 1.0)

    def items(self):
        return Room.objects.filter(is_available=True)  # Only include available rooms

    def location(self, obj):
        return f'/rooms/{obj.slug}/'  # URL for each room

    def lastmod(self, obj):
        return obj.updated_at  # Last modification date

class ActivitySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Activity.objects.all()

    def location(self, obj):
        return f'/activities/{obj.slug}/'

    def lastmod(self, obj):
        return obj.updated_at



# class GallerySitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.7

#     def items(self):
#         return Gallery.objects.all()

#     def location(self, obj):
#         return reverse('gallery_detail', kwargs={'pk': obj.pk}) #replace gallery_detail with your url name, and pk with the appropriate unique identifier.

# class StaticViewSitemap(Sitemap):
#     priority = 0.6
#     changefreq = 'monthly'

#     def items(self):
#         return ['home', 'contact'] #replace home and contact with your static view names.

#     def location(self, item):
#         return reverse(item)