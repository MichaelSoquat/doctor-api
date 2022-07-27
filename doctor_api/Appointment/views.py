from django.shortcuts import render
from rest_framework import serializers, viewsets

from Patient.models import Patient
from Patient.serializers import PatientSerializer
# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    pass
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer