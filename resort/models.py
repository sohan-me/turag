import uuid
from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from tinymce.models import HTMLField
from .utils import Util
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

		('Partially Paid', 'Partially Paid'),
		('Fully Paid', 'Fully Paid'),
	]



	room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
	full_name = models.CharField(max_length=150)
	email = models.EmailField(null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	adults = models.PositiveIntegerField()
	children = models.PositiveIntegerField(null=True, blank=True)
	check_in = models.DateField()
	check_out = models.DateField()
	address = models.CharField(max_length=255, null=True, blank=True)
	remarks = models.CharField(max_length=255, null=True, blank=True)
	booking_number = models.CharField(max_length=100, null=True, blank=True)
	status = models.CharField(max_length=100, choices=STATUS, default='Pending')


	def __str__(self):
		return self.full_name

	# Generate Booking Number
	def set_booking_number(self):
		unique_id = uuid.uuid4().hex[:12]
		email_part = self.email.split('@')[0] if self.email else "guest.who"
		self.booking_number = f"{email_part.lower()}-{unique_id}"

	# Assign the booking number if its empty
	def save(self, *args, **kwargs):
		if not self.booking_number:
			self.set_booking_number()

		# Send email to a user when booking available and marked by admin
		if self.status == 'Confirmed':
			data = {
				'full_name': self.full_name,
				'to_email': self.email,
				'room_title': self.room.title,
				'check_in': self.check_in,
				'check_out': self.check_out,
				'booking_id': self.booking_number,
			}
			Util.send_payment_email(data)

		if self.status == 'Cancelled':
			data = {
				'full_name': self.full_name,
				'to_email': self.email,
				'room_title': self.room.title,
				'check_in': self.check_in,
				'check_out': self.check_out,
				'booking_id': self.booking_number,
			}
			Util.send_cancellation_email(data)
		super().save(*args, **kwargs)



class Transaction(TimeStamp):

	booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True, related_name='transaction')
	payment_method = models.CharField(max_length=100)
	trans_id = models.CharField(max_length=200, unique=True)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	document = models.ImageField(upload_to='transaction/', null=True, blank=True)
	is_approved = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.trans_id} - {self.amount}' 

	def save(self, *args, **kwargs):
		if self.is_approved and self.booking:
			book_cost = self.booking.room.cost
			if self.amount >= book_cost:
				self.booking.status = 'Fully Paid'
			else:
				self.booking.status = 'Partially Paid'

			self.booking.save()
			data = {
				'full_name': self.booking.full_name,
				'to_email': self.booking.email,
				'room_title': self.booking.room.title,
				'booking_id': self.booking.booking_number,
				'trans_id': self.trans_id,
				'paid_amount': self.amount,
			}
			Util.send_transaction_email(data)
		super().save(*args, **kwargs)


class PaymentMethod(TimeStamp):
	PAYMENT_METHOD = (
			('Bkash', 'Bkash'),
			('Rocket', 'Rocket'),
			('Nagad', 'Nagad'),
			('Upay', 'Upay'),
			('Bank', 'Bank'),
			('Other', 'Other'),
		)

	method_name = models.CharField(choices=PAYMENT_METHOD, max_length=50)
	account_no = models.CharField(max_length=20, null=True, blank=True)
	account_holder = models.CharField(max_length=100)
	account_type = models.CharField(max_length=50)
	banner = models.ImageField(upload_to='payment_method/banner/', null=True, blank=True)
	qrcode = models.ImageField(upload_to='payment_method/qrcode', null=True, blank=True)
	ifsc_code = models.CharField(max_length=100)

	def __str__(self):
		return self.method_name




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
	image = models.ImageField(upload_to='blogs/', null=True, blank=True)
	alt_text = models.CharField(max_length=100, null=True, blank=True)
	tags = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.title



class About(TimeStamp):
	address = models.CharField(max_length=200)
	email = models.EmailField(null=True, blank=True)
	phone = models.CharField(max_length=40)
	facebook = models.URLField(null=True, blank=True)
	instagram = models.URLField(null=True, blank=True)
	youtube = models.URLField(null=True, blank=True)
	linkedin = models.URLField(null=True, blank=True)
	twitter = models.URLField(null=True, blank=True)
	pinterest = models.URLField(null=True, blank=True)
	tiktok = models.URLField(null=True, blank=True)


	def __str__(self):
		return self.address
