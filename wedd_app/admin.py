from django.contrib import admin

from . import models
# Register your models here.


admin.site.register(models.MainGuest)
admin.site.register(models.SecondGuest)
admin.site.register(models.Invitation)
admin.site.register(models.Table)