from .views import get_total_point, PointLogListView
from django.urls import path


urlpatterns = [
    path('', get_total_point, name='total_point'),
    path('list/', PointLogListView.as_view(), name='point_log'),
]
