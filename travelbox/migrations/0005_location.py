# Generated by Django 4.0.4 on 2022-05-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelbox', '0004_delete_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_name', models.CharField(max_length=8)),
            ],
        ),
    ]
