from django.contrib import admin
from .models import Serverlist
# Register your models here.

from import_export.admin import ExportActionModelAdmin, ImportExportMixin

class ServerlistAdmion(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id','name','server_count','model_name','code','use_case','created_date','published_date']

admin.site.register(Serverlist, ServerlistAdmion)



#class ServerlistOption(admin.ModelAdmin):
#    list_display = ['id','name','server_count','model_name','code','use_case','created_date','published_date']
#admin.site.register(Serverlist, ServerlistOption)




