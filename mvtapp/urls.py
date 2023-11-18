"""
URL configuration for mvtproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from mvtapp import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('data', views.data, name='data'),
    path('insert', views.insert, name='insert'),
    path('delete/<id>', views.delete, name='delete'),
    path('update/<id>', views.update, name='update'),
    path('login', views.signin, name='login'),
    path('', views.register, name='register'),
    path('logout', views.logoutp, name='logout'),
]