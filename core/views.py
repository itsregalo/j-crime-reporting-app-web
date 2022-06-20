from django.shortcuts import render
from crimereports.models import CrimeReport, CrimeReportImage, CrimeReportVideo
from crimereports.forms import CrimeReportForm, CrimeReportImageForm, CrimeReportVideoForm


def index(request, *args, **kwargs):
    crime_form = CrimeReportForm()
    crime_image_form = CrimeReportImageForm()
    crime_video_form = CrimeReportVideoForm()

    context = {
        'crime_form': crime_form,
        'crime_image_form': crime_image_form,
        'crime_video_form': crime_video_form,
    }
    return render(request, 'index.html', context)

