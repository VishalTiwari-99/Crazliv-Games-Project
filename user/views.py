from django.shortcuts import render
from rest_framework import viewsets
from .models import Education, BasicDetails
from .serializers import EducationSerializers, BasicDetailsSerializers
from rest_framework import generics
from rest_framework.permissions import AllowAny

class ListEducation(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializers
    permission_classes = [AllowAny]

class ListDetails(generics.ListAPIView):
    queryset = BasicDetails.objects.all()
    serializer_class = BasicDetailsSerializers
    permission_classes = [AllowAny]

class EducationViewset(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializers

class DetailsViewset(viewsets.ModelViewSet):
    queryset = BasicDetails.objects.all()
    serializer_class = BasicDetailsSerializers


