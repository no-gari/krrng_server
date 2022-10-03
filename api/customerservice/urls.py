from .views import FAQListAPIView, OfferCreateAPIView, HospitalReviewReportCreateAPIView
from django.urls import path


urlpatterns = [
    path('faq/list/', FAQListAPIView.as_view()),
    path('offer/create/', OfferCreateAPIView.as_view()),
    path('review-report/create/', HospitalReviewReportCreateAPIView.as_view()),
]
