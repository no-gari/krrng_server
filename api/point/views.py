from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PointSerializer
from rest_framework import status
from django.db.models import Sum
from .models import PointLog
import json


@api_view(['GET'])
def get_total_point(request):
    if not request.user.is_authenticated:
        raise ValidationError()
    user = request.user
    total_point = PointLog.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum']
    if total_point is None:
        total_point = 0
    return Response({'total_point': total_point}, status=status.HTTP_200_OK)


class PointLogListView(ListAPIView):
    serializer_class = PointSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PointLog.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        new_json = {}
        data = super().list(request, *args, **kwargs).data
        json_str = json.dumps(data)
        json_object = json.loads(json_str)
        user = self.request.user
        total_point = PointLog.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum']
        if total_point is None:
            total_point = 0
        new_json['total_point'] = total_point
        new_json['points'] = json_object
        return Response(new_json, status=status.HTTP_200_OK)
