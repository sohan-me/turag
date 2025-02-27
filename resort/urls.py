from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'room', views.RoomViewSet, basename='room')
router.register(r'activity', views.ActivityViewSet, basename='activity')


urlpatterns = [
	path('', include(router.urls)),
	path('booking/', views.BookingView.as_view())	
]