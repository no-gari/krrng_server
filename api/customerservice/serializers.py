from api.customerservice.models import FAQ, Offer, HospitalReviewReport, HospitalReviewReportImage
from rest_framework import serializers


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
