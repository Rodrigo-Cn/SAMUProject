from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from medicines.models import Medicine

class PatientCare(models.Model):
    date = models.DateField()
    hour = models.TimeField()
    city = models.CharField(max_length=40, default="Guanambi - Bahia") 
    street = models.CharField(max_length=64, default="Rua")
    district = models.CharField(max_length=40, default="Bairro")
    number = models.IntegerField(null=True, blank=True) 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    medicine = models.ManyToManyField(Medicine, blank=True)
    def __str__(self):
        return f"Atendimento {self.date} - {self.patient}"
