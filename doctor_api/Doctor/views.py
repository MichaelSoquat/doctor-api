from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    pass
    # queryset = User.objects.all()
    # serializer_class = UserSerializer