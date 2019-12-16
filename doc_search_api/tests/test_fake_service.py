import pytest
from expects import *
from doc_search_api.services.fakeservice import fake_service as service

def test_it_works():
    result = service()
    expect(result).to(equal('Status: 200 and reason: OK'))
