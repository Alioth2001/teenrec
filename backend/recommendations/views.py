from django.shortcuts import render, redirect
from questionnaire.models import QuestionnaireResponse
from activities.models import Activity
from .models import Recommendation
from sklearn.neighbors import NearestNeighbors
import numpy as np

def list_recommendations(request):
    # Determine subscription type
    if request.user.is_authenticated:
        user = request.user
        allowed = user.allowed_recommendations()
        response = QuestionnaireResponse.objects.filter(user=user).order_by("-created_at").first()
        if not response:
            return redirect("questionnaire:fill")
    else:
        allowed = 1
        response = QuestionnaireResponse.objects.filter(user=None).order_by("-created_at").first()

    if not response:
        return render(request, "recommendations/recommendations.html", {"recommendations": []})

    # Convert questionnaire to feature vector (simplified example)
    user_vector = np.array([
        int(response.commitment_hours[0]),  # crude numeric mapping
        len(response.interests),
        len(response.constraints),
    ]).reshape(1, -1)

    # Build dataset of activities
    activities = Activity.objects.all()
    activity_vectors = [[len(act.name), len(act.location), int(act.fee or 0)] for act in activities]
    activity_vectors = np.array(activity_vectors)

    recs = []
    if len(activity_vectors) > 0:
        knn = NearestNeighbors(n_neighbors=min(allowed, len(activity_vectors)))
        knn.fit(activity_vectors)
        distances, indices = knn.kneighbors(user_vector)
        recs = [activities[int(idx)] for idx in indices[0]]

    # Save recommendations for logged-in users
    if request.user.is_authenticated:
        Recommendation.objects.filter(user=request.user).delete()
        for act in recs:
            Recommendation.objects.create(user=request.user, activity=act, score=1.0)

    return render(request, "recommendations/recommendations.html", {"recommendations": recs})
