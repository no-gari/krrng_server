import geopy.distance
from rest_framework import serializers
from .models import BestPart, AvailableAnimal, Hospital, HospitalPrice, HospitalImage


class BestPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestPart
        fields = ('name', 'id',)


class AvailableAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableAnimal
        fields = ('name', 'id',)


class HospitalListSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField(read_only=True)
    distance = serializers.SerializerMethodField(read_only=True)
    review_count = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)
    available_animal = AvailableAnimalSerializer(read_only=True, many=True)
    best_part = BestPartSerializer(read_only=True, many=True)

    class Meta:
        model = Hospital
        exclude = ('is_visible', )

    def get_price(self, obj):
        disease = self.context['request'].query_params.get('bestPart', None)
        hospital_price = HospitalPrice.objects.filter(disease_id=int(disease), hospital=obj).last()
        return int(hospital_price.price)

    def get_distance(self, obj):
        user_latitude = self.context['request'].query_params.get('userLatitude', None)
        user_longitude = self.context['request'].query_params.get('userLongitude', None)
        point1 = (user_latitude, user_longitude)
        point2 = (float(obj.latitude), float(obj.longitude))
        distance = geopy.distance.geodesic(point1, point2).m
        return int(distance)

    def get_review_count(self, obj):
        reviews = obj.hospitalreview_set.count()
        return reviews

    def get_image(self, obj):
        image_url = obj.hospitalimage_set.first().image.url
        return image_url


class HospitalPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalPrice
        exclude = ('hostpital', 'disease', )


class HospitalDetailSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField(read_only=True)
    review_count = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    rate = serializers.SerializerMethodField(read_only=True)
    price_list = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Hospital
        exclude = ('recommend_number', )
