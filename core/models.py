from django.db import models


class Patient(models.Model):
    patient_id = models.CharField(primary_key=True, max_length=50)
    patient_name = models.CharField(max_length=10)
    patient_birthday = models.CharField(max_length=8)
    patient_tel = models.CharField(max_length=20)
    patient_gender = models.CharField(max_length=10)
    patient_home = models.CharField(max_length=100, blank=True, null=True)
    patient_accept_id = models.CharField(max_length=50, blank=True, null=True)
    patient_hos = models.IntegerField()
    patient_pw = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'


class Nok(models.Model):
    protector_id = models.CharField(primary_key=True, max_length=50)  # The composite primary key (protector_id, patient_id) found, that is not supported. The first column is selected.
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    protector_nm = models.CharField(max_length=10)
    protector_tel = models.CharField(max_length=20)
    protector_gender = models.CharField(max_length=10)
    protector_birth_day = models.CharField(max_length=8)
    protector_pw = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'nok'
        unique_together = (('protector_id', 'patient'),)




class Dept(models.Model):
    dept_id = models.CharField(primary_key=True, max_length=50)
    dept_nm = models.CharField(max_length=10)
    dept_res_id = models.CharField(max_length=50, blank=True, null=True)
    staff_num = models.BigIntegerField(blank=True, null=True)
    dept_tel = models.CharField(max_length=20, blank=True, null=True)
    dept_mail = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dept'



class Doctor(models.Model):
    doctor_id = models.CharField(primary_key=True, max_length=50)
    doctor_nm = models.CharField(max_length=10)
    doctor_tel = models.CharField(max_length=20)
    doctor_gender = models.CharField(max_length=10)
    doctor_med_field = models.CharField(max_length=40)
    dept = models.ForeignKey('Dept', models.DO_NOTHING, blank=True, null=True)
    doctor_salary = models.IntegerField()
    doctor_pw = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'doctor'



class Nurse(models.Model):
    nurse_id = models.CharField(primary_key=True, max_length=50)
    nurse_salery = models.IntegerField()
    nurse_name = models.CharField(max_length=10)
    nurse_tel = models.CharField(max_length=20)
    nurse_gender = models.CharField(max_length=10)
    nurse_med_field = models.CharField(max_length=40)
    nurse_m_work = models.CharField(max_length=40)
    dept = models.ForeignKey('Dept', models.DO_NOTHING, blank=True, null=True)
    nurse_pw = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'nurse'



class Therapist(models.Model):
    therapist_id = models.CharField(primary_key=True, max_length=50)
    therapist_salery = models.IntegerField()
    therapist_nm = models.CharField(max_length=10)
    therapist_tel = models.CharField(max_length=20)
    therapist_gender = models.CharField(max_length=10)
    therapist_m_work = models.CharField(max_length=40)
    dept = models.ForeignKey('Dept', models.DO_NOTHING, blank=True, null=True)
    therapist_pw = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'therapist'



class Admin(models.Model):
    admin_id = models.CharField(primary_key=True, max_length=50)
    admin_name = models.CharField(max_length=10)
    admin_pw = models.CharField(max_length=100)
    admin_tel = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'admin'



class Calender(models.Model):
    patient = models.OneToOneField('Patient', models.DO_NOTHING, primary_key=True)
    treatment_plan = models.CharField(max_length=255, blank=True, null=True)
    plan_date = models.DateTimeField()
    plan_diet = models.CharField(max_length=255, blank=True, null=True)
    plan_more_detail = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calender'



class ExcerTherapy(models.Model):
    treatment_id = models.CharField(primary_key=True, max_length=50)  # The composite primary key (treatment_id, patient_id) found, that is not supported. The first column is selected.
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    reh_goal = models.CharField(max_length=255)
    reh_therapy_date = models.CharField(max_length=17)
    use_drug = models.CharField(max_length=255)
    therapy_plan = models.CharField(max_length=255)
    therapy_point = models.CharField(max_length=255)
    therapist = models.ForeignKey('Therapist', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'excer_therapy'
        unique_together = (('treatment_id', 'patient'),)



class PersonTherapy(models.Model):
    treatment_id = models.CharField(primary_key=True, max_length=50)  # The composite primary key (treatment_id, patient_id) found, that is not supported. The first column is selected.
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    reh_goal = models.CharField(max_length=255)
    reh_therapy_date = models.CharField(max_length=17)
    use_drug = models.CharField(max_length=255)
    therapy_plan = models.CharField(max_length=255)
    therapy_point = models.CharField(max_length=255)
    therapist = models.ForeignKey('Therapist', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_therapy'
        unique_together = (('treatment_id', 'patient'),)


class DailyLife(models.Model):
    treatment = models.OneToOneField('PersonTherapy', models.DO_NOTHING, primary_key=True)  # The composite primary key (treatment_id, patient_id) found, that is not supported. The first column is selected.
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    daily_wash = models.CharField(max_length=50, blank=True, null=True)
    daily_eat = models.CharField(max_length=50, blank=True, null=True)
    daily_clothes = models.CharField(max_length=50, blank=True, null=True)
    daily_toilet = models.CharField(max_length=50, blank=True, null=True)
    daily_move = models.CharField(max_length=50, blank=True, null=True)
    daily_yn = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_life'
        unique_together = (('treatment', 'patient'),)



class Perception(models.Model):
    treatment = models.OneToOneField('PersonTherapy', models.DO_NOTHING, primary_key=True)  # The composite primary key (treatment_id, patient_id) found, that is not supported. The first column is selected.
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    percep_see = models.CharField(max_length=50, blank=True, null=True)
    percep_body = models.CharField(max_length=50, blank=True, null=True)
    percep_con = models.CharField(max_length=50, blank=True, null=True)
    percep_re = models.CharField(max_length=50, blank=True, null=True)
    percep_jud = models.CharField(max_length=50, blank=True, null=True)
    percep_solve = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perception'
        unique_together = (('treatment', 'patient'),)



class Sense(models.Model):
    treatment = models.OneToOneField('PersonTherapy', models.DO_NOTHING, primary_key=True)  # The composite primary key (treatment_id, patient_id) found, that is not supported. The first column is selected.
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    sense_touch = models.IntegerField(blank=True, null=True)
    sense_ache = models.IntegerField(blank=True, null=True)
    sense_loc = models.IntegerField(blank=True, null=True)
    sense_origin = models.IntegerField(blank=True, null=True)
    sense_see = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sense'
        unique_together = (('treatment', 'patient'),)


class Physical(models.Model):
    treatment = models.OneToOneField('PersonTherapy', models.DO_NOTHING, primary_key=True)  # The composite primary key (treatment_id, patient_id) found, that is not supported. The first column is selected.
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    phy_range = models.CharField(max_length=50, blank=True, null=True)
    phy_strong = models.IntegerField(blank=True, null=True)
    phy_ability = models.CharField(max_length=50, blank=True, null=True)
    phy_degree = models.IntegerField(blank=True, null=True)
    phy_hand = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physical'
        unique_together = (('treatment', 'patient'),)



class Muscular(models.Model):
    treatment = models.OneToOneField('ExcerTherapy', models.DO_NOTHING, primary_key=True)  # The composite primary key (treatment_id, patient_id) found, that is not supported. The first column is selected.
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    mus_health = models.CharField(max_length=50)
    mus_trial = models.IntegerField()
    mus_value = models.IntegerField()
    mus_zvalue = models.IntegerField()
    mus_number = models.IntegerField()
    mus_media = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'muscular'
        unique_together = (('treatment', 'patient'),)



class Cardiopulmonary(models.Model):
    treatment = models.OneToOneField('ExcerTherapy', models.DO_NOTHING, primary_key=True)  # The composite primary key (treatment_id, patient_id) found, that is not supported. The first column is selected.
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    cardi_health = models.CharField(max_length=50)
    cardi_trial = models.IntegerField()
    cardi_value = models.IntegerField()
    cardi_zvalue = models.IntegerField()
    cardi_number = models.IntegerField()
    cardi_media = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cardiopulmonary'
        unique_together = (('treatment', 'patient'),)


class Flexibility(models.Model):
    treatment = models.OneToOneField('ExcerTherapy', models.DO_NOTHING, primary_key=True)  # The composite primary key (treatment_id, patient_id) found, that is not supported. The first column is selected.
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    flex_health = models.CharField(max_length=50)
    flex_trial = models.IntegerField()
    flex_value = models.IntegerField()
    flex_zvalue = models.IntegerField()
    flex_number = models.IntegerField()
    flex_media = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'flexibility'
        unique_together = (('treatment', 'patient'),)



class Quickness(models.Model):
    treatment = models.OneToOneField('ExcerTherapy', models.DO_NOTHING, primary_key=True)  # The composite primary key (treatment_id, patient_id) found, that is not supported. The first column is selected.
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    quick_health = models.CharField(max_length=50)
    quick_trial = models.IntegerField()
    quick_value = models.IntegerField()
    quick_zvalue = models.IntegerField()
    quick_number = models.IntegerField()
    quick_media = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'quickness'
        unique_together = (('treatment', 'patient'),)



class Hospitalization(models.Model):
    patient = models.OneToOneField('Patient', models.DO_NOTHING, primary_key=True)
    patient_date = models.CharField(max_length=17)
    hospital_room_id = models.CharField(max_length=50)
    hospital_room_info = models.CharField(max_length=100, blank=True, null=True)
    hospital_bed_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'hospitalization'



class Reservation(models.Model):
    res_id = models.CharField(primary_key=True, max_length=50)
    res_type = models.CharField(max_length=100)
    res_time = models.DateTimeField()
    pick_up = models.IntegerField()
    pick_place = models.CharField(max_length=255, blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservation'



class Diagnosis(models.Model):
    diag_id = models.CharField(primary_key=True, max_length=50)
    doctor_id = models.CharField(max_length=50, blank=True, null=True)
    diseases = models.CharField(max_length=100, blank=True, null=True)
    main_pain = models.CharField(max_length=255, blank=True, null=True)
    d_of_diseases = models.CharField(max_length=100, blank=True, null=True)
    therapy_select = models.IntegerField(blank=True, null=True)
    field = models.CharField(max_length=100, blank=True, null=True)
    diseases_time = models.CharField(max_length=17, blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diagnosis'



class Record(models.Model):
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    record_id = models.CharField(primary_key=True, max_length=50)  # The composite primary key (record_id, patient_id) found, that is not supported. The first column is selected.
    medical_date = models.DateTimeField()
    therapist = models.ForeignKey('Therapist', models.DO_NOTHING)
    diag = models.ForeignKey('Diagnosis', models.DO_NOTHING)
    doctor = models.ForeignKey('Doctor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'record'
        unique_together = (('record_id', 'patient'),)

