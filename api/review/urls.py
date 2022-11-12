from api.review.views import HospitalReviewSet
from django.urls import path

review = HospitalReviewSet.as_view({
    'get': 'list',
    'post': 'create'
})
review_detail = HospitalReviewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', review, name='review'),
    path('<int:pk>/', review_detail, name='review_detail'),
]
