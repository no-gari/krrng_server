import geopy.distance
from django.db.models import Avg, Min
from rest_framework import serializers
from .models import BestPart, AvailableAnimal, Hospital, HospitalPrice, HospitalImage
from ..review.serializers import HospitalReviewSerializer


class BestPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestPart
        fields = ('name', 'id', 'image',)


class AvailableAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableAnimal
        fields = ('name', 'id',)


class HospitalListSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField(read_only=True)
    distance = serializers.SerializerMethodField(read_only=True)
    review_count = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Hospital
        exclude = ('is_visible', 'available_animal', 'best_part', 'rest_date', 'available_time', 'number', 'intro', )

    def get_price(self, obj):
        disease = self.context['request'].query_params.get('disease', None)
        if disease == '0':
            hospital_price = HospitalPrice.objects.filter(hospital=obj).aggregate(Min('price'))
            return hospital_price['price__min']
        else:
            hospital_price = HospitalPrice.objects.filter(disease_id=int(disease), hospital=obj).last()
            return hospital_price.price

    def get_distance(self, obj):
        user_latitude = self.context['request'].query_params.get('userLatitude', None)
        user_longitude = self.context['request'].query_params.get('userLongitude', None)
        point1 = (user_latitude, user_longitude)
        point2 = (float(obj.latitude), float(obj.longitude))
        distance = geopy.distance.geodesic(point1, point2).m
        return int(distance)

    def get_review_count(self, obj):
        reviews = obj.hospital_reviews.all().count()
        return reviews

    def get_image(self, obj):
        image_url = obj.hospitalimage_set.first().image.url
        return image_url


class HospitalPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalPrice
        exclude = ('hospital', 'disease', )


class HospitalImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = HospitalImage
        fields = ('image', 'id',)

    def get_image(self, obj):
        return obj.image.url


class HospitalDetailSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField(read_only=True)
    review_count = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    rate = serializers.SerializerMethodField(read_only=True)
    price_list = serializers.SerializerMethodField(read_only=True)
    available_animal = AvailableAnimalSerializer(read_only=True, many=True)
    best_part = BestPartSerializer(read_only=True, many=True)
    hospital_review = HospitalReviewSerializer(read_only=True, many=True, source='hospital_reviews')

    class Meta:
        model = Hospital
        exclude = ('recommend', 'is_visible', 'latitude', 'longitude',)

    def get_distance(self, obj):
        user_latitude = self.context['request'].query_params.get('userLatitude', None)
        user_longitude = self.context['request'].query_params.get('userLongitude', None)
        point1 = (user_latitude, user_longitude)
        point2 = (float(obj.latitude), float(obj.longitude))
        distance = geopy.distance.geodesic(point1, point2).m
        return int(distance)

    def get_review_count(self, obj):
        reviews = obj.hospital_reviews.count()
        return reviews

    def get_images(self, obj):
        images = obj.hospitalimage_set.all()
        return HospitalImageSerializer(images, many=True).data

    def get_rate(self, obj):
        if obj.hospital_reviews.count() == 0:
            return 0
        else:
            review_average = obj.hospital_reviews.aggregate(Avg('rates'))
            return review_average['rates__avg']

    def get_price_list(self, obj):
        return HospitalPriceSerializer(HospitalPrice.objects.filter(hospital=obj), many=True).data
