from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Appointment
        fields = ['title', 'description', 'date', 'created_at','doctor','patient']