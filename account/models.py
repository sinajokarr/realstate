from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age          = models.PositiveIntegerField(null=True, blank=True)
    is_agent     = models.BooleanField(default=False)
    agency_name  = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    avatar       = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
