from django.contrib import admin
from .models import CrimeReport, CrimeReportImage, CrimeReportVideo

# TabularInline and StackedInline are used to display the images and videos in the admin page
class CrimeReportImageInline(admin.TabularInline):
    model = CrimeReportImage
    extra = 1

# TabularInline and StackedInline are used to display the images and videos in the admin page
class CrimeReportVideoInline(admin.TabularInline):
    model = CrimeReportVideo
    extra = 1

# Register your models here.
class CrimeReportAdmin(admin.ModelAdmin):
    list_display = ('location', 'timestamp', 'user')
    inlines = [CrimeReportImageInline, CrimeReportVideoInline]

# Register your models here.
admin.site.register(CrimeReport, CrimeReportAdmin)