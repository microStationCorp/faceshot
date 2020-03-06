# Generated by Django 3.0.3 on 2020-03-06 14:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addphoto', '0004_uploadedphoto_fire_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedphoto',
            name='poop_count',
            field=models.ManyToManyField(blank=True, related_name='poop_count', to=settings.AUTH_USER_MODEL),
        ),
    ]
