from rest_framework import serializers
from .models import BasicDetails, Education

class EducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class BasicDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = BasicDetails
        fields = '__all__'
