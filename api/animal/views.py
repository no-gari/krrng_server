from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.exceptions import ValidationError
from api.animal.serializers import AnimalSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.animal.models import Animal
from rest_framework import status


class AnimalListView(ListAPIView):
    model = Animal
    serializer_class = AnimalSerializer

    def get_queryset(self):
        user_animal = Animal.objects.filter(user=self.request.user)
        return user_animal

    def list(self, request, **kwargs):
        if not request.user.is_authenticated:
            return Response({'error_msg': '로그인 후 이용해주세요,'}, status=status.HTTP_400_BAD_REQUEST)
        return super().list(request, **kwargs)


class AnimalRetreiveUpdateView(RetrieveUpdateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    allowed_methods = ['GET', 'PUT']
    lookup_field = 'pk'
    model = Animal

    def retrieve(self, request, **kwargs):
        if not request.user.is_authenticated:
            return Response({'error_msg': '로그인 후 이용해주세요,'}, status=status.HTTP_400_BAD_REQUEST)
        return super().retrieve(self, request, **kwargs)

    def patch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'error_msg': '로그인 후 이용해주세요,'}, status=status.HTTP_400_BAD_REQUEST)
        return super().patch(request, *args, **kwargs)


@api_view(["POST"])
def create_animal(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return Response({'error_msg': '로그인 후 이용해주세요,'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        serializer_data = AnimalSerializer(request.data).data
        new_animal = Animal.objects.create(
            user=request.user,
            sort=serializer_data.get('sort'),
            birthday=serializer_data.get('birthday'),
            weight=serializer_data.get('weight'),
            kind=serializer_data.get('kind'),
            hospital_address=serializer_data.get('hospital_address'),
            hospital_address_detail=serializer_data.get('hospital_address_detail'),
            interested_disease=serializer_data.get('interested_disease'),
            neuter_choices=serializer_data.get('neuter_choices'),
            has_alergy=serializer_data.get('has_alergy'),
            sex_choices=serializer_data.get('sex_choices'),
        )
        new_animal.save()
        return Response(AnimalSerializer(new_animal).data, status=status.HTTP_200_OK)
    except:
        return ValidationError({'error_msg': '다시 한 번 시도 해주세요.'})


@api_view(["DELETE"])
def delete_Animal(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return Response({'error_msg': '로그인 후 이용해주세요,'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        id = int(request.data.get('id'))
        user_animal = Animal.objects.get(id=id)
        user_animal.delete()
        return Response(status=status.HTTP_200_OK)
    except:
        return ValidationError({'error_msg': '다시 한 번 시도 해주세요.'})
