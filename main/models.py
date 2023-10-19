from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Content(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    in_the_basket = models.BooleanField(default=False)
    user = models.ForeignKey(User, verbose_name='Пользователь',  on_delete=models.CASCADE)

class Tasks(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
