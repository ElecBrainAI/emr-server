from django.db import models

# Create your models here.
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