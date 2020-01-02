import json
import pytest
from expects import *
from doc_search_api.services.better_doctor_service import DocService

def test_it_works():
    result = json.loads(DocService().all_docs('co-denver'))

    expect(result['meta']['data_type']).to(equal('array'))
    expect(result['data'][0]['practices'][0]['uid']).to(equal('ca3466def4a60da36654c49bf01ef94b'))
    expect(len(result['data'][0]['practices'][0]['insurance_uids'])).to(equal(9))
