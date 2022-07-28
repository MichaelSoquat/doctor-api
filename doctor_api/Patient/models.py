from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Patient(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.BigIntegerField()
    


    def __str__(self):
        return self.last_name
