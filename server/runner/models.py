from django.contrib.postgres.fields import ArrayField
from django.db import models

from server.enums import RunnerStatus, QueueStatus


# Create your models here.
class Runner(models.Model):
    name = models.CharField(max_length=128)
    message_bus_id = models.PositiveIntegerField()
    status = models.PositiveSmallIntegerField(
        choices=RunnerStatus.choices, default=RunnerStatus.NOT_RESPONDING.value
    )
    last_heart_beat = models.DateTimeField()
    queue_status = models.PositiveSmallIntegerField(choices=QueueStatus.choices)
    tags = ArrayField(
        models.CharField(max_length=64),
        blank=True,
        default=list,
    )

    def __str__(self):
        return self.name


class RunnerServer(models.Model):
    ip = models.IPAddressField()
    server_status = models.PositiveSmallIntegerField(choices=QueueStatus.choices)
    runner = models.ForeignKey(
        "runner.Runner", on_delete=models.PROTECT, related_name="servers"
    )

    def __str__(self):
        return self.ip
