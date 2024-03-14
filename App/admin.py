from django.contrib import admin
from App.models import Patient

class PatientAdmin (admin.ModelAdmin):
    list_display = ['name', 'prename','phone', 'age', 'sexe','cree_nouveau']
    search_fields = ['name', 'prename','phone', 'age', 'sexe']
    list_per_page = 8

admin.site.register(Patient,PatientAdmin)