from django.contrib import admin
from django.urls import path, include
from doc_search_api.controllers.doctors_controller import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/doctors/', index, name='doctors-all'),
    path('api/v1/', include('doc_search_api.urls'))
]
