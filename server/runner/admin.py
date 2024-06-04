from django.contrib import admin

from .models import Runner, RunnerServer

# Register your models here.
admin.site.register(Runner)
admin.site.register(RunnerServer)
