from .serializers import FAQSerializer, OfferSerializer, HospitalReviewReportSerializer, \
    NotificationSerializer, NoticeSerializer, FAQMenuSerializer
from .models import FAQ, Offer, HospitalReviewReport, Notification, Notice, FAQMenu
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import json


class NotificationAPIView(ListAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = [IsAuthenticated]


class NoticeAPIView(ListAPIView):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()


class NotificationDestroyView(DestroyAPIView):
    serializer_class = NoticeSerializer
    queryset = Notification.objects.all()
    permission_classes = (IsAuthenticated, )
    lookup_field = 'pk'

    def get_object(self):
        return Notification.objects.get(id=self.kwargs['pk'], user=self.request.user)


class FAQListAPIView(ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        if self.request.GET.get('category') == '0':
            return FAQ.objects.all()
        else:
            return FAQ.objects.filter(faq_menu_id=int(self.request.GET.get('category')))


class FAQMenuListView(ListAPIView):
    serializer_class = FAQMenuSerializer
    queryset = FAQMenu.objects.all()

    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs).data
        json_str = json.dumps(data)
        json_object = json.loads(json_str)
        all_faqs = FAQ.objects.all()
        all_faq_data = FAQSerializer(all_faqs, many=True).data
        json_object.insert(0, {
            "name": "전체보기",
            "id": 0,
            "faq": all_faq_data
        })
        return Response(json_object, status=status.HTTP_200_OK)


class OfferCreateAPIView(CreateAPIView):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()


class HospitalReviewReportCreateAPIView(CreateAPIView):
    serializer_class = HospitalReviewReportSerializer
    queryset = HospitalReviewReport.objects.all()
