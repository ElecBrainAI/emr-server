from rest_framework import serializers

from .models import Patient, Nok, Dept, Doctor, Nurse, Therapist, Admin, Calender, ExcerTherapy, PersonTherapy, DailyLife, Perception, Sense, Physical, Muscular, Cardiopulmonary, Flexibility, Quickness, Hospitalization, Reservation, Diagnosis, Record, Questionnaire, Inbody, Xray, Authority, PatientAuthority, NokAuthority, DoctorAuthority, NurseAuthorization, TherapistAuthority, ManagerAuthority, Equipment, EquipmentRental, RehabilitationEquipment, UseRehabilitationEquipment



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class NokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nok
        fields = "__all__"

class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dept
        fields = "__all__"

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = "__all__"

class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = "__all__"

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"

class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = "__all__"

class ExcerTherapySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcerTherapy
        fields = "__all__"

class PersonTherapySerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonTherapy
        fields = "__all__"

class DailyLifeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLife
        fields = "__all__"

class PerceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perception
        fields = "__all__"

class SenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sense
        fields = "__all__"

class PhysicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physical
        fields = "__all__"

class MuscularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscular
        fields = "__all__"

class CardiopulmonarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardiopulmonary
        fields = "__all__"

class FlexibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Flexibility
        fields = "__all__"

class QuicknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quickness
        fields = "__all__"

class HospitalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospitalization
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = "__all__"

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = "__all__"

class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = "__all__"

class InbodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbody
        fields = "__all__"

class XraySerializer(serializers.ModelSerializer):
    class Meta:
        model = Xray
        fields = "__all__"

class AuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Authority
        fields = "__all__"

class PatientAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAuthority
        fields = "__all__"

class NokAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = NokAuthority
        fields = "__all__"

class DoctorAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAuthority
        fields = "__all__"

class NurseAuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NurseAuthorization
        fields = "__all__"

class TherapistAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = TherapistAuthority
        fields = "__all__"

class ManagerAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerAuthority
        fields = "__all__"

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"

class EquipmentRentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentRental
        fields = "__all__"

class RehabilitationEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RehabilitationEquipment
        fields = "__all__"

class UseRehabilitationEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseRehabilitationEquipment
        fields = "__all__"