from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . models import *

# Register your models here.

class RegiserUser(admin.ModelAdmin):
    list_display = ("Firstname","Lastname","email","password","confirmpassword")


admin.site.register(Register,RegiserUser)
# Register your models here.
