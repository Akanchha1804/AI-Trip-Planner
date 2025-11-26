from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripViewSet, ChatRoomViewSet, UserActivityViewSet, BookingViewSet, signup, login

router = DefaultRouter()
router.register(r'trips', TripViewSet)
router.register(r'chatrooms', ChatRoomViewSet)
router.register(r'user-activities', UserActivityViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]
