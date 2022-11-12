from api.search.views import TrendingSearchView, RecentSearchViewSet, delete_all_view
from django.urls import path

recent_search = RecentSearchViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
recent_search_detail = RecentSearchViewSet.as_view({
    'delete': 'destroy',
    # 'get': 'retrieve',
})

urlpatterns = [
    path('', recent_search, name='review'),
    path('<int:pk>/', recent_search_detail, name='review_detail'),
    path('trending/', TrendingSearchView.as_view(), name='review_detail'),
    path('delete-all/', delete_all_view, name='delete_all'),
]
