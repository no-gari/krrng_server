from api.review.views import HospitalReviewListView, MyReviewListView, HospitalReviewCreateView, ReviewLikeUpdateView
from django.urls import path

urlpatterns = [
    path('create/', HospitalReviewCreateView.as_view(), name='hospital_review_create'),
    path('list/', HospitalReviewListView.as_view(), name='hospital_review_list'),
    path('my-list/', MyReviewListView.as_view(), name='my_hospital_review_list'),
    path('<int:id>/update-like/', ReviewLikeUpdateView.as_view()),
]
