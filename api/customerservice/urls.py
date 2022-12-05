from .views import FAQListAPIView, OfferCreateAPIView, FAQMenuListView, HospitalReviewReportCreateAPIView, \
    NoticeAPIView, NotificationAPIView, NotificationDestroyView, notificationDelete, notificationReadAll
from django.urls import path


urlpatterns = [
    path('faq-menu/list/', FAQMenuListView.as_view()),
    path('faq/list/', FAQListAPIView.as_view()),
    path('offer/create/', OfferCreateAPIView.as_view()),
    # path('review-report/create/', HospitalReviewReportCreateAPIView.as_view()),
    path('notice/list/', NoticeAPIView.as_view()),

    path('notification/delete/<int:pk>/', notificationDelete),
    path('notification/read-all/', notificationReadAll),
    path('notification/list/', NotificationAPIView.as_view()),
]
