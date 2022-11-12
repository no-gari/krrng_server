from django.urls import path
from .views import DiseaseListView

urlpatterns = [
    path('<str:keyword>/', DiseaseListView.as_view()),
]
