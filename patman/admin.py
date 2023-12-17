from django.contrib import admin

from .models import Patient, Nok, Dept, Doctor, Nurse, Therapist, Admin, Calender, ExcerTherapy, PersonTherapy, DailyLife, Perception, Sense, Physical, Muscular, Cardiopulmonary, Flexibility, Quickness, Hospitalization, Reservation, Diagnosis, Record, Questionnaire, Inbody, Xray, Authority, PatientAuthority, NokAuthority, DoctorAuthority, NurseAuthorization, TherapistAuthority, ManagerAuthority, Equipment, EquipmentRental, RehabilitationEquipment, UseRehabilitationEquipment

from .models import UploadImage, UploadVideo

admin.site.register(UploadImage)
admin.site.register(UploadVideo)

# Register your models here.

class ModelAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Patient, ModelAdmin)
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
admin.site.register(Questionnaire)
admin.site.register(Inbody)
admin.site.register(Xray)
admin.site.register(Authority)
admin.site.register(PatientAuthority)
admin.site.register(NokAuthority)
admin.site.register(DoctorAuthority)
admin.site.register(NurseAuthorization)
admin.site.register(TherapistAuthority)
admin.site.register(ManagerAuthority)
admin.site.register(Equipment)
admin.site.register(EquipmentRental)
admin.site.register(RehabilitationEquipment)
admin.site.register(UseRehabilitationEquipment)