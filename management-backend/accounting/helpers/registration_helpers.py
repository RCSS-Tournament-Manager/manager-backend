from django.core.exceptions import ValidationError
from accounting.models import CustomUser
from allauth.account import app_settings as allauth_account_settings
from dj_rest_auth.utils import jwt_encode
from allauth.account.utils import complete_signup
from django.utils.translation import gettext_lazy as _

from ..models import (
    CustomUser, 
)


def perform_create(serializer):
    # first_name = serializer.validated_data.get("first_name")
    # last_name = serializer.validated_data.get("last_name")
    # email = serializer.validated_data.get("email", None)
    # phone_number = serializer.validated_data.get("phone_number", None)
    # code = serializer.validated_data.get("code", False)
    # password = serializer.validated_data.get("password")

    # if code:
    #     try:
    #         invite_key = RegisterCode.objects.get(code=code)
    #         if invite_key.is_used == True:
    #             raise ValidationError(_("This code has already been used."))
    #     except RegisterCode.DoesNotExist:
    #         raise ValidationError(_("Invalid or expired registration key."))

    # user = CustomUser.objects.create_user(
    #     first_name=first_name,
    #     last_name=last_name,
    #     email=email,
    #     username=email,
    #     phone_number=phone_number,
    #     password=password,
    #     code=code,
    # )
    
    # invite_key.use()
    # return user

