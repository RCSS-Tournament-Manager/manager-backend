from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.urls import path


urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    
    
    re_path(
        r"^account-confirm-email/(?P<key>[-:\w]+)/$",
        TemplateView.as_view(),
        name="account_confirm_email",
    ),
    
]
