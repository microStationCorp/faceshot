# Generated by Django 3.0.3 on 2020-03-15 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addphoto', '0003_auto_20200315_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedphoto',
            name='caption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
