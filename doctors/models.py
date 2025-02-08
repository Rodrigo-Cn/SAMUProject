from django.db import models
from django.contrib.auth.models import User
from administrators.models import Administrator

class Doctor(User):
    name = models.CharField(max_length=40)
    crm = models.CharField(unique=True,max_length=6)
    def __str__(self):
        return self.name + ' - ' + self.crm