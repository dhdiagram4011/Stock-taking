from django.contrib import admin
from .models import *

class UserOption(admin.ModelAdmin):
    list_display = ['username','email','first_name','last_name','depart','position','phone','floor']

admin.site.register(User,UserOption)
