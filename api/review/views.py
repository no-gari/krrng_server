from .serializers import HospitalReviewSerializer, HospitalReviewCreateSerializer, HospitalReviewLikeSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from .models import HospitalReview


class HospitalReviewListView(ListAPIView):
    serializer_class = HospitalReviewSerializer

    def get_queryset(self):
        HospitalReview.objects.all()
        hospital_id = int(self.request.query_params.get('hospital'))
        return HospitalReview.objects.prefetch_related(
            'like_users__profile_set', 'hospitalreviewimage_set'
        ).select_related('hospital').filter(hospital_id=hospital_id)


class HospitalReviewCreateView(CreateAPIView):
    serializer_class = HospitalReviewCreateSerializer
    queryset = HospitalReview.objects.all()
    permission_classes = [IsAuthenticated]


class MyReviewListView(ListAPIView):
    serializer_class = HospitalReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HospitalReview.objects.prefetch_related(
            'like_users__profile_set', 'hospitalreviewimage_set'
        ).filter(user=self.request.user)


class HospitalReviewSet(viewsets.ModelViewSet):
    serializer_class = HospitalReviewSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        permission_classes = [AllowAny]
        if self.action == 'create' or 'update' or 'partial_update' or 'destroy':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return HospitalReview.objects.prefetch_related('like_users')

    def list(self, request, *args, **kwargs):
        queryset = HospitalReview.objects.filter(hospital_id=self.kwargs['pk'])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ReviewLikeUpdateView(RetrieveUpdateAPIView):
    queryset = HospitalReview.objects.prefetch_related('like_users').all()
    serializer_class = HospitalReviewLikeSerializer
    allowed_methods = ['put', 'get']
    lookup_field = 'id'
