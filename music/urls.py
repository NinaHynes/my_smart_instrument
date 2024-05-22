# music/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SoundPresetViewSet, UserProfileViewSet, VisualPresetViewSet

router = DefaultRouter()
router.register(r'sound-presets', SoundPresetViewSet)
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'visual-presets', VisualPresetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
