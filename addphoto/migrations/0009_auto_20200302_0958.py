# Generated by Django 3.0.3 on 2020-03-02 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addphoto', '0008_auto_20200301_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedphoto',
            name='fire_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='uploadedphoto',
            name='haha_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='uploadedphoto',
            name='poop_count',
            field=models.IntegerField(default=0),
        ),
    ]
