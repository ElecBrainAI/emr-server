# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Record(models.Model):
    record_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    patient_id = models.IntegerField(blank=True, null=True)
    symptoms = models.CharField(max_length=38, blank=True, null=True)
    diagnostics = models.CharField(max_length=38, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'record'


class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    reg_date = models.DateField()
    note = models.TextField()

    class Meta:
        managed = True
        db_table = 'patient'

    def __str__(self):
        return str(self.id)