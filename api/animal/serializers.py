from api.animal.models import Animal, AnimalKind
from rest_framework import serializers


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        exclude = ('user',)


class AnimalKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalKind
        exclude = ('sort_animal', )
