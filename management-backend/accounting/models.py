from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


# class CustomUser(AbstractUser):
#     is_approved = models.BooleanField(default=False)
#     code = models.CharField(max_length=64, blank=True, null=True)

#     email_verified = models.BooleanField(default=False)

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

