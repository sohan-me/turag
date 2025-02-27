from django.contrib import admin
from .models import *
from nested_admin import NestedModelAdmin, NestedTabularInline, NestedStackedInline
# Register your models here.

class RoomImageLineAdmin(NestedTabularInline):
	model = RoomImageLine
	extra = 4
	can_delete = True


class AmenitiesAdmin(NestedTabularInline):
	model = Amenities
	extra = 2


class ComplementaryAdmin(NestedTabularInline):
	model = Complementary
	extra = 2


@admin.register(Room)
class RoomAdmin(NestedModelAdmin):
	list_display = ['id', 'title', 'cost', 'type', 'tags', 'is_available']
	list_display_links = ['title']
	list_filter = ['type', 'is_available']

	inlines = [RoomImageLineAdmin, AmenitiesAdmin, ComplementaryAdmin]


class ActivityImageLineAdmin(NestedTabularInline):
	model = ActivityImageLine
	extra = 4
	can_delete = True



@admin.register(Activity)
class ActivityAdmin(NestedModelAdmin):
	list_display = ['id', 'title', 'type', 'tags']
	list_display_links = ['title']
	list_filter = ['type']

	inlines = [ActivityImageLineAdmin]



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	list_display = ['id', 'room', 'email', 'phone', 'full_name', 'check_in', 'check_out', 'status']
	list_display_links = ['id', 'email', 'phone']
	list_filter = ['status']
	search_fields = ['email', 'phone', 'full_name']