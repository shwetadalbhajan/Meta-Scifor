from django.contrib import admin
from .models import MyModel

class MyModelAdmin(admin.ModelAdmin):
    list_display = ("author","title")

admin.site.register(MyModel,MyModelAdmin)