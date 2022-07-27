from django.contrib import admin

from Patient.models import Patient
from .models import Appointment

# Register your models here.
admin.site.register(Appointment)