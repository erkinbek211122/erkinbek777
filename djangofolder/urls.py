"""
URL configuration for djangofolder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from djangofolder.settings import DEBUG,MEDIA_URL,MEDIAFILE_DIRS,STATICFILES_DIRS,STATIC_URL
from myfolder.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
path('',index,name='index'),
path('portfolio/',porfolio,name='portfolio'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIAFILE_DIRS)
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

if  DEBUG:
        urlpatterns += static(MEDIA_URL, document_root=MEDIAFILE_DIRS)
        urlpatterns += static(STATIC_URL, document_root=STATICFILES_DIRS)