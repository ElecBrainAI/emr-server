from django.contrib import admin
from .models import Patient, Nok, Dept, Doctor, Nurse, Therapist, Admin, Calender, ExcerTherapy, PersonTherapy, DailyLife, Perception, Sense, Physical, Muscular, Cardiopulmonary, Flexibility, Quickness, Hospitalization, Reservation, Diagnosis, Record




# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Patient, PatientAdmin)
admin.site.register(Nok)
admin.site.register(Dept)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Therapist)
admin.site.register(Admin)
admin.site.register(Calender)
admin.site.register(ExcerTherapy)
admin.site.register(PersonTherapy)
admin.site.register(DailyLife)
admin.site.register(Perception)
admin.site.register(Sense)
admin.site.register(Physical)
admin.site.register(Muscular)
admin.site.register(Cardiopulmonary)
admin.site.register(Flexibility)
admin.site.register(Quickness)
admin.site.register(Hospitalization)
admin.site.register(Reservation)
admin.site.register(Diagnosis)
admin.site.register(Record)