from django.shortcuts import render
from rest_framework import viewsets
from .models import SoundPreset, UserProfile
from .serializers import SoundPresetSerializer, UserProfileSerializer

class SoundPresetViewSet(viewsets.ModelViewSet):
    queryset = SoundPreset.objects.all()
    serializer_class = SoundPresetSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

