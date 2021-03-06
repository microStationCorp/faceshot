from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class extraUserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    last_voted_pic_id=models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
