from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=64)
    district = models.CharField(max_length=40)
    number = models.IntegerField(null=True)
    date_birth = models.DateField()
    phone = models.CharField(max_length=15,null=True,unique=True)
    cpf = models.CharField(max_length=11,null=True,unique=True)

    def __str__(self):
        return self.name + ' - ' + self.street