from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from patients.models import Patient
from medicines.models import Medicine
from patientcares.models import PatientCare
from doctors.models import Doctor
from django.utils import timezone
from datetime import timedelta

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"message": "Logout realizado com sucesso"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error": "Token não encontrado"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getChartParameters(request):
    try:
        numPatients = Patient.objects.count()
        numPatientCares = PatientCare.objects.count()
        numDoctors = Doctor.objects.count()
        numMedicines = Medicine.objects.count()

        return Response({
            'numPatients': numPatients,
            'numPatientCares': numPatientCares,
            'numDoctors': numDoctors,
            'numMedicines': numMedicines 
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getChartParametersTwo(request):
    try:
        today = timezone.localtime(timezone.now()).date()

        day_one = today
        day_two = today - timedelta(days=1)
        day_three = today - timedelta(days=2)
        day_four = today - timedelta(days=3)

        return Response({
            'dayOne': day_one.strftime('%d/%m/%Y'),
            'dayTwo': day_two.strftime('%d/%m/%Y'),
            'dayThree': day_three.strftime('%d/%m/%Y'),
            'dayFour': day_four.strftime('%d/%m/%Y'),
            'dayOneNum': PatientCare.objects.filter(date=day_one).count(),
            'dayTwoNum': PatientCare.objects.filter(date=day_two).count(),
            'dayThreeNum': PatientCare.objects.filter(date=day_three).count(),
            'dayFourNum': PatientCare.objects.filter(date=day_four).count(),
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTable(request):
    try:
        last_addresses = PatientCare.objects.order_by('-id')[:3].values('street', 'district', 'city')

        return Response({
            'lastAddresses': list(last_addresses)
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

