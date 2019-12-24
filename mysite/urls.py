from django.contrib import admin
from django.urls import path, include, re_path
from doc_search_api.controllers.doctors_controller import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/doctors/', index),
    re_path('api/(?P<version>(v1|v2))/', include('doc_search_api.urls'))
]
