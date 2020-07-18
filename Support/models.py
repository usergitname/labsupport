from django.db import models

# Create your models here.
class Incident(models.Model):
    PRIORITY_CHOICES = (
        ('defaul', ' '),
        ('critical', 'CRITICAL'),
        ('high', 'HIGH'),
        ('low', 'LOW'),
    )

    STATUS_CHOICES = (
        ('defaul', ' '),
        ('open', 'OPEN'),
        ('inprogress', 'IN-PROGRESS'),
        ('fixed', 'FIXED'),
    )

    ASSIGNEDTO_CHOICES = (
        ('defaul', ' '),
        ('Shri', 'Shri'),
        ('Joshi', 'Joshi'),
        ('Satya', 'Satya'),
    )

    Description = models.CharField(max_length=2083,default=' ')
    Priority =  models.CharField(max_length=2083, choices=PRIORITY_CHOICES, default='Select Priority')
    Status = models.CharField(max_length=2083, choices=STATUS_CHOICES, default='Select Status')
    AssignedTo = models.CharField(max_length=2083, choices=ASSIGNEDTO_CHOICES, default='Select Assigned To ')
    Attachements = models.FileField(upload_to='media',default=' ')


class Document(models.Model):
    Description = models.CharField(max_length=2083, default=' ')
    Attachements = models.FileField(upload_to='media', default=' ')


class Device(models.Model):
    Name = models.CharField(max_length=2083, default=' ')
    Device = models.CharField(max_length=2083, default=' ')
    Model = models.CharField(max_length=2083, default=' ')
    SerialNumber = models.CharField(max_length=2083, default=' ')
    Online = models.CharField(max_length=2083, default=' ')
    Apple_Gmail_ID = models.CharField(max_length=2083, default=' ')
    Owner = models.CharField(max_length=2083, default=' ')