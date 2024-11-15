from django.db import models
from django.contrib.auth.models import User

class Administrator(User):
    name = models.CharField(max_length=40)
    position = models.CharField(max_length=40,null=True)
    cpf = models.CharField(max_length=11,unique=True)

    def __str__(self):
        return self.name + ' - ' + self.cpf
