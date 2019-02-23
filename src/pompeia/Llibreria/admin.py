from django.contrib import admin
from .models import *

admin.site.register(Encuadernació)
admin.site.register(Idioma)
admin.site.register(Tema)
admin.site.register(Ciutat)
admin.site.register(CoŀleccióNom)
admin.site.register(Departament)
admin.site.register(Editorial)
admin.site.register(Observacions)
admin.site.register(Autor)
admin.site.register(Representant)
admin.site.register(Traductor)
admin.site.register(Adreça)
admin.site.register(Coŀlecció)
admin.site.register(Proveïdor)

@admin.register(Albarà)
class AlbaràAdmin(admin.ModelAdmin):
    fields = ('proveïdor', 'data', 'tipus', 'número')
    list_display = fields
#   list_editable = ('tipus',)

admin.site.register(Catàleg)
admin.site.register(MetaLlibre)
admin.site.register(Llibre)
