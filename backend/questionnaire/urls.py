from django.urls import path
from . import views

app_name = "questionnaire"

urlpatterns = [
    path("fill/", views.fill_questionnaire, name="fill"),
    path("edit/", views.edit_questionnaire, name="edit"),
]
