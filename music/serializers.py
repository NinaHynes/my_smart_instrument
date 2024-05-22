# music/serializers.py
from rest_framework import serializers
from .models import SoundPreset, UserProfile

class SoundPresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundPreset
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
