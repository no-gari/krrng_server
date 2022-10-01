from django.contrib import admin
from .models import  Hospital, HopitalPrice, BestPart, AvailableAnimal


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    pass


@admin.register(HopitalPrice)
class HospitalPriceAdmin(admin.ModelAdmin):
    pass


@admin.register(BestPart)
class BestPartAdmin(admin.ModelAdmin):
    pass


@admin.register(AvailableAnimal)
class AvailableAnimalAdmin(admin.ModelAdmin):
    pass
