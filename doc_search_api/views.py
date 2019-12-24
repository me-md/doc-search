from doc_search_api.serializer import DocSerializer

def doctors(data, provider):
    return DocSerializer.doctors(data, provider)
