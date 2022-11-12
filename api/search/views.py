from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import RecentSearchSerializer, TrendingSearchSerializer
from .models import RecentSearch, TrendingSearch
from rest_framework import viewsets
from rest_framework.generics import ListAPIView


class RecentSearchViewSet(viewsets.ModelViewSet):
    serializer_class = RecentSearchSerializer
    queryset = RecentSearch.objects.all()
    lookup_field = 'pk'

    def get_permissions(self):
        permission_classes = [AllowAny]
        if self.action == 'create' or 'update' or 'partial_update' or 'destroy':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class TrendingSearchView(ListAPIView):
    serializer_class = TrendingSearchSerializer
    queryset = TrendingSearch.objects.all().order_by('ranking')
