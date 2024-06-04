from django.contrib.auth.models import AbstractUser
from django.db import models
from django_minio_backend import MinioBackend, iso_date_prefix

from server.enums import Roles


# Create your models here.
class User(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=Roles.choices)
    team = models.ForeignKey(
        "competition.Team", on_delete=models.PROTECT, related_name="members"
    )
    avatar = models.FileField(
        verbose_name="avatar-upload",
        upload_to=iso_date_prefix,
        storage=MinioBackend(bucket_name="user-avatar-private"),
    )
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.username
