from .models import HospitalReview, HospitalReviewImage, HospitalRecieptImage
from rest_framework.exceptions import ValidationError
from rest_framework import serializers


class HospitalReviewImageSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=False)

    class Meta:
        model = HospitalReviewImage
        exclude = ('hospital_review', )


class HospitalRecieptImageSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=False)

    class Meta:
        model = HospitalRecieptImage
        exclude = ('hospital_review', )


class HospitalReviewSerializer(serializers.ModelSerializer):
    is_like = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField(read_only=True)
    nickname = serializers.SerializerMethodField(read_only=True)
    review_image = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = HospitalReview
        fields = ('id', 'nickname', 'diagnosis', 'rates', 'content', 'likes', 'review_image', 'created_at', 'is_like')

    def get_likes(self, obj):
        return obj.like_users.count()

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

    def get_nickname(self, obj):
        return obj.user.profile_set.last().nickname

    def get_review_image(self, obj):
        return HospitalReviewImageSerializer(obj.hospitalreviewimage_set.all(), many=True).data

    def get_is_like(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return user in obj.like_users.all()
        else:
            return False


class HospitalReviewCreateSerializer(HospitalReviewSerializer):
    review_image = serializers.ListField(child=serializers.FileField(allow_empty_file=True, use_url=True))
    reciept_image = serializers.ListField(child=serializers.FileField(allow_empty_file=True, use_url=True))

    class Meta:
        model = HospitalReview
        fields = ('hospital', 'diagnosis', 'content', 'rates', 'review_image', 'reciept_image')

    def create(self, validated_data):
        hospital = validated_data['hospital']
        diagnosis = validated_data['diagnosis']
        content = validated_data['content']
        rates = validated_data['rates']
        review_image = validated_data['review_image']
        reciept_image = validated_data['reciept_image']

        new_review = HospitalReview.objects.create(
            user=self.context['request'].user,
            hospital=hospital,
            diagnosis=diagnosis,
            content=content,
            rates=rates
        )
        new_review.save()

        for image in review_image:
            new_image = HospitalReviewImage.objects.create(hospital_review=new_review, image=image)
            new_image.save()

        for image in reciept_image:
            new_image = HospitalRecieptImage.objects.create(hospital_review=new_review, image=image)
            new_image.save()

        return validated_data


class HospitalReviewLikeSerializer(serializers.ModelSerializer):
    is_like = serializers.SerializerMethodField()

    class Meta:
        model = HospitalReview
        fields = ['is_like']

    def get_is_like(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return user in obj.like_users.all()
        else:
            return False

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if not user.is_authenticated:
            return ValidationError({'error_msg': '좋아요를 누르려면 로그인 해야 합니다.'})
        if user in instance.like_users.all():
            instance.like_users.remove(user)
        else:
            instance.like_users.add(user)
        return instance
