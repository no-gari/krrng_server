from api.animal.models import Animal, AnimalKind, SortAnimal
from rest_framework import serializers


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        exclude = ('user',)


class AnimalCreateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Animal
        exclude = ('image', )

    def get_user(self, obj):
        return self.context['request'].user.id

    def create(self, attrs):
        return attrs


class SortAnimalSerializer(serializers.ModelSerializer):
    kinds = serializers.SerializerMethodField()

    class Meta:
        model = SortAnimal
        fields = ('sort', 'kinds')

    def get_kinds(self, obj):
        return AnimalKindSerializer(obj.animalkind_set.all(), many=True).data


class AnimalKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalKind
        exclude = ('sort_animal', )
