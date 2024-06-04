from django.db import models
from django_minio_backend import MinioBackend, iso_date_prefix

from server.enums import GroupTypes, GroupStatus, TeamStatus, MatchStatus, ResultStatus


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=32)
    affiliation = models.CharField(max_length=64)
    # logo = models.FileField(verbose_name="logo-upload",
    #                         upload_to=iso_date_prefix,
    #                         storage=MinioBackend(bucket_name="team-logo-private"))
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=32)
    type = models.PositiveSmallIntegerField(choices=GroupTypes.choices)
    teams = models.ManyToManyField(
        "competition.Team", related_name="groups", through="competition.GroupTeam"
    )
    server_config = models.ForeignKey(
        "competition.ServerConfig", on_delete=models.PROTECT, related_name="groups"
    )
    status = models.PositiveSmallIntegerField(choices=GroupStatus.choices)
    capacity = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ServerConfig(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    value = models.JSONField(verbose_name="config")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class GroupTeam(models.Model):
    group = models.ForeignKey("competition.Group", on_delete=models.PROTECT)
    team = models.ForeignKey("competition.Team", on_delete=models.PROTECT)
    status = models.PositiveSmallIntegerField(
        choices=TeamStatus.choices, default=TeamStatus.ACTIVE.value
    )


class Match(models.Model):
    left_team = models.ForeignKey(
        "competition.Team", on_delete=models.PROTECT, related_name="home_matches"
    )
    right_team = models.ForeignKey(
        "competition.Team", on_delete=models.PROTECT, related_name="away_matches"
    )
    server_config = models.ForeignKey(
        "competition.ServerConfig", on_delete=models.PROTECT, related_name="matches"
    )
    runner = models.ForeignKey(
        "runner.Runner", on_delete=models.PROTECT, related_name="matches"
    )
    group = models.ForeignKey(
        "competition.Group", on_delete=models.PROTECT, related_name="matches"
    )
    left_team_score = models.PositiveSmallIntegerField(default=0)
    right_team_score = models.PositiveSmallIntegerField(default=0)
    left_team_penalty_score = models.PositiveSmallIntegerField(default=0)
    right_team_penalty_score = models.PositiveSmallIntegerField(default=0)
    status = models.PositiveSmallIntegerField(
        choices=MatchStatus.choices, default=MatchStatus.NO_STATUS.value
    )
    priority = models.PositiveSmallIntegerField(default=0)
    scheduled_start_time = models.DateTimeField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    # game_log =
    # teams_log =
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.left_team.name} vs {self.right_team.name}"


class BinaryUpload(models.Model):
    team = models.ForeignKey(
        "competition.Team", on_delete=models.PROTECT, related_name="binaries"
    )
    result_status = models.PositiveSmallIntegerField(
        choices=ResultStatus.choices, default=ResultStatus.UPLOADED.value
    )
    error_message = models.TextField(blank=True, null=True)
    # binary_file =
    finished_docker_image_hash = models.TextField(blank=True, null=True)
    # finished_docker_image_file =
    uploaded_by = models.ForeignKey(
        "user.User", on_delete=models.PROTECT, related_name="uploads"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.team.name} - {self.id}"
