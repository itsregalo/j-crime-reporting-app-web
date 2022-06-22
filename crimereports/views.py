from django.shortcuts import redirect, render
from .forms import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import MostWanted

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
            return redirect('core:index')
        messages.error(request, 'Error Uploading Crime')
        return redirect('core:index')

def upload_terrorism_report(request):
    terrorism_form = TerrorismReportForm()
    terrorism_image_form = TerrorismReportImageForm()
    terrorism_video_form = TerrorismReportVideoForm()
    if request.method == 'POST':
        form = TerrorismReportForm(request.POST, request.FILES)
        # get form images and videos in CrimeReportImageForm and CrimeReportVideoForm
        form_images = TerrorismReportImageForm(request.POST, request.FILES) or None
        form_videos = TerrorismReportVideoForm(request.POST, request.FILES) or None
        if form.is_valid() and form_images.is_valid() and form_videos.is_valid():
            crime_report = form.save()
            crime_report_images = form_images.save(commit=False)
            crime_report_images.crime_report = crime_report
            crime_report_images.save()
            crime_report_videos = form_videos.save(commit=False)
            crime_report_videos.crime_report = crime_report
            crime_report_videos.save()
            messages.success(request, 'Crime Uploaded Successfully')
            return redirect('core:index')
        messages.error(request, 'Error Uploading Crime')
        return redirect('core:index')
    context = {
        'terrorism_form': terrorism_form,
        'terrorism_image_form': terrorism_image_form,
        'terrorism_video_form': terrorism_video_form,
    }
    return render(request, 'crimereports/upload_terrorism.html', context)

def upload_suspicious_activity_report(request):

    if request.method == 'POST':
        form = SuspiciousActivityForm(request.POST, request.FILES)
        # get form images and videos in CrimeReportImageForm and CrimeReportVideoForm
        form_images = SuspiciousActivityImageForm(request.POST, request.FILES) or None
        form_videos = SuspiciousActivityVideoForm(request.POST, request.FILES) or None
        if form.is_valid() and form_images.is_valid() and form_videos.is_valid():
            crime_report = form.save()
            crime_report_images = form_images.save(commit=False)
            crime_report_images.crime_report = crime_report
            crime_report_images.save()
            crime_report_videos = form_videos.save(commit=False)
            crime_report_videos.crime_report = crime_report
            crime_report_videos.save()
            messages.success(request, 'Crime Uploaded Successfully')
            return redirect('core:index')
        messages.error(request, 'Error Uploading Crime')
        return redirect('core:index')
    context = {
        'suspicious_activity_form': SuspiciousActivityForm(),
        'suspicious_activity_image_form': SuspiciousActivityImageForm(),
        'suspicious_activity_video_form': SuspiciousActivityVideoForm(),
    }
    return render(request, 'crimereports/upload_suspicious_activity.html', context)


def upload_lost_item_report(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
        # get form images and videos in CrimeReportImageForm and CrimeReportVideoForm
        form_images = LostItemImageForm(request.POST, request.FILES) or None
        form_videos = LostItemVideoForm(request.POST, request.FILES) or None
        if form.is_valid() and form_images.is_valid() and form_videos.is_valid():
            crime_report = form.save()
            crime_report_images = form_images.save(commit=False)
            crime_report_images.crime_report = crime_report
            crime_report_images.save()
            crime_report_videos = form_videos.save(commit=False)
            crime_report_videos.crime_report = crime_report
            crime_report_videos.save()
            messages.success(request, 'Crime Uploaded Successfully')
            return redirect('core:index')
        messages.error(request, 'Error Uploading Crime')
        return redirect('core:index')
    context = {
        'lost_item_form': LostItemForm(),
        'lost_item_image_form': LostItemImageForm(),
        'lost_item_video_form': LostItemVideoForm(),
    }
    return render(request, 'crimereports/upload_lost_item.html', context)



def upload_theft_report(request):
    if request.method == 'POST':
        form = TheftForm(request.POST, request.FILES)
        # get form images and videos in CrimeReportImageForm and CrimeReportVideoForm
        form_images = TheftImageForm(request.POST, request.FILES) or None
        form_videos = TheftVideoForm(request.POST, request.FILES) or None
        if form.is_valid() and form_images.is_valid() and form_videos.is_valid():
            crime_report = form.save()
            crime_report_images = form_images.save(commit=False)
            crime_report_images.crime_report = crime_report
            crime_report_images.save()
            crime_report_videos = form_videos.save(commit=False)
            crime_report_videos.crime_report = crime_report
            crime_report_videos.save()
            messages.success(request, 'Crime Uploaded Successfully')
            return redirect('core:index')
        messages.error(request, 'Error Uploading Crime')
        return redirect('core:index')
    context = {
        'theft_form': TheftForm(),
        'theft_image_form': TheftImageForm(),
        'theft_video_form': TheftVideoForm(),
    }
    return render(request, 'crimereports/upload_theft.html', context)


def most_wanted(request):
    most_wanted_criminals = MostWanted.objects.filter(is_captured=False)
    context = {
        'most_wanted_criminals': most_wanted_criminals
    }
    return render(request, 'core/most_wanted.html', context)
