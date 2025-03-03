from django.contrib import admin
from .models import *
from nested_admin import NestedModelAdmin, NestedTabularInline, NestedStackedInline
# Register your models here.

class RoomImageLineAdmin(NestedStackedInline):
	model = RoomImageLine
	extra = 4
	can_delete = True


@admin.register(Amenities)
class AmenitiesAdmin(admin.ModelAdmin):
	list_display = ['id', 'icon', 'title']


@admin.register(Complementary)
class ComplementaryAdmin(admin.ModelAdmin):
	list_display = ['id', 'icon', 'title']


@admin.register(Room)
class RoomAdmin(NestedModelAdmin):
	list_display = ['id', 'title', 'cost', 'type', 'venue', 'tags', 'is_available']
	list_display_links = ['title']
	list_filter = ['type', 'is_available', 'venue']
	prepopulated_fields = {'slug': ('title', )}

	inlines = [RoomImageLineAdmin]


class ActivityImageLineAdmin(NestedTabularInline):
	model = ActivityImageLine
	extra = 4
	can_delete = True



@admin.register(Activity)
class ActivityAdmin(NestedModelAdmin):
	list_display = ['id', 'title', 'type', 'venue', 'tags']
	list_display_links = ['title']
	list_filter = ['type', 'venue']
	prepopulated_fields = {'slug': ('title', )}

	inlines = [ActivityImageLineAdmin]



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	list_display = ['id', 'room', 'email', 'phone', 'full_name', 'check_in', 'check_out', 'status']
	list_display_links = ['id', 'email', 'phone']
	list_filter = ['status']
	search_fields = ['email', 'phone', 'full_name']



@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
	list_display = ['id', 'facebook', 'linkedin', 'instagram', 'youtube', 'tiktok', 'pinterest', 'whatsapp', 'twitter']



@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
	list_display = ['type', 'image', 'description']
	list_display_links = ['type', 'image', 'description']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ['full_name', 'email', 'phone', 'subject', 'mark_as_read']
	list_display_links = ['full_name', 'email', 'phone', 'subject']
	list_editable = ['mark_as_read']
	search_fields = ['email', 'phone', 'full_name']
	list_filter = ['mark_as_read']