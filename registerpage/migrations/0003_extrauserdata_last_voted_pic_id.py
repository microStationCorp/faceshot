# Generated by Django 3.0.3 on 2020-03-02 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerpage', '0002_auto_20200229_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrauserdata',
            name='last_voted_pic_id',
            field=models.IntegerField(default=0),
        ),
    ]