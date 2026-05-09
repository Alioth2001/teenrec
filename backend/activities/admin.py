from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "location", "fee", "indoor_outdoor")
    search_fields = ("name", "category", "location")
