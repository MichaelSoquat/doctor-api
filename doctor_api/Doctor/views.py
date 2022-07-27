from django.shortcuts import render
from rest_framework import serializers, viewsets

from .serializers import DoctorSerializer

from .models import Doctor
# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer