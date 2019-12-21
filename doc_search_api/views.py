# from django.shortcuts import render
# from django.core import serializers
from .serializer import DocSerializer
# import json
# from http.client import HTTPResponse
from doc_search_api.services.better_doctor_service import DocService

def doctor_data(self, **kwargs):
    service = DocService()
    data = service.all_docs(self.GET['location'])
    response = DocSerializer.doctors(data)
    return response
