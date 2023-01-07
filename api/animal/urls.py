from api.animal.views import AnimalListView, AnimalRetreiveUpdateView, AnimalKindListView, AnimalCreateAPIView
from django.urls import path


urlpatterns = [
    path('<int:pk>/', AnimalRetreiveUpdateView.as_view()),
    path('<int:pk>/', AnimalRetreiveUpdateView.as_view()),
    path('create/', AnimalCreateAPIView.as_view()),
    path('kind/', AnimalKindListView.as_view()),
    path('list/', AnimalListView.as_view()),
]
