from django.db import models
from users.models import CustomUser

class Subscription(models.Model):
    TIER_CHOICES = [
        ("free", "Free"),
        ("premium", "Premium"),
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="subscription_detail")
    tier = models.CharField(max_length=10, choices=TIER_CHOICES, default="free")
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.tier}"
