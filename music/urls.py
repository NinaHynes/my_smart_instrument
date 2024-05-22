# music/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SoundPresetViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'sound-presets', SoundPresetViewSet)
router.register(r'user-profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
