from django.db import models
from users.models import CustomUser

class QuestionnaireResponse(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    # Part A: Basic Profile
    age_group = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    school_level = models.CharField(max_length=20)

    # Part A: Interests
    interests = models.JSONField()  # multiple selections

    # Part A: Personality Likert scale
    teamwork = models.IntegerField()
    physical_activity = models.IntegerField()
    problem_solving = models.IntegerField()
    creativity = models.IntegerField()
    performing = models.IntegerField()
    structured_env = models.IntegerField()
    helping_others = models.IntegerField()

    # Part B: Commitment
    commitment_hours = models.CharField(max_length=20)
    schedule = models.CharField(max_length=20)

    # Part B: Skill
    participated_before = models.CharField(max_length=5)  # Yes/No
    skill_level = models.CharField(max_length=20)

    # Part B: Constraints
    activity_type = models.CharField(max_length=20)  # Indoor/Outdoor/Both
    constraints = models.JSONField()

    # Part B: Goal
    goal = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Questionnaire for {self.user.username if self.user else 'Guest'}"
