from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user

    return Response({
        'id': user.id,
        'name': user.get_full_name() or user.username,
        'email': user.email,
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_permission(request):
    user = request.user
    group = user.groups.first()

    return Response({
        'group': group.name if group else None,
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_not_permission(request):
    return Response(
        {'message': 'Sem permissão de administrador'},
        status=status.HTTP_401_UNAUTHORIZED
    )