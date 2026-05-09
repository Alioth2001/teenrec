from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    SUBSCRIPTION_CHOICES = [
        ("guest", "Guest"),
        ("free", "Free"),
        ("premium", "Premium"),
    ]
    subscription = models.CharField(
        max_length=10, choices=SUBSCRIPTION_CHOICES, default="guest"
    )

    def allowed_recommendations(self):
        if self.subscription == "guest":
            return 1
        elif self.subscription == "free":
            return 2
        elif self.subscription == "premium":
            return 3
        return 0

    def __str__(self):
        return self.username
