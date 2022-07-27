from django.shortcuts import render
from rest_framework import serializers, viewsets

from Patient.models import Patient
from Patient.serializers import PatientSerializer
from .serializers import AppointmentSerializer
from .models import Appointment
# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer