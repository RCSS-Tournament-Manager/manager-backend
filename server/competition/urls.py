from django.urls import path

from competition.views import TeamViewSet, GroupViewSet, ServerConfigViewSet

urlpatterns = [
    path("teams/v0/", TeamViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "teams/<pk>/v0/",
        TeamViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
    path("groups/v0/", GroupViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "groups/<pk>/v0/",
        GroupViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
    path("configs/v0/", ServerConfigViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "configs/<pk>/v0/",
        ServerConfigViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
]
