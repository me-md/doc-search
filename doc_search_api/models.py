from django.db import models

class Provider(models.Model):
    UID = models.CharField(max_length = 120)
    Name = models.CharField(max_length = 120)
