from rest_framework import serializers
from .models import BestPart, AvailableAnimal, HospitalPrice, Hospital, HospitalReview, HospitalReviewImage, HospitalImage
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView


class HospitalListAPIView(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['name']
