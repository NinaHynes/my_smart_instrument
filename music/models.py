from django.db import models

# music/models.py
from django.db import models
from django.contrib.auth.models import User

class SoundPreset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    settings = models.JSONField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    midi_config = models.JSONField(default=dict)

class VisualPreset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    settings = models.JSONField()