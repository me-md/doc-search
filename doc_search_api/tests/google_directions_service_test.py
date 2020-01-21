import json
import pytest
from expects import *
from doc_search_api.services.google_distance_service import GoogleDistanceService

def test_it_works():
    result = json.loads(GoogleDistanceService().distances(40.714224,-73.961452, [[39.720454,-104.898462],[39.73094,-104.93483]]))
    print(result)
    expect(result['destination_addresses'][0]).to(equal('130 Rampart Way, Denver, CO 80230, USA'))
    expect(result['destination_addresses'][1]).to(equal('880 Clermont St, Denver, CO 80220, USA'))
    expect(result['origin_addresses'][0]).to(equal('279 Bedford Ave, Brooklyn, NY 11211, USA'))
    expect(result['rows'][0]['elements'][0]['distance']['text']).to(equal('1,784 mi'))
    expect(result['rows'][0]['elements'][1]['distance']['text']).to(equal('1,780 mi'))
