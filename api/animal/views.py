from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import AnimalSerializers
from .models import Animal


class AnimalCreateAPIView(CreateAPIView):
    serializer_class = AnimalSerializers
    queryset = Animal.objects.all()
    permission_classes = IsAuthenticated

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'status': 200, 'data': response.data})
