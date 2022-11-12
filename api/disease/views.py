from rest_framework.generics import ListAPIView
from .models import Disease, Symptom
from .serializers import DiseaseSerializer
from django.db.models import Q


class DiseaseListView(ListAPIView):
    serializer_class = DiseaseSerializer
    lookup_field = 'keyword'

    def get_queryset(self):
        keyword = self.kwargs['keyword']
        disease_list = Disease.objects.filter(
            Q(symptom__name__icontains=keyword)|
            Q(name__icontains=keyword)
        )
        return disease_list
