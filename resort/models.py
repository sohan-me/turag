from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from tinymce.models import HTMLField
# Create your models here.



# Abstract model to increase code reusability
class TimeStamp(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True



# Amenities model
class Amenities(TimeStamp):
	icon = models.ImageField(upload_to='room/amenities/', null=True, blank=True)
	title = models.CharField(max_length=255)

	class Meta:
		verbose_name_plural = 'Amenities'

	def __str__(self):
		return self.title



# Complementary model
class Complementary(TimeStamp):
	icon = models.ImageField(upload_to='room/amenities/', null=True, blank=True)
	title = models.CharField(max_length=255)

	class Meta:
		verbose_name_plural = 'complementaries'
 
	def __str__(self):
		return self.title



# Model for Rooms
class Room(TimeStamp):
	TYPE = [
		('Cottage', 'Cottage'),
		('Suite', 'Suite'),
		('Villa', 'Villa'),
		('Duplex', 'Duplex'),
		('Lake View', 'Lake View'),
		('River View', 'River View'),
		('Deluxe', 'Deluxe'),

	]

	VENU = [
		('Dhaka', 'Dhaka'),
		('Gazipur', 'Gazipur'),
	]

	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True, blank=True)
	description = models.TextField()
	dynamic_image = models.ImageField(upload_to='room/dynamic_image/', null=True, blank=True)
	cost = models.DecimalField(max_digits=10, decimal_places=2)
	type = models.CharField(choices=TYPE, max_length=20)
	venue = models.CharField(choices=VENU, max_length=20)
	tags = models.CharField(max_length=300)
	amenities = models.ManyToManyField(Amenities, blank=True, related_name='room')
	complementary = models.ManyToManyField(Complementary, blank=True, related_name='room')
	is_available = models.BooleanField(default=True)

	def __str__(self):
		return self.title


# pre_save signal to create slug for room objects
@receiver(pre_save, sender=Room)
def assign_room_slug(sender, instance, **kwargs):
	if not instance.slug:
		slug = slugify(instance.title)
		unique_slug = slug
		flag = 1
		while Room.objects.filter(slug=unique_slug).exists():
			unique_slug = f'{slug}-{flag}'
			flag += 1
		instance.slug = unique_slug




# Image model to store room images
class RoomImageLine(models.Model):
	room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_image')
	image = models.ImageField(upload_to='room/images/')
	alt_text = models.CharField(max_length=100)
	is_featured = models.BooleanField(default=False)

	def __str__(self):
		return self.room.title




# Model for Activities
class Activity(TimeStamp):
	TYPE = [
		('Restaurant', 'Restaurant'),
		('Event', 'Event'),
		('Recreation', 'Recreation'),
		('Play Ground', 'Play Ground'),
		('Kids Zone', 'Kids Zone'),
		('Hall', 'Hall'),
		('Outdoor', 'Outdoor'),
	]

	VENU = [
		('Dhaka', 'Dhaka'),
		('Gazipur', 'Gazipur'),
	]

	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=260)
	slogan = models.CharField(max_length=300, null=True, blank=True)
	description = models.TextField()
	type = models.CharField(max_length=20, choices=TYPE)
	venue = models.CharField(choices=VENU, max_length=20)
	tags = models.CharField(max_length=300, null=True, blank=True)
	

	class Meta:
		verbose_name_plural = 'Activities'

	def __str__(self):
		return self.title


# pre_save signal to generate slug for activity objects
@receiver(pre_save, sender=Activity)
def assign_activity_slug(sender, instance, **kwargs):
	if not instance.slug:
		slug = slugify(instance.title)
		unique_slug = slug
		flag = 1
		while Activity.objects.filter(slug=unique_slug).exists():
			unique_slug = f'{slug}-{flag}'
			flag += 1
		instance.slug = unique_slug


# Image model to store activity images
class ActivityImageLine(models.Model):
	activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='activity_image')
	image = models.ImageField(upload_to='activity/images/')
	alt_text = models.CharField(max_length=100)
	is_featured = models.BooleanField(default=False)

	def __str__(self):
		return self.activity.title



# Model for storing Booking request
class Booking(TimeStamp):

	STATUS = [
		('Pending', 'Pending'),
		('Confirmed', 'Confirmed'),
		('Cancelled', 'Cancelled'),
	]

	room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
	full_name = models.CharField(max_length=150)
	email = models.EmailField(null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	adults = models.PositiveIntegerField()
	children = models.PositiveIntegerField()
	check_in = models.DateField()
	check_out = models.DateField()
	address = models.CharField(max_length=255, null=True, blank=True)
	remarks = models.CharField(max_length=255, null=True, blank=True)
	status = models.CharField(max_length=100, choices=STATUS, default='Pending')

	def __str__(self):
		return self.full_name



class Social(TimeStamp):

	facebook = models.URLField(max_length=300, null=True, blank=True)
	linkedin = models.URLField(max_length=300, null=True, blank=True)
	instagram = models.URLField(max_length=300, null=True, blank=True)
	youtube = models.URLField(max_length=300, null=True, blank=True)
	tiktok = models.URLField(max_length=300, null=True, blank=True)
	pinterest = models.URLField(max_length=300, null=True, blank=True)
	whatsapp = models.URLField(max_length=300, null=True, blank=True)
	twitter = models.URLField(max_length=300, null=True, blank=True)
	





class Gallery(TimeStamp):
	Type = [
		('Outdoor', 'Outdoor'),
		('Dining', 'Dining'),
		('Activities', 'Activities'),
		('Events', 'Events'),
		('Interior', 'Interior'),
		('Rooms', 'Rooms'),
	]

	type = models.CharField(choices=Type, max_length=20)
	image = models.ImageField(upload_to='gallery/')
	alt_text = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Galleries'

	def __str__(self):
		return self.type



# Model for storing user contact messages
class Contact(TimeStamp):

	full_name = models.CharField(max_length=55)
	email = models.EmailField(null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	subject = models.CharField(max_length=300, null=True, blank=True)
	comment = models.TextField(null=True, blank=True)
	mark_as_read = models.BooleanField(default=False)

	def __str__(self):
		return self.full_name + ' ' + self.subject



# Model for storing blogs
class Blog(TimeStamp):
	
	title = models.CharField(max_length=150)
	slug = models.CharField(max_length=160)
	meta_description = models.TextField(null=True, blank=True)
	description = HTMLField()
	thumbnail = models.ImageField(upload_to='blogs/thumbnail/')
	image = models.ImageField(upload_to='blogs/', null=True, blank=True)
	alt_text = models.CharField(max_length=100, null=True, blank=True)
	tags = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.title