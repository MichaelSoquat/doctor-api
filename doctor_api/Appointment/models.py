from django.db import models
from datetime import date, timezone

from Doctor.models import Doctor
from Patient.models import Patient

# Create your models here.
class Appointment(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


    def __str__(self):
        return '{0}'.format(self.title)
