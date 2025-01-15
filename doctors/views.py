from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Doctor
from .serializers import DoctorSerializer
from .paginations import DoctorPagination

class DoctorView(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        if name:
            doctors = Doctor.objects.filter(name__icontains=name)
        else:
            doctors = Doctor.objects.all()
        paginator = DoctorPagination()
        page = paginator.paginate_queryset(doctors, request)
        doctors_serializer = DoctorSerializer(page, many=True)
        return paginator.get_paginated_response(doctors_serializer.data)
    
    def post(self, request):
        doctor_serializer = DoctorSerializer(data=request.data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return Response(doctor_serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorViewDetail(APIView):
    def get(self, request, id):
        doctor = get_object_or_404(Doctor, pk=id)
        doctor_serializer = DoctorSerializer(doctor)
        return Response(doctor_serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        doctor = get_object_or_404(Doctor, pk=id)
        doctor_serializer = DoctorSerializer(doctor, data=request.data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return Response(doctor_serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        doctor = get_object_or_404(Doctor, pk=id)
        doctor.delete()
        return Response({"message": "Médico deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)
