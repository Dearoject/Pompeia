from django.contrib import admin
from .models import Albarà, Proveïdor

@admin.register(Proveïdor)
class ProveïdorAdmin(admin.ModelAdmin):
    pass

@admin.register(Albarà)
class AlbaràAdmin(admin.ModelAdmin):
    fields = ('proveïdor', 'data', 'tipus', 'número')
