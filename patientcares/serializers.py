from rest_framework import serializers
from .models import PatientCare

class PatientCareSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientCare
        field = '__all__'