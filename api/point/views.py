from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PointSerializer
from rest_framework import status
from django.db.models import Sum
from .models import PointLog


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
