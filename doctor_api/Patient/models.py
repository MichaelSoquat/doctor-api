from django.db import models


# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.BigIntegerField()
    


    def __str__(self):
        return self.last_name
