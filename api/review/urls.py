from api.review.views import HospitalReviewSet
from django.urls import path

review = HospitalReviewSet.as_view({
    'get': 'list',
    'post': 'create'
})

review_detail = HospitalReviewSet.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'delete'
})

urlpatterns = [
    path('<int:pk>/', review, name='review'),
    path('detail/<int:pk>/', review_detail, name='review_detail'),
]
