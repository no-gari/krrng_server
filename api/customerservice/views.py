from .serializers import FAQSerializer, OfferSerializer, HospitalReviewReportSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import FAQ, Offer, HospitalReviewReport
from rest_framework.permissions import AllowAny


class FAQListAPIView(ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()
    permission_classes = AllowAny


class OfferCreateAPIView(CreateAPIView):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
    permission_classes = AllowAny


class HospitalReviewReportCreateAPIView(CreateAPIView):
    serializer_class = HospitalReviewReportSerializer
    queryset = HospitalReviewReport.objects.all()
    permission_classes = AllowAny
