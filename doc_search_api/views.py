from doc_search_api.serializers import DocSerializer

def doctors(data, provider):
    return DocSerializer.doctors(data, provider)
