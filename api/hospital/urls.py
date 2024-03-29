from api.hospital.views import HospitalListView, HospitalDetailView, HospitalSearchView
from django.urls import path

urlpatterns = [
    path('detail/<int:pk>/', HospitalDetailView.as_view()),
    path('search/', HospitalSearchView.as_view()),
    path('list/', HospitalListView.as_view()),
]
