from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=40)
    dosage = models.CharField(max_length=10)
    manufacturer = models.CharField(max_length=40,null=True)
    composition = models.CharField(max_length=40,null=True)
    medicine_image = models.ImageField(upload_to='medicines/')

    def __str__(self):
        return self.name + ' - ' + self.dosage