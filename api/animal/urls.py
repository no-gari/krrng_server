from api.animal.views import AnimalCreateAPIView
from django.urls import path


urlpatterns = [
    path('animal/create/', AnimalCreateAPIView.as_view()),
]
