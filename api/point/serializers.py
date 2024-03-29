from rest_framework import serializers
from .models import PointLog
from django.db.models import Sum


class TotalPointSerializer(serializers.Serializer):
    total_point = serializers.SerializerMethodField(read_only=True)

    def get_total_point(self):
        user = self.context['request'].user
        return PointLog.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum']


class PointSerializer(serializers.ModelSerializer):
    is_expanded = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PointLog
        exclude = ('user', )

    def get_is_expanded(self, obj):
        return False