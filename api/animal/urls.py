from api.animal.views import create_animal, AnimalListView, AnimalRetreiveUpdateView
from django.urls import path


urlpatterns = [
    path('create/', create_animal),
    path('<int:pk>/', AnimalRetreiveUpdateView.as_view()),
    path('<int:pk>/', AnimalRetreiveUpdateView.as_view()),
    path('list/', AnimalListView.as_view()),
]
