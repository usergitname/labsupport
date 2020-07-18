# Generated by Django 3.0.8 on 2020-07-18 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default=' ', max_length=2083)),
                ('Device', models.CharField(default=' ', max_length=2083)),
                ('Model', models.CharField(default=' ', max_length=2083)),
                ('SerialNumber', models.CharField(default=' ', max_length=2083)),
                ('Online', models.CharField(default=' ', max_length=2083)),
                ('Apple_Gmail_ID', models.CharField(default=' ', max_length=2083)),
                ('Owner', models.CharField(default=' ', max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(default=' ', max_length=2083)),
                ('Attachements', models.FileField(default=' ', upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(default=' ', max_length=2083)),
                ('Priority', models.CharField(choices=[('defaul', ' '), ('critical', 'CRITICAL'), ('high', 'HIGH'), ('low', 'LOW')], default='Select Priority', max_length=2083)),
                ('Status', models.CharField(choices=[('defaul', ' '), ('open', 'OPEN'), ('inprogress', 'IN-PROGRESS'), ('fixed', 'FIXED')], default='Select Status', max_length=2083)),
                ('AssignedTo', models.CharField(choices=[('defaul', ' '), ('Shri', 'Shri'), ('Joshi', 'Joshi'), ('Satya', 'Satya')], default='Select Assigned To ', max_length=2083)),
                ('Attachements', models.FileField(default=' ', upload_to='media')),
            ],
        ),
    ]
