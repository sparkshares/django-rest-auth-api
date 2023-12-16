from django.contrib.auth import authenticate
from account.serializers import UserChangePasswordSerializer, UserLoginSerializer, UserProfileSerializer, UserRegistrationSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def user_registration_service(data):
    serializer = UserRegistrationSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        token = get_tokens_for_user(user)
        return {'token':token,'msg':'User Registration success'}, status.HTTP_201_CREATED
    return serializer.errors, status.HTTP_400_BAD_REQUEST

def user_login_service(data):
    serializer = UserLoginSerializer(data=data)
    if serializer.is_valid():
        email= serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email,password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return {'token':token,'msg':'Login Successful'}, status.HTTP_201_CREATED
        return {'msg':'Login Failed'}, status.HTTP_400_BAD_REQUEST
    return serializer.errors, status.HTTP_400_BAD_REQUEST

def user_profile_service(user):
    serializer = UserProfileSerializer(user)
    return serializer.data, status.HTTP_200_OK

def user_change_password_service(user, data):
    serializer = UserChangePasswordSerializer(data=data, context={'user': user})
    if serializer.is_valid():
        return {'msg':'Password Changed Successfully'}, status.HTTP_200_OK
    return serializer.errors, status.HTTP_400_BAD_REQUEST