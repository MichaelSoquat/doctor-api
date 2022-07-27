from rest_framework import routers, serializers, viewsets

from .models import Patient

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Patient
        fields = ['first_name', 'last_name', 'email', 'phone']