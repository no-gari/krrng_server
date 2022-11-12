from django.contrib import admin
from .models import Hospital, HospitalPrice, BestPart, AvailableAnimal
from api.disease.models import Disease, Symptoms


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    pass


@admin.register(HospitalPrice)
class HospitalPriceAdmin(admin.ModelAdmin):
    pass


@admin.register(BestPart)
class BestPartAdmin(admin.ModelAdmin):
    pass


@admin.register(AvailableAnimal)
class AvailableAnimalAdmin(admin.ModelAdmin):
    pass


@admin.register(Symptoms)
class SymptomsAdmin(admin.ModelAdmin):
    pass


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    pass
