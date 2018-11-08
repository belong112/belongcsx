"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name = 'home'),
    path('add/' , views.add, name = 'add'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/',views.login),
    path('register/',views.register),
    path('changepassword/',views.changepassword,name = 'change'),
    path('myfav/<int:user_id>/delete/<int:song_id>/', views.delete),
    path('myfav/<int:user_id>/', views.myfav , name = 'myfav'),
    # url(r'^myfav/(?P<user_id>[0-9]+)/$',views.myfav,name = 'myfav'),
    url(r'^addfav/(?P<song_id>[0-9]+)/(?P<user_id>[0-9]+)/$',views.addfav),
    # url(r'^myfav/([0-9]+)/delete/(?P<song_id>[0-9]+)/(?P<user_id>[0-9]+)/$',views.delete),
    # url(r'^pic$', views.picture, name="pic"),
]
