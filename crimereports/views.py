from audioop import reverse
from django.shortcuts import render
from .forms import CrimeReportForm, CrimeReportImageForm, CrimeReportVideoForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def upload_crime_report(request):
    if request.method == 'POST':
        form = CrimeReportForm(request.POST, request.FILES)
        # get form images and videos in CrimeReportImageForm and CrimeReportVideoForm
        form_images = CrimeReportImageForm(request.POST, request.FILES)
        form_videos = CrimeReportVideoForm(request.POST, request.FILES)
        if form.is_valid() and form_images.is_valid() and form_videos.is_valid():
            crime_report = form.save()
            crime_report_images = form_images.save(commit=False)
            crime_report_images.crime_report = crime_report
            crime_report_images.save()
            crime_report_videos = form_videos.save(commit=False)
            crime_report_videos.crime_report = crime_report
            crime_report_videos.save()
            return HttpResponseRedirect(reverse('core:index'))

    else:
        form = CrimeReportForm()
    return render(request, 'crimereports/upload_crime_report.html', {'form': form})