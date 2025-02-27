from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import *
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import  AllowAny
from .serializers import BookingSerializer, RoomSerializer, ActivitySerializer, SocialSerializer
from rest_framework.response import Response
from .utils import Util


# Create your views here.


# User Booking View
class BookingView(APIView):
	serializer_class = BookingSerializer
	permission_classes = [AllowAny]
	

	@extend_schema(
        description="Create Booking for Users.",
        request=BookingSerializer
    )
	def post(self, request):

		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()

			email_data = {
				'subject': f'Room Booking Request Received.',
				'body': f'''Dear {request.data.get('full_name')},\nThis email confirms that we have received your room booking request for {request.data['check_in']} to {request.data['check_out']}.\nWe are currently reviewing your request and will contact you shortly with an update on its status.\nThank you for your patience.\nSincerely,\nTurag Resort''',
				'to_email': request.data.get('email'),
			}

			# Send email to user upon booking request
			Util.send_email(email_data)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
			


class RoomViewSet(viewsets.ViewSet):
	serializer_class = RoomSerializer
	permission_classes = [AllowAny]
	lookup_field = 'slug'

	def get_queryset(self):
		return Room.objects.prefetch_related('room_image').prefetch_related('amenities').prefetch_related('complementary')


	@extend_schema(
		description='Get list of all the rooms.',
		responses={200: RoomSerializer(many=True)}
	)
	def list(self, request):
		queryset = self.get_queryset()
		serializer = self.serializer_class(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


	@extend_schema(
		description='Retrieve a room by its slug.',
		responses={200: RoomSerializer}
	)
	def retrieve(self, request, slug=None):
		try:
			room = self.get_queryset().get(slug=slug)
			serializer = self.serializer_class(room)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except Room.DoesNotExist:
			raise NotFound(detail='Room not Found')
			


class ActivityViewSet(viewsets.ViewSet):
	serializer_class = ActivitySerializer
	permission_classes = [AllowAny]
	lookup_field = 'slug'

	def get_queryset(self):
		return Activity.objects.prefetch_related('activity_image')

	@extend_schema(
		description='Get list of all the activities.',
		responses={200: ActivitySerializer(many=True)},
	)
	def list(self, request):
		queryset = self.get_queryset()
		serializer = self.serializer_class(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	@extend_schema(
		description='Retrieve a activity by its slug.',
		responses={200: ActivitySerializer},
	)
	def retrieve(self, request, slug=None):
		try:
			activity = self.get_queryset().get(slug=slug)
			serializer = self.serializer_class(activity)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except Activity.DoesNotExist:
			raise NotFound(detail='Activity not found')




class SocialViewSet(viewsets.ViewSet):
	serializer_class = SocialSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		return Social.objects.all()

	@extend_schema(
		description='Get list of all social links',
		responses={200:SocialSerializer(many=True)}
		)
	def list(self, request):
		queryset = self.get_queryset()
		serializer = self.serializer_class(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)