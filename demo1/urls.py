"""demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from demoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.site,name="site"),
    path('sign/',views.sign,name="sign"),
    path('log/',views.log,name="log"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('insert/', views.insert, name='insert'),
    path('insertView/', views.insertView, name='insertView'),
    path('display/',views.display,name='display'),
    path('deleteView/',views.deleteView,name='deleteView'),
    path('updateView/',views.updateView,name='updateView'),
    path('updateData/',views.updateData,name='updateData')
]
