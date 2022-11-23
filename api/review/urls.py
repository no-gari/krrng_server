from api.review.views import HospitalReviewSet, HospitalReviewListView, MyReviewListView, HospitalReviewCreateView
from django.urls import path

urlpatterns = [
    path('list/', HospitalReviewListView.as_view(), name='hospital_review_list'),
    path('my-list/', MyReviewListView.as_view(), name='my_hospital_review_list'),
    path('create/', HospitalReviewCreateView.as_view(), name='hospital_review_create'),
]
