from django.contrib import admin
from .models import PointLog


@admin.register(PointLog)
class PointLogAdmin(admin.ModelAdmin):
    pass
