from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from .serializers import DoctorSerializer

from .models import Doctor
# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def destroy(self, request, *args, **kwargs):
        task_object = self.get_object()
        task_object.delete()
        return Response('Object deleted')