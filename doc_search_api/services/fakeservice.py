import http.client

def fake_service():
    connection = http.client.HTTPConnection('www.google.com')
    connection.request('GET', '/')
    response = connection.getresponse()
    return("Status: {} and reason: {}".format(response.status, response.reason))
    connection.close()
