from rest_framework import serializers
from .models import BestPart, AvailableAnimal, HopitalPrice, Hospital, HospitalReview, HospitalReviewImage, HospitalImage
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView


class HotelListAPIView(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['name']

    hospital_price = serializers.SerializerMethodField(read_only=True)
    hospital_address = serializers.SerializerMethodField(read_only=True)
    hospital_image = serializers.SerializerMethodField(read_only=True)
    rate = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    def get_hospital_price(self, value):
        pass

    def get_hospital_address(self, value):
        pass

    def get_hopital_image(self, value):
        pass

    def get_rate(self, value):
        pass

    def get_reviews(self, value):
        pass