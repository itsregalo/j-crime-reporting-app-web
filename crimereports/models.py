from django.db import models
from django.utils.text import slugify
import uuid

# Create your models here.


class CrimeReport(models.Model):
    """
    CrimeReport model
    """
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, blank=True, null=True)
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    location_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.location+' - '+str(self.timestamp)


class CrimeReportImage(models.Model):
    """
    CrimeReportImage model
    """
    crime_report = models.ForeignKey(CrimeReport, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.crime_report.location + ' ' + str(self.timestamp)

class CrimeReportVideo(models.Model):
    """
    CrimeReportVideo model
    """
    crime_report = models.ForeignKey(CrimeReport, on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.video.name + ' - ' + str(self.timestamp)
