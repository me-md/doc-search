from django.db import models

class LocationCondition(models.Model):
    location = models.CharField(max_length=500)
    condition = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
