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
        fields = '__all__'

    def get_user(self, obj):
        return self.context['request'].user.id

    def save(self):
        user = self.context['request'].user
        name = self.validated_data.get('name'),
        sort = self.validated_data.get('sort'),
        birthday = self.validated_data.get('birthday'),
        weight = self.validated_data.get('weight'),
        kind = self.validated_data.get('kind'),
        hospital_address = self.validated_data.get('hospital_address'),
        hospital_address_detail = self.validated_data.get('hospital_address_detail'),
        interested_disease = self.validated_data.get('interested_disease'),
        neuter_choices = self.validated_data.get('neuter_choices'),
        has_alergy = self.validated_data.get('has_alergy'),
        sex_choices = self.validated_data.get('sex_choices'),
        image = self.validated_data.get('image')


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
