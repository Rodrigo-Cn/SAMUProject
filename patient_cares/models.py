from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from medicines.models import Medicine

class Patient_care(models.Model):
    date = models.DateField()
    hour = models.TimeField()
    location = models.CharField(max_length=70, null=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ManyToManyField(Doctor)
    medicine = models.ManyToManyField(Medicine)
