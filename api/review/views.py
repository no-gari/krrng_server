from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import HospitalReviewSerializer
from rest_framework import viewsets
from .models import HospitalReview


class HospitalReviewSet(viewsets.ModelViewSet):
    serializer_class = HospitalReviewSerializer
    queryset = HospitalReview.objects.all()
    lookup_field = 'pk'

    def get_permissions(self):
        permission_classes = [AllowAny]
        if self.action == 'create' or 'update' or 'partial_update' or 'destroy':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
