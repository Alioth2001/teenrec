from django import forms
from .models import QuestionnaireResponse

class QuestionnaireForm(forms.ModelForm):
    LIKERT_CHOICES = [
        (1, "Strongly Disagree"),
        (2, "Disagree"),
        (3, "Neutral"),
        (4, "Agree"),
        (5, "Strongly Agree"),
    ]

    AGE_CHOICES = [("13-14", "13–14"), ("15-16", "15–16"), ("17-18", "17–18")]
    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]
    SCHOOL_CHOICES = [("lower", "Lower secondary"), ("alevels", "A-levels")]

    INTEREST_CHOICES = [
        ("sports", "Sports"),
        ("music", "Music"),
        ("arts", "Arts"),
        ("tech", "Technology"),
        ("drama", "Drama/acting"),
        ("writing", "Writing/Journalism"),
        ("debate", "Debate/Public speaking"),
        ("volunteering", "Community Service/Volunteering"),
        ("entrepreneurship", "Entrepreneurship"),
        ("science", "Science clubs"),
    ]

    COMMITMENT_CHOICES = [
        ("<2", "< 2 hours"),
        ("2-4", "2–4 hours"),
        ("5-7", "5–7 hours"),
        ("8+", "8+ hours"),
    ]

    SCHEDULE_CHOICES = [("weekdays", "Weekdays"), ("weekends", "Weekends"), ("both", "Both")]
    PARTICIPATED_CHOICES = [("yes", "Yes"), ("no", "No")]
    SKILL_CHOICES = [("beginner", "Beginner"), ("intermediate", "Intermediate"), ("advanced", "Advanced")]
    ACTIVITY_TYPE_CHOICES = [("indoor", "Indoor"), ("outdoor", "Outdoor"), ("both", "Both")]
    LIMITATION_CHOICES = [("physical", "Physical"), ("time", "Time constraint"), ("financial", "Financial"), ("none", "None")]
    GOAL_CHOICES = [("fun", "Fun and relaxation"), ("skills", "Skill development"), ("social", "Socializing"), ("career", "Career preparation")]

    # Fields
    age_group = forms.ChoiceField(choices=AGE_CHOICES, widget=forms.RadioSelect)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    school_level = forms.ChoiceField(choices=SCHOOL_CHOICES, widget=forms.RadioSelect)

    interests = forms.MultipleChoiceField(choices=INTEREST_CHOICES, widget=forms.CheckboxSelectMultiple)

    teamwork = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect)
    physical_activity = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect)
    problem_solving = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect)
    creativity = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect)
    performing = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect)
    structured_env = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect)
    helping_others = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect)

    commitment_hours = forms.ChoiceField(choices=COMMITMENT_CHOICES, widget=forms.RadioSelect)
    schedule = forms.ChoiceField(choices=SCHEDULE_CHOICES, widget=forms.RadioSelect)

    participated_before = forms.ChoiceField(choices=PARTICIPATED_CHOICES, widget=forms.RadioSelect)
    skill_level = forms.ChoiceField(choices=SKILL_CHOICES, widget=forms.RadioSelect)

    activity_type = forms.ChoiceField(choices=ACTIVITY_TYPE_CHOICES, widget=forms.RadioSelect)
    constraints = forms.MultipleChoiceField(choices=LIMITATION_CHOICES, widget=forms.CheckboxSelectMultiple)

    goal = forms.ChoiceField(choices=GOAL_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = QuestionnaireResponse
        fields = [
            "age_group", "gender", "school_level", "interests",
            "teamwork", "physical_activity", "problem_solving", "creativity",
            "performing", "structured_env", "helping_others",
            "commitment_hours", "schedule", "participated_before", "skill_level",
            "activity_type", "constraints", "goal"
        ]
