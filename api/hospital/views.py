from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import ValidationError
from collections import OrderedDict
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from .serializers import HospitalListSerializer, BestPartSerializer, AvailableAnimalSerializer, HospitalDetailSerializer
from rest_framework import status
import json
from .models import Hospital, HospitalPrice, HospitalImage
from rest_framework.response import Response


class HospitalListView(ListAPIView):
    serializer_class = HospitalListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        disease = self.request.query_params.get('disease')
        best_part = self.request.query_params.get('bestPart')
        if best_part == '0' and disease == '0':
            hospital_list = Hospital.objects.filter(
                is_visible=True).prefetch_related("hospitalprice_set").prefetch_related("best_part")
        else:
            if best_part == 0:
                hospital_list = Hospital.objects.filter(
                    hospitalprice__disease__in=[int(disease)],
                    is_visible=True
                ).prefetch_related("hospitalprice_set").prefetch_related("best_part")
            elif disease == 0:
                hospital_list = Hospital.objects.filter(
                    best_part__in=[int(best_part)],
                    is_visible=True
                ).prefetch_related("hospitalprice_set").prefetch_related("best_part")
            else:
                hospital_list = Hospital.objects.filter(
                    best_part__in=[int(best_part)],
                    hospitalprice__disease__in=[int(disease)],
                    is_visible=True
                ).prefetch_related("hospitalprice_set").prefetch_related("best_part")
        return hospital_list

    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs).data
        json_str = json.dumps(data)
        json_object = json.loads(json_str)
        sort = request.query_params.get('filter')
        if sort == 'distance':
            new_data = sorted(json_object, key=lambda k: k['distance'], reverse=False)
        elif sort == 'price':
            new_data = sorted(json_object, key=lambda k: k['price'], reverse=False)
        elif sort == 'recommend':
            new_data = sorted(json_object, key=lambda k: k['recommend'], reverse=True)
        else:
            new_data = sorted(json_object, key=lambda k: k['review_count'], reverse=True)
        return Response(new_data, status=status.HTTP_200_OK)


class HospitalSearchView(ListAPIView):
    serializer_class = HospitalListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        hospital_list = Hospital.objects.filter(name__icontains=keyword, is_visible=True).prefetch_related("hospitalprice_set")
        return hospital_list

    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs).data
        json_str = json.dumps(data)
        json_object = json.loads(json_str)
        new_data = sorted(json_object, key=lambda k: k['distance'], reverse=False)
        return Response(new_data, status=status.HTTP_200_OK)


class HospitalDetailView(RetrieveAPIView):
    serializer_class = HospitalDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'

    def get_object(self):
        return Hospital.objects.get(id=self.kwargs['pk'])
