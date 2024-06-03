from rest_framework import serializers
from .models import RegistrationRequest

class RegistrationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationRequest
        fields = [
            "email",
            "phone_number",
            "key",
            "message",
            "is_approved",
            "created_at",
        ]
        read_only_fields = ["is_approved", "created_at"]

    def validate(self, data):
        """
        Check that either an email or a phone number is provided, and that
        either a key or a message is provided, but not both.
        """
        if not data.get("email") and not data.get("phone_number"):
            raise serializers.ValidationError(
                "Either an email or a phone number must be provided."
            )

        # Check that either a key or a message is provided
        key = data.get("key")
        message = data.get("message")
        if not bool(key) and not bool(message):
            raise serializers.ValidationError(
                "Either a key or a message must be provided"
            )

        return data


class RegisterWithCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False, allow_blank=True)
    phone_number = serializers.CharField(max_length=17, required=False, allow_blank=True)
    password = serializers.CharField(max_length=128, required=True, allow_blank=False)
    first_name = serializers.CharField(max_length=30, required=True, allow_blank=False)
    last_name = serializers.CharField(max_length=30, required=True, allow_blank=False)
    code = serializers.CharField(max_length=64, required=True, allow_blank=False)

    def validate(self, data):
        """
        Check that either an email or a phone number is provided, and that
        either a key or a message is provided, but not both.
        """
        if not data.get("email") and not data.get("phone_number"):
            raise serializers.ValidationError(
                "Either an email or a phone number must be provided."
            )

        return data


class RegisterSendVerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PhoneVerificationSendCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=17)
    
class PhoneVerifyCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=64)
    
class EmailVerificationSendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

class EmailVerifyCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=64)