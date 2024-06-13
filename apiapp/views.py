from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import routers, serializers, viewsets
# Create your views here.
class technologiesViewSet(viewsets.ModelViewSet):
    queryset = technologies.objects.all()
    serializer_class = technologiesserializers



class educationViewset(viewsets.ModelViewSet):
    queryset = education.objects.all()
    serializer_class = educationserializers

class experienceViewSet(viewsets.ModelViewSet):
    queryset = experiences.objects.all()
    serializer_class = experienceserializers

class projectViewSet(viewsets.ModelViewSet):
    queryset = projects.objects.all()
    serializer_class = projectserializers