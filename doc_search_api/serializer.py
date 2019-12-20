from rest_framework import serializers
import json
from doc_search_api.objects import Doctor

class DocSerializer():
    def doctors(doc_data):
        docs = []
        for doc in doc_data['data']:
            docs.append(Doctor(doc))
        return json.dumps(docs)
