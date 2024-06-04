from django.contrib import admin
from .models import Team, Group, ServerConfig, Match, BinaryUpload

# Register your models here.
admin.site.register(Team)
admin.site.register(Group)
admin.site.register(ServerConfig)
admin.site.register(Match)
admin.site.register(BinaryUpload)
