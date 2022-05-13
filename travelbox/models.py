from pyexpat import model
from django.db import models

# Create your models here.
class Travel_box(models.Model):
    travel_box_id = models.CharField(max_length=32)
    sub_title = models.TextField(max_length=1024, blank=True, null = True)
    script = models.TextField(max_length=1024, blank=True, null = True)
    place_name = models.TextField(max_length=16, blank= True, null = True)
    traffic = models.TextField(max_length=1024, blank=True, null = True)
    accomdation = models.TextField(max_length=8192, blank=True, null = True)
    addr_accomdation = models.TextField(max_length=2048, blank=True, null = True)
    food  = models.TextField(max_length=1024, blank=True, null = True)
    activity = models.TextField(max_length=1024, blank=True, null = True)
    sightseeing = models.TextField(max_length=8192, blank=True, null = True)
    # sightseeing_addr_link = models.TextField(max_length=2048, blank=True, null = True)
    
    image_head = models.ImageField(
        upload_to = 'landing/images/%Y/%m/%d/%H/',
        blank = True
    )
    image_1 = models.ImageField(
        upload_to = 'landing/images/%Y/%m/%d/%H/',
        blank = True
    )
    image_2 = models.ImageField(
        upload_to = 'landing/images/%Y/%m/%d/%H/',
        blank = True
    )
    image_3 = models.ImageField(
        upload_to = 'landing/images/%Y/%m/%d/%H/',
        blank = True
    )

    image_accomdation = models.ImageField(
        upload_to = 'landing/images/%Y/%m/%d/%H/',
        blank = True
    )

    image_food = models.ImageField(
        upload_to = 'landing/images/%Y/%m/%d/%H/',
        blank = True
    )

    image_activity = models.ImageField(
        upload_to = 'landing/images/%Y/%m/%d/%H/',
        blank = True
    )

    image_sightseeing = models.ImageField(
        upload_to = 'landing/images/%Y/%m/%d/%H/',
        blank = True
    )

    





class GetPic(models.Model):
     travel_box_id = models.CharField(max_length=32)
     travel_box = models.ForeignKey(Travel_box, name="box_id", on_delete=models.CASCADE, null=True, blank=True)
     user_image_1 = models.ImageField(
        upload_to = 'landing/images/%Y/%m/%d/%H/',
        blank = True
    )
     user_image_2 = models.ImageField(
        upload_to = 'landing/images/%Y/%m/%d/%H/',
        blank = True
    )
     user_image_3 = models.ImageField(
        upload_to = 'landing/images/%Y/%m/%d/%H/',
        blank = True
    )

    #  check_num = models.IntegerField() #체크박스해당 숫자


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actual city name on the dashboard
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'

# class Local(models.Model):

#     local_name = models.ForeignKey(Travel_box, name="local_name", on_delete=models.CASCADE, null=True, blank=True)

#     image_accomdation = models.ImageField(
#         upload_to = 'landing/images/%Y/%m/%d/%H/',
#         blank = True
#     )

#     image_food = models.ImageField(
#         upload_to = 'landing/images/%Y/%m/%d/%H/',
#         blank = True
#     )

#     image_activity = models.ImageField(
#         upload_to = 'landing/images/%Y/%m/%d/%H/',
#         blank = True
#     )

#     image_sightseeing = models.ImageField(
#         upload_to = 'landing/images/%Y/%m/%d/%H/',
#         blank = True
#     )