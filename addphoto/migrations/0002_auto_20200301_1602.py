# Generated by Django 3.0.3 on 2020-03-01 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addphoto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedphoto',
            name='image',
            field=models.ImageField(max_length=1, upload_to='get_image_path'),
        ),
    ]
