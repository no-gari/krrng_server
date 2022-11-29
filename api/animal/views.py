from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from api.animal.serializers import AnimalSerializer, AnimalKindSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import ValidationError
from api.animal.models import Animal, AnimalKind
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class AnimalListView(ListAPIView):
    model = Animal
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_animal = Animal.objects.filter(user=self.request.user)
        return user_animal

    def list(self, request, **kwargs):
        if not request.user.is_authenticated:
            return Response({'error_msg': '로그인 후 이용해주세요,'}, status=status.HTTP_400_BAD_REQUEST)
        return super().list(request, **kwargs)


class AnimalKindListView(ListAPIView):
    model = AnimalKind
    serializer_class = AnimalKindSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        id = int(self.request.query_params.get('id'))
        return AnimalKind.objects.prefetch_related('sort_animal').filter(sort_animal_id=id)


class AnimalRetreiveUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    allowed_methods = ['GET', 'PUT', 'DELETE']
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
        new_animal = Animal.objects.create(
            user=request.user,
            sort=request.data.get('sort'),
            birthday=request.data.get('birthday'),
            weight=request.data.get('weight'),
            kind=request.data.get('kind'),
            hospital_address=request.data.get('hospital_address'),
            hospital_address_detail=request.data.get('hospital_address_detail'),
            interested_disease=request.data.get('interested_disease'),
            neuter_choices=request.data.get('neuter_choices'),
            has_alergy=request.data.get('has_alergy'),
            sex_choices=request.data.get('sex_choices'),
            image=request.FILES.get('image')
        )
        new_animal.save()
        return Response(status=status.HTTP_200_OK)
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
