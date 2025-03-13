from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import *
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from rest_framework.permissions import  AllowAny
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action
from .utils import Util
from django.http import Http404


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
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			


class RoomViewSet(viewsets.ViewSet):
	serializer_class = RoomSerializer
	permission_classes = [AllowAny]
	lookup_field = 'slug'

	def get_queryset(self):
		return Room.objects.prefetch_related('room_image').prefetch_related('amenities').prefetch_related('complementary')


	# Decorator for documenting API and OpenApiParameter for swagger ui param unput field
	@extend_schema(
		description='Get list of all the rooms or use api/room/?type={type}&venue={venue} to filter rooms.',
		responses={200: RoomSerializer(many=True)},
		parameters=[
        OpenApiParameter(name='type', description="Filter rooms by type.", required=False, type=str),
        OpenApiParameter(name='venue', description="Filter rooms by venue.", required=False, type=str),
    	],
	)
	def list(self, request):
		queryset = self.get_queryset()
	
		type = request.query_params.get('type', None)
		venue = request.query_params.get('venue', None)


		if type:
			queryset = queryset.filter(type=type)

		if venue:
			queryset = queryset.filter(venue=venue)

		if not queryset.exists():
			return Response({"detail": "No rooms found for the specified filters."},status=status.HTTP_404_NOT_FOUND)

		serializer = self.serializer_class(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)




	@extend_schema(
		description='Retrieve a room by it`s slug.',
		responses={200: RoomSerializer}
	)
	def retrieve(self, request, slug=None):
		try:
			room = self.get_queryset().get(slug=slug)
			serializer = self.serializer_class(room)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except Room.DoesNotExist:
			raise Http404('Room not found')
			


class ActivityViewSet(viewsets.ViewSet):
	serializer_class = ActivitySerializer
	permission_classes = [AllowAny]
	lookup_field = 'slug'

	def get_queryset(self):
		return Activity.objects.prefetch_related('activity_image')


	# Decorator for documenting API and OpenApiParameter for swagger ui param unput field
	@extend_schema(
		description='Get list of all the activities or use api/activity/?type={type}&venue={venue} to filter activities.',
		responses={200: ActivitySerializer(many=True)},
		parameters=[
        OpenApiParameter(name='type', description="Filter rooms by type.", required=False, type=str),
        OpenApiParameter(name='venue', description="Filter rooms by venue.", required=False, type=str),
    	],
	)
	def list(self, request):
		queryset = self.get_queryset()

		type = request.query_params.get('type', None)
		venue = request.query_params.get('venue', None)


		if type:
			queryset = queryset.filter(type=type)

		if venue:
			queryset = queryset.filter(venue=venue)

		if not queryset.exists():
			return Response({"detail": "No activities found for the specified filters."},status=status.HTTP_404_NOT_FOUND)

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
			raise Http404('Activity not Found')




class SocialViewSet(viewsets.ViewSet):
	serializer_class = SocialSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		return Social.objects.all()

	@extend_schema(
		description='Get social links.',
		responses={200:SocialSerializer()},
		)
	def list(self, request):
		queryset = self.get_queryset()

		if not queryset.exists():
			return Response(
				{'detail':'No social links found.'}, status=status.HTTP_400_BAD_REQUEST
			)

		serializer = self.serializer_class(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)




class GalleryViewSet(viewsets.ViewSet):
	serializer_class = GallerySerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		return Gallery.objects.all()

	@extend_schema(
		description="Get list of all gallery images.",
		responses={200:GallerySerializer(many=True)}
		)
	def list(self, request):
		queryset = self.get_queryset()
		if not queryset.exists():
			return Response(
				{'detail':'No gallery images found.'}, status=status.HTTP_400_BAD_REQUEST
				)
		serializer = self.serializer_class(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)



	@action(detail=False, methods=['get'], url_path='by-type/(?P<type>[^/.]+)')
	@extend_schema(
		description="Get list of gallery images by type.",
		responses={200:GallerySerializer(many=True)}
		)
	def list_by_type(self, request, type=None):
		queryset = self.get_queryset().filter(type=type)
		if not queryset.exists():
			return Response(
				{"detail": "No gallery images found for the specified type."},
				status=status.HTTP_404_NOT_FOUND
			)
		serializer = self.serializer_class(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)



class ContactView(APIView):
	serializer_class = ContactSerializer
	permission_classes = [AllowAny]


	@extend_schema(
		description='Contact endpoint for user.',
		request=ContactSerializer
		)
	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()

			email_data = {
				'subject':'Turag WaterResort: We received your message.',
				'body': f'''Dear {request.data['full_name']},\nThank you for contacting us. We have received your message regarding ({request.data['subject']}). We will review your inquiry and get back to you promptly.\nThank you,\nTurag Resort Team''',
				'to_email': request.data['email']			
			}

			Util.send_email(email_data)
			return Response(status=status.HTTP_200_OK)




class BlogView(viewsets.ViewSet):
	serializer_class = BlogSerializer
	permission_classes = [AllowAny]
	lookup_field = 'slug'

	def get_queryset(self):
		return Blog.objects.all()



	@extend_schema(
		description='Get list of all blogs.',
		responses={200:BlogSerializer(many=True)},
	)
	def list(self, request):
		queryset = self.get_queryset()

		if not queryset.exists():
			return Response({'detail':'No blogs found'}, status=status.HTTP_404_NOT_FOUND)

		serializer = self.serializer_class(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)



	@extend_schema(
		description='Retrieve a blog with it`s slug',
		responses={200:BlogSerializer},
	)
	def retrieve(self, request, slug=None):
		try:
			blog = self.get_queryset().get(slug=slug)
			serializer = self.serializer_class(blog)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except Blog.DoesNotExist:
			raise Http404('No blog found.')




class TransactionView(APIView):
	serializer_class = TransactionSerializer
	permission_classes = [AllowAny]

	@extend_schema(
		description='make payment and submit payment information',
		request=TransactionSerializer,
	)
	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PaymentMethodView(APIView):
	serializer_class = PaymentMethodSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		return PaymentMethod.objects.all()

	@extend_schema(
		description='all payment methods',
		responses={200:PaymentMethodSerializer},
	)
	def get(self, request):
		queryset = self.get_queryset()
		if not queryset.exists():
			return Response({'detail':'No methods are found.'}, status=status.HTTP_404_NOT_FOUND)
		serializer = self.serializer_class(queryset, many=True)

		return Response(serializer.data, status=status.HTTP_200_OK)



class AboutView(APIView):
	serializer_class = AboutSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		return About.objects.all()

	@extend_schema(
		description='get address, email, phone and social links for turag.',
		
	)
	def get(self, request):
		queryset = self.get_queryset()
		if not queryset.exists():
			return Response({'detail':'No about informations are found !'}, status=status.HTTP_404_NOT_FOUND)
		serializer = self.serializer_class(queryset, many=True)
		return Response(serializer,data, status=status.HTTP_200_OK)