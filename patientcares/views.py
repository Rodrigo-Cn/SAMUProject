from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import PatientCare
from .paginations import PatientCarePagination
from .serializers import PatientCareSerializer

class PatientCareView(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        if name:
            patientcares = PatientCare.objects.filter(name_icontains=name)
        else:
            patientcares = PatientCare.objects.all()
        pagination = PatientCarePagination
        page = pagination.paginate_queryset(patientcares, request)
        patientcaresserializer = PatientCareSerializer(page, many=True)
        return Response(patientcaresserializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        patientcaresserializer = PatientCareSerializer(request.data)
        if patientcaresserializer.is_valid():
            patientcaresserializer.save()
            return Response(patientcaresserializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class PatientCareViewDetail(APIView):
    def get(self, request, id):
        patientcare = get_object_or_404(PatientCare, pk=id)
        patientcareserializer = PatientCareSerializer(patientcare)
        return Response(patientcareserializer.data, status=status.HTTP_202_ACCEPTED)
    
    def put(self, request, id):
        patientcare = get_object_or_404(PatientCare, pk=id)
        patientcareserializer = PatientCareSerializer(patientcare , request.data)
        if patientcareserializer.is_valid():
            patientcareserializer.save()
            return Response(patientcareserializer.data, status=status.HTTP_200_OK)  
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)  
    
    def delete(self, request, id):
        patientcare = get_object_or_404(PatientCare, pk=id)
        patientcare.delete()
        return Response({"message": "Atendimento deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)