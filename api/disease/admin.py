from django.contrib import admin
from api.disease.models import Disease, Symptom


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    pass


@admin.register(Symptom)
class SymptomsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        disease_list = form.cleaned_data['disease']
        name_list = form.cleaned_data['name'].split(',')
        if len(name_list) > 1:
            for name in name_list:
                new_symptom = Symptom.objects.create(name=name)
                new_symptom.save()
                new_symptom.disease.add(*disease_list)
        return super().save_model(request, obj, form, change)
