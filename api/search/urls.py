from api.search.views import TrendingSearchView, RecentSearchViewSet
from django.urls import path

recent_search = RecentSearchViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
recent_search_detail = RecentSearchViewSet.as_view({
    'delete': 'delete'
})

urlpatterns = [
    path('', recent_search, name='review'),
    path('<int:pk>/', recent_search_detail, name='review_detail'),
    path('trending/', TrendingSearchView.as_view(), name='review_detail'),
]
