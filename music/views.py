from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SoundPreset, UserProfile
from .serializers import SoundPresetSerializer, UserProfileSerializer

class SoundPresetViewSet(viewsets.ModelViewSet):
    queryset = SoundPreset.objects.all()
    serializer_class = SoundPresetSerializer
    permission_classes = [IsAuthenticated]  # Add IsAuthenticated permission

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]  # Add IsAuthenticated permission


