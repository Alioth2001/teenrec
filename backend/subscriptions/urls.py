from django.urls import path
from . import views

app_name = "subscriptions"

urlpatterns = [
    path("", views.subscription_view, name="view"),
    path("upgrade/", views.upgrade_subscription, name="upgrade"),
    path("downgrade/", views.downgrade_subscription, name="downgrade"),
]
