from django.contrib import admin
from .models import *

class PersonAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date")

class CollegeAdmin(admin.ModelAdmin):
  list_display = ("name","college","address")

admin.site.register(Person,PersonAdmin)
admin.site.register(College,CollegeAdmin)