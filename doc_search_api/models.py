from django.db import models

class Provider(models.Model):
    uid = models.CharField(max_length = 120)
    name = models.CharField(max_length = 120)
    nick_name = models.CharField(max_length = 120)
