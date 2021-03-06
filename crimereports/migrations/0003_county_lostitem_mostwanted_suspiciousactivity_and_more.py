# Generated by Django 4.0.4 on 2022-06-22 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crimereports', '0002_remove_crimereport_slug_crimereport_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('county_no', models.PositiveSmallIntegerField(unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Counties',
                'db_table': 'counties',
                'ordering': ['county_no'],
            },
        ),
        migrations.CreateModel(
            name='LostItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_description', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crimereports.county')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Lost Items',
                'db_table': 'lost_items',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='MostWanted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')),
                ('description', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crimereports.county')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Most Wanted',
                'db_table': 'most_wanted',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='SuspiciousActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_description', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crimereports.county')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Suspicious Activities',
                'db_table': 'suspicious_activities',
            },
        ),
        migrations.CreateModel(
            name='Terrorism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_description', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crimereports.county')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Terrorism',
                'db_table': 'terrorism',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='TheftReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_description', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crimereports.county')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Theft Reports',
                'db_table': 'theft_reports',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AlterModelOptions(
            name='crimereport',
            options={'ordering': ['-timestamp'], 'verbose_name_plural': 'Crime Reports'},
        ),
        migrations.AlterModelOptions(
            name='crimereportimage',
            options={'ordering': ['-timestamp'], 'verbose_name_plural': 'Crime Report Images'},
        ),
        migrations.AlterModelOptions(
            name='crimereportvideo',
            options={'ordering': ['-timestamp'], 'verbose_name_plural': 'Crime Report Videos'},
        ),
        migrations.RemoveField(
            model_name='crimereport',
            name='location',
        ),
        migrations.AlterModelTable(
            name='crimereport',
            table='crime_reports',
        ),
        migrations.AlterModelTable(
            name='crimereportimage',
            table='crime_report_images',
        ),
        migrations.AlterModelTable(
            name='crimereportvideo',
            table='crime_report_videos',
        ),
        migrations.CreateModel(
            name='TheftReportVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/%Y/%m/%d')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('crime_report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimereports.theftreport')),
            ],
            options={
                'verbose_name_plural': 'Theft Reports Videos',
                'db_table': 'theft_reports_videos',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='TheftReportImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('crime_report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimereports.theftreport')),
            ],
            options={
                'verbose_name_plural': 'Theft Reports Images',
                'db_table': 'theft_reports_images',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='TerrorismReportVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/%Y/%m/%d')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('crime_report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimereports.terrorism')),
            ],
            options={
                'verbose_name_plural': 'Terrorism Report Videos',
                'db_table': 'terrorism_report_videos',
            },
        ),
        migrations.CreateModel(
            name='TerrorismReportImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('crime_report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimereports.terrorism')),
            ],
            options={
                'verbose_name_plural': 'Terrorism Report images',
                'db_table': 'terrorism_report_images',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='SuspiciousReportVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/%Y/%m/%d')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('crime_report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimereports.suspiciousactivity')),
            ],
            options={
                'verbose_name_plural': 'Suspicious Activities Videos',
                'db_table': 'suspicious_activities_videos',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='SuspiciousActivityReportImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('crime_report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimereports.suspiciousactivity')),
            ],
            options={
                'verbose_name_plural': 'Suspicious Activities Images',
                'db_table': 'suspicious_activities_images',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='MostWantedImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('crime_report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimereports.mostwanted')),
            ],
            options={
                'verbose_name_plural': 'Most Wanted Images',
                'db_table': 'most_wanted_images',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='LostItemVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/%Y/%m/%d')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('crime_report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimereports.lostitem')),
            ],
            options={
                'verbose_name_plural': 'Lost Items Videos',
                'db_table': 'lost_items_videos',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='LostItemReportImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('crime_report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimereports.lostitem')),
            ],
            options={
                'verbose_name_plural': 'Lost Items Images',
                'db_table': 'lost_items_images',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AddField(
            model_name='crimereport',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimereports.county'),
        ),
    ]
