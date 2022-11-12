from .models import TrendingSearch, RecentSearch
from rest_framework import serializers


class TrendingSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendingSearch
        exclude = ('ranking',)


class RecentSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentSearch
        exclude = ('user',)

    def create(self, validated_data):
        recent_keyword = RecentSearch.objects.create(
            user=self.context['request'].user,
            keyword=self.validated_data.get('keyword'),
        )
        return recent_keyword
