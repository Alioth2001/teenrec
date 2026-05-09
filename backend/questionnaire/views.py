from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import QuestionnaireForm
from .models import QuestionnaireResponse

def fill_questionnaire(request):
    if request.method == "POST":
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            questionnaire = form.save(commit=False)
            if request.user.is_authenticated:
                questionnaire.user = request.user
            else:
                questionnaire.user = None
            questionnaire.save()
            return redirect("recommendations:list")
    else:
        if request.user.is_authenticated:
            existing = QuestionnaireResponse.objects.filter(user=request.user).order_by("-created_at").first()
            form = QuestionnaireForm(instance=existing) if existing else QuestionnaireForm()
        else:
            form = QuestionnaireForm()

    return render(request, "questionnaire/fill.html", {"form": form})



@login_required
def edit_questionnaire(request):
    questionnaire = QuestionnaireResponse.objects.filter(user=request.user).order_by("-created_at").first()

    if request.method == "POST":
        form = QuestionnaireForm(request.POST, instance=questionnaire)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.user = request.user
            updated.save()
            return redirect("recommendations:list")
    else:
        form = QuestionnaireForm(instance=questionnaire)

    return render(request, "questionnaire/questionnaire.html", {"form": form})

