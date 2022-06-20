from audioop import reverse
from django.shortcuts import render
from .forms import CrimeReportForm, CrimeReportImageForm, CrimeReportVideoForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def upload_crime_report(request):
    if request.method == 'POST':
        form = CrimeReportForm(request.POST, request.FILES)
        # get form images and videos in CrimeReportImageForm and CrimeReportVideoForm
        form_images = CrimeReportImageForm(request.POST, request.FILES) or None
        form_videos = CrimeReportVideoForm(request.POST, request.FILES) or None
        if form.is_valid() and form_images.is_valid() and form_videos.is_valid():
            crime_report = form.save()
            crime_report_images = form_images.save(commit=False)
            crime_report_images.crime_report = crime_report
            crime_report_images.save()
            crime_report_videos = form_videos.save(commit=False)
            crime_report_videos.crime_report = crime_report
            crime_report_videos.save()
            messages.success(request, 'Crime Uploaded Successfully')
            return HttpResponseRedirect(reverse('core:index'))
        messages.error(request, 'Error Uploading Crime')
        return HttpResponseRedirect(reverse('core:index'))

