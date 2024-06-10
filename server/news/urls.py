from django.urls import path

from news.views import NewsViewSet

urlpatterns = [
    path("v0/", NewsViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "<pk>/v0/",
        NewsViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
]
