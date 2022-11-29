from api.animal.views import create_animal, AnimalListView, AnimalRetreiveUpdateView, AnimalKindListView
from django.urls import path


urlpatterns = [
    path('create/', create_animal),
    path('<int:pk>/', AnimalRetreiveUpdateView.as_view()),
    path('<int:pk>/', AnimalRetreiveUpdateView.as_view()),
    path('list/', AnimalListView.as_view()),

    path('kind/', AnimalKindListView.as_view()),
]
