"""djangotemplateexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,re_path
from videoshow import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    re_path(r'^(\d{1})/$', views.index, name='tv-url')
]
#
# <iframe height=498 width=510 src='http://player.youku.com/embed/XMzA3ODcyMTA4MA==' frameborder=0 'allowfullscreen'></iframe>
# <iframe height=498 width=510 src='http://player.youku.com/embed/XMTU5OTM2MTc1Mg==' frameborder=0 'allowfullscreen'></iframe>
# <iframe height=498 width=510 src='http://player.youku.com/embed/XNzQzMTY4NjA4' frameborder=0 'allowfullscreen'></iframe>
