from django.shortcuts import render
from crimereports.models import CrimeReport, CrimeReportImage, CrimeReportVideo
from crimereports.forms import CrimeReportForm, CrimeReportImageForm, CrimeReportVideoForm


def index(request, *args, **kwargs):
    crime_forms = CrimeReportForm()
    crime_image_forms = CrimeReportImageForm()
    crime_video_forms = CrimeReportVideoForm()

    context = {
        'crime_forms': crime_forms,
        'crime_image_forms': crime_image_forms,
        'crime_video_forms': crime_video_forms,
    }
    return render(request, 'index.html', context)

