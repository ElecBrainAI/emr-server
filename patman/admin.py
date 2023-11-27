from django.contrib import admin
from .models import Patient, Record


class PatientAdmin(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(Patient, PatientAdmin)
admin.site.register(Record)
