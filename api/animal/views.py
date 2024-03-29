from api.animal.serializers import AnimalSerializer, SortAnimalSerializer, AnimalCreateSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import ValidationError
from api.animal.models import Animal, SortAnimal
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
    model = SortAnimal
    serializer_class = SortAnimalSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return SortAnimal.objects.all().prefetch_related('animalkind_set')


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


class AnimalCreateAPIView(CreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalCreateSerializer
    allowed_methods = ['GET', 'POST']
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        new_animal = Animal.objects.create(
            user=request.user,
            name=request.data.get('name'),
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
            image=request.FILES.get('image'),
        )
        new_animal.save()
        kwargs['id'] = new_animal.id
        image = request.FILES.get('image', None)
        if image is not None:
            kwargs['image'] = new_animal.image.url
        else:
            kwargs['image'] = None
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        data = serializer.data
        data['id'] = kwargs['id']
        data['image'] = kwargs['image']
        return Response(data, status=status.HTTP_201_CREATED)


@api_view(["DELETE"])
def delete_animal(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return Response({'error_msg': '로그인 후 이용해주세요,'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        id = int(request.data.get('id'))
        user_animal = Animal.objects.get(id=id)
        user_animal.delete()
        return Response(status=status.HTTP_200_OK)
    except:
        return ValidationError({'error_msg': '다시 한 번 시도 해주세요.'})
