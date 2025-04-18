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


class ActivityImageLineAdmin(NestedStackedInline):
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


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):

	list_display = ['id', 'type', 'extra_cost']
	list_display_links = ['id', 'type', 'extra_cost']
	list_filter = ['type']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	list_display = ['id', 'room', 'plan_type', 'email', 'phone', 'full_name', 'check_in', 'check_out', 'status']
	list_display_links = ['id', 'email', 'phone']
	list_filter = ['status']
	search_fields = ['email', 'phone', 'full_name']



@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
	list_display = ['id', 'facebook', 'linkedin', 'instagram', 'youtube', 'tiktok', 'pinterest', 'whatsapp', 'twitter']

	def has_add_permission(self, request):
		if self.model.objects.exists():
			return False
		return super().has_add_permission(request)



@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
	list_display = ['type', 'image', 'alt_text', 'venue', 'description']
	list_display_links = ['type', 'image', 'description']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ['full_name', 'email', 'phone', 'subject', 'mark_as_read']
	list_display_links = ['full_name', 'email', 'phone', 'subject']
	list_editable = ['mark_as_read']
	search_fields = ['email', 'phone', 'full_name']
	list_filter = ['mark_as_read']



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'slug', 'alt_text', 'tags', 'created_at']
	list_display_links = ['id', 'title']
	prepopulated_fields = {'slug': ('title', )}




@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
	list_display = ['id', 'booking', 'payment_method', 'trans_id', 'amount', 'is_approved']
	list_display_links = ['id', 'booking', 'payment_method', 'trans_id']
	list_filter = ['is_approved', 'payment_method']
	search_fields = ['trans_id']



@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
	list_display = ['id', 'method_name', 'account_no', 'account_type', 'ifsc_code']
	list_display_links = ['id', 'method_name', 'account_no']



@admin.register(VenueInfo)
class VenueInfoAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'venue', 'youtube_url']
	list_display_links = ['id', 'title', 'venue']
