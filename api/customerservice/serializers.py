from api.customerservice.models import FAQ, Offer, HospitalReviewReport, \
    HospitalReviewReportImage, Notification, Notice, FAQMenu
from rest_framework import serializers


class NoticeSerializer(serializers.ModelSerializer):
    is_expanded = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Notice
        fields = ('name', 'content', 'created_at', 'is_expanded', )

    def get_is_expanded(self, obj):
        return False


class NotificationSerializer(serializers.ModelSerializer):
    timesince = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = '__all__'

    def get_timesince(self, obj):
        from django.utils.timesince import timesince
        return timesince(obj.created_at)


class FAQMenuSerializer(serializers.ModelSerializer):
    faq = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = FAQMenu
        fields = ('name', 'id', 'faq', )

    def get_faq(self, obj):
        faqs = obj.faq_set.all()
        return FAQSerializer(faqs, many=True).data


class FAQSerializer(serializers.ModelSerializer):
    is_expanded = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = FAQ
        fields = ('name', 'content', 'id', 'is_expanded', )

    def get_is_expanded(self, obj):
        return False


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
