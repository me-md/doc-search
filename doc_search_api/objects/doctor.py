from django.db import models
from doc_search_api.formatters.doctor_formatter import DoctorFormatter

class Doctor(models.Model):

    def __init__(self, data, coords):
        self.name = 'Doctor Data'
        self.formatter = DoctorFormatter(data, coords)
        self.practice = self.formatter.practice()
        self.profile = self.formatter.profile()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
