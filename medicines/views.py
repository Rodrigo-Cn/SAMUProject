from rest_framework.pagination import PageNumberPagination
from .models import Medicine
from .serializer import MedicineSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MedicinePagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'

class MedicineAPIView(APIView):
    def get(self, request):
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
        
class MedicineAPIViewDetail(APIView):
    def get(self, request, id):
        medicine = get_object_or_404(Medicine ,pk=id)
        medicineSerializer = MedicineSerializer(medicine)
        return Response(medicineSerializer.data)
    
    def put(self, request, id):
        medicine = get_object_or_404(Medicine, pk=id)
        medicineSerializer = MedicineSerializer(medicine, data=request.data)
        if medicineSerializer.is_valid():
            medicineSerializer.save()
            return Response(medicineSerializer.data)
        else:
            return Response(medicineSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        medicine = get_object_or_404(Medicine, pk=id)
        medicine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
