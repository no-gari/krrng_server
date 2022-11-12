from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import RecentSearchSerializer, TrendingSearchSerializer
from .models import RecentSearch, TrendingSearch
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.exceptions import ValidationError
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response


class RecentSearchViewSet(viewsets.ModelViewSet):
    serializer_class = RecentSearchSerializer
    queryset = RecentSearch.objects.all()
    lookup_field = 'pk'

    def get_permissions(self):
        permission_classes = [AllowAny]
        if self.action == 'create' or 'update' or 'partial_update' or 'destroy':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


@api_view(['DELETE'])
def delete_all_view(request):
    if not request.method == 'DELETE':
        raise ValidationError()
    if request.user.is_authenticated:
        del_objects = RecentSearch.objects.filter(user=request.user)
        for del_object in del_objects:
            del_object.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class TrendingSearchView(ListAPIView):
    serializer_class = TrendingSearchSerializer
    queryset = TrendingSearch.objects.all().order_by('ranking')
