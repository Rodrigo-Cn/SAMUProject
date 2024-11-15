from django.db import models

class Patient_care(models.Model):
    date = models.DateField()
    hour = models.TimeField()
    location = models.CharField(max_length=70, null=True)
