from tabnanny import verbose
from django.db import models
from django.utils.text import slugify
import uuid
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from accounts.models import User
# Create your models here.

class County(models.Model):
    name = models.CharField(max_length=100)
    county_no = models.PositiveSmallIntegerField(unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name_plural = 'Counties'
        ordering = ['county_no']
        db_table = 'counties'


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class CrimeReport(models.Model):
    """
    CrimeReport model
    """
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, blank=True, null=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    location_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name_plural = 'Crime Reports'
        ordering = ['-timestamp']
        db_table = 'crime_reports'

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

    class Meta:
        verbose_name_plural = 'Crime Report Images'
        ordering = ['-timestamp']
        db_table = 'crime_report_images'

    def __str__(self):
        return str(self.timestamp)

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

    class Meta:
        verbose_name_plural = 'Crime Report Videos'
        ordering = ['-timestamp']
        db_table = 'crime_report_videos'

class Terrorism(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, blank=True, null=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True)
    location_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name_plural = 'Terrorism'
        ordering = ['-timestamp']
        db_table = 'terrorism'

    def __str__(self):
        return self.location_description+'-'+str(self.timestamp)

class TerrorismReportImage(models.Model):
    """
    TerrorismReportImage model
    """
    crime_report = models.ForeignKey(Terrorism, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name_plural = 'Terrorism Report images'
        ordering = ['-timestamp']
        db_table = 'terrorism_report_images'


    def __str__(self):
        return str(self.timestamp)

class TerrorismReportVideo(models.Model):
    """
    TerrorismReportVideo model
    """
    crime_report = models.ForeignKey(Terrorism, on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name_plural='Terrorism Report Videos'
        db_table = 'terrorism_report_videos'
        


    def __str__(self):
        return self.video.name + ' - ' + str(self.timestamp)



class SuspiciousActivity(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, blank=True, null=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True)
    location_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name_plural = 'Suspicious Activities'
        db_table = 'suspicious_activities'

    def __str__(self):
        return self.location_description+'-'+str(self.timestamp)

class SuspiciousActivityReportImage(models.Model):
    """
    SuspiciousActivityReportImage model
    """
    crime_report = models.ForeignKey(SuspiciousActivity, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name_plural = 'Suspicious Activities Images'
        ordering = ['-timestamp']
        db_table = 'suspicious_activities_images'

    def __str__(self):
        return str(self.timestamp)

class SuspiciousReportVideo(models.Model):
    """
    SuspiciousReportVideo model
    """
    crime_report = models.ForeignKey(SuspiciousActivity, on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name_plural = 'Suspicious Activities Videos'
        ordering = ['-timestamp']
        db_table = 'suspicious_activities_videos'

    def __str__(self):
        return self.video.name + ' - ' + str(self.timestamp)




class LostItem(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, blank=True, null=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True)
    location_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name_plural = 'Lost Items'
        ordering = ['-timestamp']
        db_table = 'lost_items'

    def __str__(self):
        return self.location_description+'-'+str(self.timestamp)

class LostItemReportImage(models.Model):
    """
    LostItemReportImage model
    """
    crime_report = models.ForeignKey(LostItem, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name_plural = 'Lost Items Images'
        ordering = ['-timestamp']
        db_table = 'lost_items_images'

    def __str__(self):
        return str(self.timestamp)

class LostItemVideo(models.Model):
    """
    LostItemVideo model
    """
    crime_report = models.ForeignKey(LostItem, on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name_plural = 'Lost Items Videos'
        ordering = ['-timestamp']
        db_table = 'lost_items_videos'

    def __str__(self):
        return self.video.name + ' - ' + str(self.timestamp)




class TheftReport(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, blank=True, null=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True)
    location_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name_plural = 'Theft Reports'
        ordering = ['-timestamp']
        db_table = 'theft_reports'

    def __str__(self):
        return self.location_description+'-'+str(self.timestamp)

class TheftReportImage(models.Model):
    """
    TheftReport model
    """
    crime_report = models.ForeignKey(TheftReport, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name_plural = 'Theft Reports Images'
        ordering = ['-timestamp']
        db_table = 'theft_reports_images'

    def __str__(self):
        return str(self.timestamp)

class TheftReportVideo(models.Model):
    """
    TheftReportVideo model
    """
    crime_report = models.ForeignKey(TheftReport, on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name_plural = 'Theft Reports Videos'
        ordering = ['-timestamp']
        db_table = 'theft_reports_videos'

    def __str__(self):
        return self.video.name + ' - ' + str(self.timestamp)

class MostWanted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(100, 100)], format='JPEG', options={'quality': 60})
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    is_captured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Most Wanted'
        ordering = ['-timestamp']
        db_table = 'most_wanted'

    def __str__(self):
        return self.location_description+'-'+str(self.timestamp)

class MostWantedImages(models.Model):
    """
    MostWanted model
    """
    crime_report = models.ForeignKey(MostWanted, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name_plural = 'Most Wanted Images'
        ordering = ['-timestamp']
        db_table = 'most_wanted_images'

    def __str__(self):
        return str(self.timestamp)