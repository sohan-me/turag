from rest_framework import serializers
from .models import *
from django.shortcuts import get_object_or_404



class RoomImageLineSerializer(serializers.ModelSerializer):
	class Meta:
		model = RoomImageLine
		fields = ['image', 'is_featured']


class AmenitiesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Amenities
		fields = ['icon', 'title']


class ComplementarySerializer(serializers.ModelSerializer):
	class Meta:
		model = Complementary
		fields = ['icon', 'title']


class RoomSerializer(serializers.ModelSerializer):
	images = RoomImageLineSerializer(many=True, source='room_image')
	amenities = AmenitiesSerializer(many=True)
	complementary = ComplementarySerializer(many=True)

	class Meta:
		model = Room
		fields = ['id', 'title', 'slug', 'description', 'cost', 'type', 'venue', 'tags', 'is_available', 'images', 'amenities', 'complementary']
		read_only_fields = ['id', 'slug']


class ActivityImageLineSerializer(serializers.ModelSerializer):
	class Meta:
		model = ActivityImageLine
		fields = ['image', 'is_featured']


class ActivitySerializer(serializers.ModelSerializer):
	images = ActivityImageLineSerializer(many=True, source='activity_image')

	class Meta:
		model = Activity
		fields = ['id', 'title', 'slug', 'slogan', 'description', 'type', 'venue', 'tags', 'images']
		read_only_fields = ['id', 'slug']


class PlanSerializer(serializers.ModelSerializer):
	class Meta:
		model = Plan
		fields = '__all__'



class BookingSerializer(serializers.ModelSerializer):
	room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
	plan_type = serializers.PrimaryKeyRelatedField(queryset=Plan.objects.all())
	
	class Meta:
		model = Booking
		fields = ['id', 'room', 'plan_type', 'full_name', 'email', 'phone', 'adults', 'children', 'check_in', 'check_out', 'address', 'remarks']
		read_only_fields = ['id']

	def validate(self, data):
		if data['check_in'] > data['check_out']:
			raise serializers.ValidationError('check_out must occur after check_in.')
		return data


class SocialSerializer(serializers.ModelSerializer):
	class Meta:
		model = Social
		fields = '__all__'



class GallerySerializer(serializers.ModelSerializer):
	class Meta:
		model = Gallery
		fields = '__all__'




class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		exclude = ['mark_as_read']



class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
	booking_id = serializers.CharField(write_only=True)
	class Meta:
		model = Transaction
		fields = ['payment_method', 'trans_id', 'booking_id', 'amount', 'document']

	def create(self, validated_data):
		booking_number = validated_data.pop('booking_id', None)
		booking = get_object_or_404(Booking, booking_number=booking_number) if booking_number else None
		validated_data['booking'] = booking
		return super().create(validated_data)



class PaymentMethodSerializer(serializers.ModelSerializer):
	class Meta:
		model = PaymentMethod
		fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
	class Meta:
		model = About
		fields = '__all__'


class VenueInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = VenueInfo
		fields = '__all__'
