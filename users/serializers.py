from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator
from rest_framework_simplejwt.tokens import RefreshToken

# Get the CustomUser model (which is used in place of the default User model)
User = get_user_model()

# Custom validator for Indian phone numbers
phone_number_validator = RegexValidator(
    regex=r'^\+91[6-9][0-9]{9}$|^[6-9][0-9]{9}$',
    message="Enter a valid Indian phone number"
)
class RegisterSerializer(serializers.ModelSerializer):
    # Adding the phone number validator and ensuring it's unique
    phone_number = serializers.CharField(
        max_length=15,  # Maximum length for phone numbers with country code
        required=True,
        validators=[phone_number_validator, UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'phone_number', 'date_of_birth']

    def create(self, validated_data):
        # Creating the user with a hashed password
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'phone_number', 'date_of_birth', 'last_login_ip']
