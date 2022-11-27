from api.animal.models import Animal
from rest_framework import serializers


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        exclude = ('user',)
