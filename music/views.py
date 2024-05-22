from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SoundPreset, UserProfile, VisualPreset
from .serializers import SoundPresetSerializer, UserProfileSerializer, VisualPresetSerializer

class SoundPresetViewSet(viewsets.ModelViewSet):
    queryset = SoundPreset.objects.all()
    serializer_class = SoundPresetSerializer
    permission_classes = [IsAuthenticated]  # Add IsAuthenticated permission

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]  # Add IsAuthenticated permission

class VisualPresetViewSet(viewsets.ModelViewSet):
    queryset = VisualPreset.objects.all()
    serializer_class = VisualPresetSerializer
    permission_classes = [IsAuthenticated]
