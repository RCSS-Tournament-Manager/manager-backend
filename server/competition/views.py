from rest_framework import viewsets, status
from rest_framework.response import Response
from competition.models import Team, Group, ServerConfig
from competition.serializers import (
    TeamSerializer,
    GroupSerializer,
    ServerConfigSerializer,
)


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.filter(is_deleted=False)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        return super().update(request, partial=True, *args, **kwargs)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def create(self, request, *args, **kwargs):
        teams = request.data.pop("teams", [])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        if len(teams) > instance.capacity:
            return Response(
                {"detail": "The number of teams exceeds the group's capacity."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        instance.teams.add(*teams)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        teams = request.data.pop("teams", [])
        instance = self.get_object()
        capacity = request.data.get("capacity", instance.capacity)
        if len(teams) > capacity:
            return Response(
                {"detail": "The number of teams exceeds the group's capacity."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if len(teams) > 0:
            instance.teams.add(*teams)
        return super().update(request, partial=True, *args, **kwargs)


class ServerConfigViewSet(viewsets.ModelViewSet):
    queryset = ServerConfig.objects.all()
    serializer_class = ServerConfigSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, partial=True, *args, **kwargs)
