from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ("name","job_title")

admin.site.register(Data,DataAdmin)