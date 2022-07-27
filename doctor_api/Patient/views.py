from django.shortcuts import render
from rest_framework import serializers, viewsets

from .serializers import PatientSerializer

from .models import Patient


class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

