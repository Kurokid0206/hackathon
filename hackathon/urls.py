"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework.routers import SimpleRouter
from hackathon.views.user import UserProfileViewSet
from hackathon.views.product import ProductViewSet
from hackathon.configs import settings
router = SimpleRouter(trailing_slash=False)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('green_recycle.urls')),

    # set up an API with ckeditor
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
urlpatterns += url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

router.register(r"api/user-profile", UserProfileViewSet, "user-profile")
router.register(r"api/product", ProductViewSet, "product")
urlpatterns += router.urls
