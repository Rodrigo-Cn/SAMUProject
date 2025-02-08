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
def getChartParameters(request):  # ✅ Certifique-se de que request está presente aqui
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
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # ✅ Retorna erro detalhado
