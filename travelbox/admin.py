from django.contrib import admin

from travelbox import views, models

# Register your models here.
admin.site.register(models.Travel_box)
admin.site.register(models.GetPic)
admin.site.register(models.City)
# admin.site.register(models.Local)

