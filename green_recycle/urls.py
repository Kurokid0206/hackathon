from django.contrib import admin
from django.urls import path
from green_recycle.views import index, blog

app_name = "green_recycle"

urlpatterns = [
    path("", index.home, name="index"),
    path("index1", index.home1, name="index1"),
    path("index2", index.home2, name="index2"),
    path("index3", index.home3, name="index3"),
    path("blog", blog.get_blog, name="get_blog"),
    path("blog-detail/<int:blog_id>", blog.blog_detail, name="blog_detail"),
]
