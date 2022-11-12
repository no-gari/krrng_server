from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import HospitalReviewSerializer
from rest_framework.response import Response
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

    def list(self, request, *args, **kwargs):
        queryset = HospitalReview.objects.filter(hospital_id=self.kwargs['pk'])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
