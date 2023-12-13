from rest_framework import serializers
from account.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = User
        fields = ["email", "password","password2", "name","tc"]
        extra_kwargs = {"password": {"write_only": True}}
        
        
    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.pop("password2")
        if password != password2:
            raise serializers.ValidationError("Password must match")
        return attrs
    
    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    class Meta:
        model = User
        fields = ["email", "password"]
      

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email", "name"]

class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={"input_type": "password"}, write_only=True)
    password2=serializers.CharField(max_length=255, style={"input_type": "password"}, write_only=True)
    
    class Meta:
        fields = ["password","password2"]
        
    def validate(self,attrs):
        password = attrs.get("password")
        password2 = attrs.pop("password2")
        user = self.context.get("user")
        if password != password2:
            raise serializers.ValidationError("Password and confirm password must match")
        
        user.set_password(password)
        user.save()
        return attrs