from django.urls import path
from .views import *

app_name = 'crimereports'

urlpatterns = [
    path('upload_crime_report/', upload_crime_report, name='upload-crime'),
    path('upload_terrorism_report/', upload_terrorism_report, name='upload-terrorism'),
    path('upload_suspicious_activity_report/', upload_suspicious_activity_report, name='upload-suspicious_activity'),
    path('upload_lost_item_report/', upload_lost_item_report, name='upload-lost-items'),
    path('upload_theft_report/', upload_theft_report, name='upload-theft'),
    path('most_wanted/', most_wanted, name='most-wanted'),
    
]
