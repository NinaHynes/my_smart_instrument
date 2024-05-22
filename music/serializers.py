from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SoundPreset, UserProfile, VisualPreset


class SoundPresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundPreset
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class VisualPresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisualPreset
        fields = '__all__'