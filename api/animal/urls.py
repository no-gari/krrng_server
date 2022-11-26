from api.animal.views import AnimalCreateView, AnimalListView, AnimalRetreiveUpdateView
from django.urls import path


urlpatterns = [
    path('create/', AnimalCreateView.as_view()),
    path('<int:pk>/', AnimalRetreiveUpdateView.as_view()),
    path('<int:pk>/', AnimalRetreiveUpdateView.as_view()),
    path('list/', AnimalListView.as_view()),
]
