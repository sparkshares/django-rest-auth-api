from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from account.services.postServices import create_post_service, list_user_posts_service
from account.services.userServices import user_change_password_service, user_login_service, user_profile_service, user_registration_service


@api_view(['POST'])
def user_registration(request):
    data, status_code = user_registration_service(request.data)
    return Response(data, status=status_code)

@api_view(['POST'])
def user_login(request):
    data, status_code = user_login_service(request.data)
    return Response(data, status=status_code)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    data, status_code = user_profile_service(request.user)
    return Response(data, status=status_code)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_change_password(request):
    data, status_code = user_change_password_service(request.user, request.data)
    return Response(data, status=status_code)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    data, is_valid = create_post_service(request.user, request.data.copy())
    if is_valid:
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_posts(request):
    data = list_user_posts_service(request.user)
    return Response(data, status=status.HTTP_200_OK)