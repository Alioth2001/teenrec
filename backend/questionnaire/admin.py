from django.contrib import admin
from .models import QuestionnaireResponse

@admin.register(QuestionnaireResponse)
class QuestionnaireResponseAdmin(admin.ModelAdmin):
    list_display = ("user", "age_group", "gender", "school_level", "created_at")
    search_fields = ("user__username", "age_group", "gender", "school_level")
