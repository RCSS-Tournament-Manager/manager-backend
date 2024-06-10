from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    team = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "role", "team")
