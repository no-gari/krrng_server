from rest_framework import serializers
from .models import Symptom, Disease


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ('name', 'id', )


class Symptomerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ('name', 'id', )
