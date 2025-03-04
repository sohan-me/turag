from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'room', views.RoomViewSet, basename='room')
router.register(r'activity', views.ActivityViewSet, basename='activity')
router.register(r'social', views.SocialViewSet, basename='social')
router.register(r'gallery', views.GalleryViewSet, basename='gallery')
router.register(r'blog', views.BlogView, basename='blog'),


urlpatterns = [
	path('', include(router.urls)),
	path('booking/', views.BookingView.as_view()),
	path('contact/', views.ContactView.as_view()),	
]