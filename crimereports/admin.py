from django.contrib import admin
from .models import *

class CountyAdmin(admin.ModelAdmin):
    list_diplay = ('name','county_no')

admin.site.register(County, CountyAdmin)

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
    list_display = ('county', 'timestamp', 'user')
    inlines = [CrimeReportImageInline, CrimeReportVideoInline]

# Register your models here.
admin.site.register(CrimeReport, CrimeReportAdmin)


class TerrorismImageInline(admin.TabularInline):
    model = TerrorismReportImage
    extra = 1

class TerrorismVideoInline(admin.TabularInline):
    model = TerrorismReportVideo
    extra = 1

class TerrorismReportAdmin(admin.ModelAdmin):
    list_display = ('county', 'timestamp', 'user')
    inlines = [TerrorismImageInline, TerrorismVideoInline]

admin.site.register(Terrorism, TerrorismReportAdmin)



class SuspiciousActivityImageInline(admin.TabularInline):
    model = SuspiciousActivityReportImage
    extra = 1

class SuspiciousActivityVideoInline(admin.TabularInline):
    model = SuspiciousReportVideo
    extra = 1

class SuspiciousActivityReportAdmin(admin.ModelAdmin):
    list_display = ('county', 'timestamp', 'user')
    inlines = [SuspiciousActivityImageInline, SuspiciousActivityVideoInline]

admin.site.register(SuspiciousActivity, SuspiciousActivityReportAdmin)



class LostItemImageInline(admin.TabularInline):
    model = LostItemReportImage
    extra = 1

class LostItemVideoInLine(admin.TabularInline):
    model = LostItemVideo
    extra = 1

class LostItemReportAdmin(admin.ModelAdmin):
    list_display = ('county', 'timestamp', 'user')
    inlines = [LostItemImageInline, LostItemVideoInLine]

admin.site.register(LostItem, LostItemReportAdmin)


class TheftReportImageInline(admin.TabularInline):
    model = TheftReportImage
    extra = 1

class TheftReportVideoInline(admin.TabularInline):
    model = TheftReportVideo
    extra = 1

class TheftReportAdmin(admin.ModelAdmin):
    list_display = ('county', 'timestamp', 'user')
    inlines = [TheftReportImageInline, TheftReportVideoInline]

admin.site.register(TheftReport, TheftReportAdmin)


class MostWantedImageInline(admin.TabularInline):
    model = MostWantedImages
    extra = 1

class MostWantedReportAdmin(admin.ModelAdmin):
    list_display = ('county', 'timestamp', 'user')
    inlines = [MostWantedImageInline]

admin.site.register(MostWanted, MostWantedReportAdmin)