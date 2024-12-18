from django.urls import path
from .views import *

urlpatterns = [
    path('', getData, name="get"),
    path('post/', postData, name="post"),
    path('put/<int:pk>/', putData, name="put"),
    path('delete/<int:pk>/', deleteData, name="delete"),
    path('patch/<int:pk>/', patchData, name="patch"),
]
