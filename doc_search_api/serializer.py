from rest_framework import serializers
from django.http import HttpResponse
import json
from doc_search_api.objects.doctor import Doctor
from doc_search_api.formatters.doctors_formatter import DoctorFormatter

class DocSerializer():
    def doctors(doc_data):
        docs = []
        format = json.loads(doc_data)
        for doc in format['data']:
            docs.append(Doctor(doc))
        return HttpResponse(DoctorFormatter().format(docs))
