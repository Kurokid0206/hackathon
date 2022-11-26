from django.contrib import admin
from django.urls import path
from green_recycle.views.index import index

app_name = "green_recycle"

urlpatterns = [
    path("", index, name="index"),
]
