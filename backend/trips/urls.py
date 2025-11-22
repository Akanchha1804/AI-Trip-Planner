from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripViewSet, ChatRoomViewSet

router = DefaultRouter()
router.register(r'trips', TripViewSet)
router.register(r'chatrooms', ChatRoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
