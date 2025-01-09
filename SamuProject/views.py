from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"message": "Logout realizado com sucesso"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error": "Token não encontrado"}, status=status.HTTP_400_BAD_REQUEST)
