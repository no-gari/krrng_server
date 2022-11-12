from django.contrib import admin
from api.disease.models import Disease, Symptom


@admin.register(Symptom)
class SymptomsAdmin(admin.ModelAdmin):
    pass


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    pass
