from django.urls import path
from . import views

app_name = "recommendations"

urlpatterns = [
    path("list/", views.list_recommendations, name="list"),
]
