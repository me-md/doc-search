from doc_search_api.views import doctors
from doc_search_api.facades.doctors_facade import DoctorsFacade
from django.http import JsonResponse

def index(request):
    location = request.GET['location'] if 'location' in request.GET else None
    provider = request.GET['provider'] if 'provider' in request.GET else None
    lat = request.GET['lat'] if 'lat' in request.GET else None
    lon = request.GET['lon'] if 'lon' in request.GET else None
    coords = [lat, lon] if lat and lon else None
    if location and provider:
        data = DoctorsFacade().doctors(location)
        return doctors(data, provider, coords, location)
    elif location:
        data = DoctorsFacade().doctors(location)
        return doctors(data, None, coords, location)
    else:
        return JsonResponse({'error': 'Must Supply a location in query params.'})
