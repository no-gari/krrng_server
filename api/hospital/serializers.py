from rest_framework import serializers
from .models import BestPart, AvailableAnimal, HospitalPrice, Hospital, HospitalImage


class BestPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestPart
        fields = ('name', )


class AvailableAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableAnimal
        fields = ('name', )


class HospitalSearchSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    recommend_number = serializers.CharField(read_only=True)
    distance = serializers.CharField(read_only=True)
    review_count = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = Hospital
        fields = ('name', 'address', 'recommend_number', )


# class HospitalSerializer(serializers.ModelSerializer):
#     class Meta:
