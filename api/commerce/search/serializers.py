from rest_framework import serializers
from api.commerce.models import SearchKeywords


class SearchKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchKeywords
        fields = ['keywords', 'order', 'id']
