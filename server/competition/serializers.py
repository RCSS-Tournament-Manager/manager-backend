from rest_framework import serializers
from competition.models import Team, Group, ServerConfig


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name", "affiliation"]


class GroupSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        exclude = ["created_at", "updated_at"]


class ServerConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerConfig
        exclude = ["created_at", "updated_at"]
