# Generated by Django 3.0.3 on 2020-03-01 10:35

import addphoto.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addphoto', '0003_auto_20200301_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedphoto',
            name='image',
            field=models.ImageField(upload_to=addphoto.models.get_image_path),
        ),
    ]