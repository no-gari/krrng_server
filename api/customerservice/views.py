from .serializers import FAQSerializer, OfferSerializer, HospitalReviewReportSerializer, \
    NotificationSerializer, NoticeSerializer, FAQMenuSerializer
from .models import FAQ, Offer, HospitalReviewReport, Notification, Notice, FAQMenu
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated


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


class OfferCreateAPIView(CreateAPIView):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()


class HospitalReviewReportCreateAPIView(CreateAPIView):
    serializer_class = HospitalReviewReportSerializer
    queryset = HospitalReviewReport.objects.all()
