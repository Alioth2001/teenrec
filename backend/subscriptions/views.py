from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Subscription

@login_required
def subscription_view(request):
    try:
        subscription = request.user.subscription_detail
    except Subscription.DoesNotExist:
        subscription = None
    return render(request, "subscriptions/subscription.html", {"subscription": subscription})

@login_required
def upgrade_subscription(request):
    try:
        subscription = request.user.subscription_detail
        subscription.tier = "premium"
        subscription.save()
    except Subscription.DoesNotExist:
        Subscription.objects.create(user=request.user, tier="premium")
    return redirect("subscriptions:view")

@login_required
def downgrade_subscription(request):
    try:
        subscription = request.user.subscription_detail
        subscription.tier = "free"
        subscription.save()
    except Subscription.DoesNotExist:
        Subscription.objects.create(user=request.user, tier="free")
    return redirect("subscriptions:view")
