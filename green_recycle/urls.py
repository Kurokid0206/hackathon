from django.contrib import admin
from django.urls import path
from .views import index

app_name = 'green_recycle'

urlpatterns = [
    path('', index.index, name='index'),
]