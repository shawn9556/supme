from django.db import models

# Create your models here.
class Travel_box(models.Model):
    travel_box_id = models.CharField(max_length=32)
    place_name = models.TextField(max_length=16, blank= True, null = True)
    traffic = models.TextField(max_length=64, blank=True, null = True)
    accomdation = models.TextField(max_length=64, blank=True, null = True)
    food  = models.TextField(max_length=64, blank=True, null = True)
    activity = models.TextField(max_length=64, blank=True, null = True)
    sightseeing = models.TextField(max_length=64, blank=True, null = True)
    image = models.ImageField(
        upload_to = 'landing/images/%Y/%m/%d/%H/',
        blank = True
    )

