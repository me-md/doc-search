import json
import pytest
from expects import *
from doc_search_api.services.better_doctor_service import doc_service

def test_it_works():
    result = json.loads(doc_service.all_docs('co-denver'))

    expect(result['meta']['data_type'].to(equal('array')))
