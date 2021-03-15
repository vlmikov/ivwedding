from django.contrib import admin

from . import models
# Register your models here.


admin.site.register(models.Guest)
admin.site.register(models.Invitation)
admin.site.register(models.Table)