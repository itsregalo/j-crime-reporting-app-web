from django import forms
from .models import (CrimeReport, CrimeReportImage, CrimeReportVideo,
                    Terrorism, TerrorismReportImage, TerrorismReportVideo,
                    SuspiciousActivity, SuspiciousActivityReportImage, SuspiciousReportVideo,
                    LostItem, LostItemReportImage, LostItemVideo,
                    TheftReport, TheftReportImage, TheftReportVideo,
                    MostWanted, MostWantedImages)


class CrimeReportForm(forms.ModelForm):

    class Meta:
        model = CrimeReport
        fields = ['county', 'location_description', 'description']

    widgets = {
        'county': forms.Select(attrs={'class': 'form-control', 'placeholder': 'County'}),
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


class TerrorismReportForm(forms.ModelForm):

    class Meta:
        model = Terrorism
        fields = ['county', 'location_description', 'description']

    widgets = {
        'county': forms.Select(attrs={}),
        'location_description': forms.Textarea(attrs={'class': 'materialize-textarea', 
                                                        'placeholder': 'Location Description',
                                                        'data-length': '120'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'})
    }

class TerrorismReportImageForm(forms.ModelForm):
 
    class Meta:
        model = TerrorismReportImage
        fields = ['image']

    widgets = {
        'image': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Images', 'multiple': True}),
    }

class TerrorismReportVideoForm(forms.ModelForm):

    class Meta:
        model = TerrorismReportVideo
        fields = ['video']

    widgets = {
        'video': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Videos', 'multiple': True}),
    }



class SuspiciousActivityForm(forms.ModelForm):

    class Meta:
        model = SuspiciousActivity
        fields = ['county', 'location_description', 'description']

    widgets = {
        'county': forms.Select(attrs={'class': 'form-control', 'placeholder': 'County'}),
        'location_description': forms.Textarea(attrs={'class': 'materialize-textarea', 
                                                        'placeholder': 'Location Description',
                                                        'data-length': '120'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
    }

class SuspiciousActivityImageForm(forms.ModelForm):
 
    class Meta:
        model = SuspiciousActivityReportImage
        fields = ['image']

    widgets = {
        'image': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Images', 'multiple': True}),
    }

class SuspiciousActivityVideoForm(forms.ModelForm):

    class Meta:
        model = SuspiciousReportVideo
        fields = ['video']

    widgets = {
        'video': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Videos', 'multiple': True}),
    }



class LostItemForm(forms.ModelForm):

    class Meta:
        model = LostItem
        fields = ['county', 'location_description', 'description']

    widgets = {
        'county': forms.Select(attrs={'class': 'form-control', 'placeholder': 'County'}),
        'location_description': forms.Textarea(attrs={'class': 'materialize-textarea', 
                                                        'placeholder': 'Location Description',
                                                        'data-length': '120'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
    }

class LostItemImageForm(forms.ModelForm):
 
    class Meta:
        model = LostItemReportImage
        fields = ['image']

    widgets = {
        'image': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Images', 'multiple': True}),
    }

class LostItemVideoForm(forms.ModelForm):

    class Meta:
        model = LostItemVideo
        fields = ['video']

    widgets = {
        'video': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Videos', 'multiple': True}),
    }


class TheftForm(forms.ModelForm):

    class Meta:
        model = TheftReport
        fields = ['county', 'location_description', 'description']

    widgets = {
        'county': forms.Select(attrs={'class': 'form-control', 'placeholder': 'County'}),
        'location_description': forms.Textarea(attrs={'class': 'materialize-textarea', 
                                                        'placeholder': 'Location Description',
                                                        'data-length': '120'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
    }

class TheftImageForm(forms.ModelForm):
 
    class Meta:
        model = TheftReportImage
        fields = ['image']

    widgets = {
        'image': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Images', 'multiple': True}),
    }

class TheftVideoForm(forms.ModelForm):

    class Meta:
        model = TheftReportVideo
        fields = ['video']

    widgets = {
        'video': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Videos', 'multiple': True}),
    }


class MostWantedForm(forms.ModelForm):

    class Meta:
        model = MostWanted
        fields = ['county',  'description']

    widgets = {
        'county': forms.Select(attrs={'class': 'form-control', 'placeholder': 'County'}),
        'image': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Images', 'multiple': True}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
    }

class MostWantedImageForm(forms.ModelForm):
 
    class Meta:
        model = MostWantedImages
        fields = ['image']

    widgets = {
        'image': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Images', 'multiple': True}),
    }


