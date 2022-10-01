from api.commerce.models import CollectionModel, ShippingRequest, SearchKeywords
from django.contrib import admin


@admin.register(CollectionModel)
class PopupAdmin(admin.ModelAdmin):
    pass


@admin.register(ShippingRequest)
class ShippingRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(SearchKeywords)
class SearchKeywordAdmin(admin.ModelAdmin):
    pass
