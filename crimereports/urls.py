from django.urls import path
from .views import *

app_name = 'crimereports'

urlpatterns = [
    path('upload_crime_report/', upload_crime_report, name='upload-crime'),
]
