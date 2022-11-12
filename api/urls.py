from drf_yasg.views import get_schema_view
from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title=f'{settings.SITE_NAME} API',
        default_version='v1',
        description="Test description",
    ),
    public=False,
)


urlpatterns = [
    path('user/', include('api.user.urls')),
    path('animal/', include('api.animal.urls')),
    path('review/', include('api.review.urls')),
    path('search/', include('api.search.urls')),
    path('disease/', include('api.disease.urls')),
    path('cs/', include('api.customerservice.urls')),
]
