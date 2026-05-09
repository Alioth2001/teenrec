from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    indoor_outdoor = models.CharField(
        max_length=20,
        choices=[("indoor", "Indoor"), ("outdoor", "Outdoor"), ("both", "Both")],
        default="both"
    )

    def __str__(self):
        return self.name
