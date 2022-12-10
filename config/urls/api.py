from api.user.views.find_change_user_info import redirectOneLink
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.conf import settings
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title=f'{settings.SITE_NAME} API',
        default_version='v1',
        description="krrng api v1",
    ),
    public=False,
)


urlpatterns = [
    path('api/v1/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path('', redirectOneLink)
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]