# Generated by Django 4.1.4 on 2024-06-04 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("runner", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                (
                    "type",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "Pool"), (1, "Stepladder")]
                    ),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "No Status"),
                            (1, "Running"),
                            (2, "Ended"),
                            (3, "Stopped"),
                        ]
                    ),
                ),
                ("capacity", models.PositiveSmallIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ServerConfig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                ("description", models.TextField(blank=True, null=True)),
                ("value", models.JSONField(verbose_name="config")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                ("affiliation", models.CharField(max_length=64)),
                ("is_deleted", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("left_team_score", models.PositiveSmallIntegerField(default=0)),
                ("right_team_score", models.PositiveSmallIntegerField(default=0)),
                (
                    "left_team_penalty_score",
                    models.PositiveSmallIntegerField(default=0),
                ),
                (
                    "right_team_penalty_score",
                    models.PositiveSmallIntegerField(default=0),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "No Status"),
                            (1, "Error"),
                            (2, "In Queue"),
                            (3, "Running"),
                            (4, "Ended"),
                            (5, "Stopped"),
                        ],
                        default=0,
                    ),
                ),
                ("priority", models.PositiveSmallIntegerField(default=0)),
                ("scheduled_start_time", models.DateTimeField()),
                ("start_time", models.DateTimeField(blank=True, null=True)),
                ("end_time", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="matches",
                        to="competition.group",
                    ),
                ),
                (
                    "left_team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="home_matches",
                        to="competition.team",
                    ),
                ),
                (
                    "right_team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="away_matches",
                        to="competition.team",
                    ),
                ),
                (
                    "runner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="matches",
                        to="runner.runner",
                    ),
                ),
                (
                    "server_config",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="matches",
                        to="competition.serverconfig",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GroupTeam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Active"),
                            (1, "Waiting"),
                            (2, "Eliminated"),
                            (3, "Champion"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="competition.group",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="competition.team",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="group",
            name="server_config",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="groups",
                to="competition.serverconfig",
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="teams",
            field=models.ManyToManyField(
                related_name="groups",
                through="competition.GroupTeam",
                to="competition.team",
            ),
        ),
        migrations.CreateModel(
            name="BinaryUpload",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "result_status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Uploaded"),
                            (1, "Not Checked"),
                            (2, "Passed"),
                            (3, "Failed"),
                        ],
                        default=0,
                    ),
                ),
                ("error_message", models.TextField(blank=True, null=True)),
                ("finished_docker_image_hash", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="binaries",
                        to="competition.team",
                    ),
                ),
            ],
        ),
    ]
