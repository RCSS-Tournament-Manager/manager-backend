from django.db import models

from server.enums import ContentType, Visibility


# Create your models here.
class Event(models.Model):
    owner = models.ForeignKey('user.User', on_delete=models.DO_NOTHING, related_name='events')
    operation = models.TextField(blank=True, null=True)
    operation_data = models.JSONField()
    occurrence_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class News(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    brief = models.TextField(blank=True, null=True)
    content_type = models.CharField(
        max_length=64,
        choices=ContentType.choices,
        default=ContentType.TEXT.value
    )
    visibility = models.PositiveSmallIntegerField(choices=Visibility.choices, default=Visibility.PUBLIC.value)
    pinned = models.BooleanField(default=False)
    link = models.URLField(blank=True, null=True)
    author = models.ForeignKey('user.User', on_delete=models.DO_NOTHING, related_name='published_news')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
