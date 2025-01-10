from .models import Medicine
from .serializers import MedicineSerializer
from .paginations import MedicinePagination
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class MedicineView(APIView):
    #permission_classes = [IsAuthenticated]  

    def get(self, request):
        name = request.query_params.get('name')
        if name:
            medicines = Medicine.objects.filter(name__icontains=name)
        else:
            medicines = Medicine.objects.all()
        paginator = MedicinePagination()
        page = paginator.paginate_queryset(medicines, request)
        medicinesserializer = MedicineSerializer(page, many=True)
        return paginator.get_paginated_response(medicinesserializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        medicineserializer = MedicineSerializer(data=request.data)
        if medicineserializer.is_valid():
            medicineserializer.save()
            return Response(medicineserializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(medicineserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class MedicineViewDetail(APIView):
    #permission_classes = [IsAuthenticated]  
    
    def get(self, request, id):
        medicine = get_object_or_404(Medicine ,pk=id)
        medicineserializer = MedicineSerializer(medicine)
        return Response(medicineserializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        medicine = get_object_or_404(Medicine, pk=id)
        medicineserializer = MedicineSerializer(medicine, data=request.data)
        if medicineserializer.is_valid():
            medicineserializer.save()
            return Response(medicineserializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response(medicineserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        medicine = get_object_or_404(Medicine, pk=id)
        medicine.delete()
        return Response({"message": "Medicamento deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)
