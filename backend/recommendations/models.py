from django.db import models
from users.models import CustomUser
from activities.models import Activity

class Recommendation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    score = models.FloatField()  # similarity score from k-NN
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity.name} for {self.user.username}"
