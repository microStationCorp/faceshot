# Generated by Django 3.0.3 on 2020-03-01 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addphoto', '0002_auto_20200301_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedphoto',
            name='image',
            field=models.ImageField(upload_to='get_image_path'),
        ),
    ]
