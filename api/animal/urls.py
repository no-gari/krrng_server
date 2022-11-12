from api.animal.views import create_animal, AnimalListView, AnimalRetreiveUpdateView
from django.urls import path


urlpatterns = [
    path('animal/create/', create_animal),
    path('animal/update/<int:pk>/', AnimalRetreiveUpdateView.as_view()),
    path('animal/get/<int:pk>/', AnimalRetreiveUpdateView.as_view()),
    path('animal/list/', AnimalListView.as_view()),
]
