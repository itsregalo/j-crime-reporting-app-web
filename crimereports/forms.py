from django import forms
from .models import CrimeReport, CrimeReportImage, CrimeReportVideo


class CrimeReportForm(forms.ModelForm):

    class Meta:
        model = CrimeReport
        fields = ['location', 'location_description', 'description']

    widgets = {
        'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
        'location_description': forms.Textarea(attrs={'class': 'materialize-textarea', 
                                                        'placeholder': 'Location Description',
                                                        'data-length': '120'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
    }

class CrimeReportImageForm(forms.ModelForm):
 
    class Meta:
        model = CrimeReportImage
        fields = ['image']

    widgets = {
        'image': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Images', 'multiple': True}),
    }

class CrimeReportVideoForm(forms.ModelForm):

    class Meta:
        model = CrimeReportVideo
        fields = ['video']

    widgets = {
        'video': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Videos', 'multiple': True}),
    }

