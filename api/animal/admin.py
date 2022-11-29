from django.contrib import admin
from .models import Animal, AnimalKind, SortAnimal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass


@admin.register(AnimalKind)
class AnimalKindAdmin(admin.ModelAdmin):
    pass
