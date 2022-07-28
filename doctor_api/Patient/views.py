from django.shortcuts import render
from rest_framework import serializers, viewsets

from .serializers import PatientSerializer
from rest_framework.response import Response
from .models import Patient


class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def destroy(self, request, *args, **kwargs):
        task_object = self.get_object()
        task_object.delete()
        return Response('Object deleted')