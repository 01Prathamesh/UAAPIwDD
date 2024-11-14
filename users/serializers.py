from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

# Custom validator for Indian phone number
phone_number_validator = RegexValidator(
    regex=r'^\+91[6-9][0-9]{9}$|^[6-9][0-9]{9}$',
    message="Enter a valid Indian phone number"
)

class RegisterSerializer(serializers.ModelSerializer):
    # Adding the phone number validator
    phone_number = serializers.CharField(
        max_length=15,  # Maximum length for phone numbers with country code
        required=True,
        validators=[phone_number_validator]
    )
    
    class Meta:
        model = User
        fields = ['username', 'password', 'phone_number', 'date_of_birth']

    def create(self, validated_data):
        # Hashing the password during user creation
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'phone_number', 'date_of_birth', 'last_login_ip']
