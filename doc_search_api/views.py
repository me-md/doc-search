from doc_search_api.serializer import DocSerializer

def doctors(data):
    return DocSerializer.doctors(data)
