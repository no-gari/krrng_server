from .models import HospitalReview, HospitalReviewImage, HospitalRecieptImage
from rest_framework import serializers


class HospitalReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalReviewImage
        fields = ('image', )


class HospitalRecieptImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalRecieptImage
        fields = ('image', )


class HospitalReviewSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    rates = serializers.SerializerMethodField()
    reciept_image = HospitalRecieptImageSerializer(source='recieptimage_set', many=True, read_only=True)
    review_image = HospitalReviewImageSerializer(source='reviewimage_set', many=True, read_only=True)

    class Meta:
        model = HospitalReview
        exclude = ('user', 'like_users', 'rates')

    def get_likes(self, obj):
        return obj.like_users.count()

    def get_rate(self, obj):
        return round(obj.rates, 1)

    def create(self, validated_data):
        reciept_images = validated_data.pop('reciept_image')
        review_images = validated_data.pop('review_image')
        h_review = HospitalReview.objects.create(
            user=self.context['request'].user,
            hospital_id=self.validated_data.get('hospital'),
            diagnosis=self.validated_data.get('diagnosis'),
            review=self.validated_data.get('review'),
            rates=self.validated_data.get('rates'),
        )
        for reciept_image in reciept_images:
            new_reciept = HospitalRecieptImage.objects.create(hospital_review=h_review, image=reciept_image)
            new_reciept.save()
        for review_image in review_images:
            new_review = HospitalRecieptImage.objects.create(hospital_review=h_review, image=review_image)
            new_review.save()
        return h_review
