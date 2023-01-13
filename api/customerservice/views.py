from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from .models import FAQ, Offer, HospitalReviewReport, Notification, Notice, FAQMenu, AppVersion
from .serializers import FAQSerializer, OfferSerializer, NotificationSerializer, \
    HospitalReviewReportSerializer, NoticeSerializer, FAQMenuSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json


class NotificationAPIView(ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user, is_deleted=False).prefetch_related('user').order_by('-id')


@api_view(['GET'])
def notificationReadAll(request):
    try:
        notifications = Notification.objects.filter(
            user=request.user, is_read=False, is_deleted=False
        ).prefetch_related('user')
        for noti in notifications:
            noti.is_read = True
            noti.save()
        return Response(status=status.HTTP_200_OK)
    except:
        raise ValidationError()


@api_view(['DELETE'])
def notificationDelete(request, *args, **kwargs):
    try:
        noti = Notification.objects.get(id=kwargs['pk'])
        noti.is_deleted = True
        noti.save()
        notis = Notification.objects.filter(user=request.user, is_deleted=False).prefetch_related('user').order_by('-id')
        return Response(NotificationSerializer(notis, many=True).data, status=status.HTTP_200_OK)
    except:
        raise ValidationError()


class NotificationUpdateView(UpdateAPIView):
    serializer_class = NoticeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Notification.objects.prefetch_related('user')
    lookup_field = ['pk']

    def get_object(self):
        return Notification.objects.get(id=self.kwargs['pk'])


class NotificationDestroyView(DestroyAPIView):
    serializer_class = NoticeSerializer
    queryset = Notification.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_object(self):
        return Notification.objects.get(id=self.kwargs['pk'], user=self.request.user)


class NoticeAPIView(ListAPIView):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all().order_by('-id')


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


@api_view(['GET'])
def app_version(request, *args, **kwargs):
    try:
        latest_app_version = AppVersion.objects.all().order_by('version').last()
        app_version = latest_app_version.version
        return Response(app_version, status=status.HTTP_200_OK)
    except:
        raise ValidationError()
