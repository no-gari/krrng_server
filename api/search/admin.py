from django.contrib import admin
from api.search.models import RecentSearch, TrendingSearch


@admin.register(TrendingSearch)
class TrendingSearchAdmin(admin.ModelAdmin):
    pass


# @admin.register(RecentSearch)
# class DiseaseAdmin(admin.ModelAdmin):
#     pass
