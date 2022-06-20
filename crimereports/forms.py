from django import forms
from .models import CrimeReport, CrimeReportImage, CrimeReportVideo


class CrimeReportForm(forms.ModelForm):

    class Meta:
        model = CrimeReport
        fields = ['location', 'location_description', 'description']

    widgets = {
        'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
        'location_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Location Description'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
    }

class CrimeReportImageForm(forms.ModelForm):
 
    class Meta:
        model = CrimeReportImage
        fields = ['image']

    widgets = {
        'image': forms.FileInput(attrs={'class': 'form-control-file'}),
    }

class CrimeReportVideoForm(forms.ModelForm):

    class Meta:
        model = CrimeReportVideo
        fields = ['video']

    widgets = {
        'video': forms.FileInput(attrs={'class': 'form-control-file'}),
    }
