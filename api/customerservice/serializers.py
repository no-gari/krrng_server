from api.customerservice.models import FAQ, Offer, HospitalReviewReport,\
    HospitalReviewReportImage, Notification, Notice, FAQMenu
from rest_framework import serializers


class NoticeSerializer(serializers.ModelSerializer):
    timesince = serializers.SerializerMethodField()

    class Meta:
        model = Notice
        fields = ('name', 'content', 'timesince')

    def get_timesince(self, obj):
        from django.utils.timesince import timesince
        return timesince(obj.created_at)


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class FAQMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQMenu
        fields = ('name',)


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class HospitalReviewReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalReviewReport
        fields = '__all__'

    def create(self, validated_date):
        images = self.context['request'].FILES.getlist('hostpital_review_report_images')

        for image in list(images):
            temp_image = HospitalReviewReportImage.objects.create(property=self.instance, image=image)
            temp_image.save()
