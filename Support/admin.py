from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from .models import Incident
from .models import Document
from .models import Device
# Register your models here.
class AdminRegister(admin.ModelAdmin):
    list_display = ('Description','Priority','Status', 'AssignedTo', 'Attachements')
admin.site.register(Incident,AdminRegister)


class AdminRegister(admin.ModelAdmin):
    list_display = ('Description', 'Attachements')
admin.site.register(Document,AdminRegister)

class AdminRegister(ImportExportModelAdmin):
    list_display = ('Name', 'Device', 'Model', 'SerialNumber', 'Online', 'Apple_Gmail_ID', 'Owner')
admin.site.register(Device,AdminRegister)