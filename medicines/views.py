from .models import Medicine
from .serializer import MedicineSerializer
from .pagination import MedicinePagination
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class MedicineAPI(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        name = request.query_params.get('name')
        if name:
            medicine = Medicine.objects.filter(name__icontains=name)
        else:
            medicine = Medicine.objects.all()
        paginator = MedicinePagination()
        page = paginator.paginate_queryset(medicine, request)
        medicine_serializer = MedicineSerializer(page, many=True)

        return paginator.get_paginated_response(medicine_serializer.data)
    
    def post(self, request):
        medicineSerializer = MedicineSerializer(data = request.data)
        if medicineSerializer.is_valid():
            medicineSerializer.save()
            return Response(medicineSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(medicineSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class MedicineAPIDetail(APIView):
    permission_classes = [IsAuthenticated]  
    
    def get(self, request, id):
        medicine = get_object_or_404(Medicine ,pk=id)
        medicineSerializer = MedicineSerializer(medicine)
        return Response(medicineSerializer.data)
    
    def put(self, request, id):
        medicine = get_object_or_404(Medicine, pk=id)
        medicineSerializer = MedicineSerializer(medicine, data=request.data)
        if medicineSerializer.is_valid():
            medicineSerializer.save()
            return Response(medicineSerializer.validated_data)
        else:
            return Response(medicineSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        medicine = get_object_or_404(Medicine, pk=id)
        medicine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
