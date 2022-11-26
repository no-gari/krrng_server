from api.animal.models import Animal
from rest_framework import serializers


class AnimalSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=False)

    class Meta:
        model = Animal
        exclude = ('user',)

    def create(self, validated_data):
        return validated_data