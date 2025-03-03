from rest_framework import serializers
from .models import *



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
		fields = ['id', 'title', 'slug', 'description', 'cost', 'type', 'tags', 'is_available', 'images', 'amenities', 'complementary']
		read_only_fields = ['id', 'slug']


class ActivityImageLineSerializer(serializers.ModelSerializer):
	class Meta:
		model = ActivityImageLine
		fields = ['image', 'is_featured']


class ActivitySerializer(serializers.ModelSerializer):
	images = ActivityImageLineSerializer(many=True, source='activity_image')

	class Meta:
		model = Activity
		fields = ['id', 'title', 'slug', 'description', 'type', 'tags', 'images']
		read_only_fields = ['id', 'slug']



class BookingSerializer(serializers.ModelSerializer):
	room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
	
	class Meta:
		model = Booking
		fields = ['id', 'room', 'full_name', 'email', 'phone', 'adults', 'children', 'check_in', 'check_out', 'address', 'remarks']
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