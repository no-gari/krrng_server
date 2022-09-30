from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('api/v1/', include('api.urls')),
    path('api/admin/', admin.site.urls),
]
