"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from main.views import HomePage, AboutPage, SignUp, DeleteCar, UpdatePage

urlpatterns = [
    path('', HomePage, name='home'),
    path('admin/', admin.site.urls),
    path('about', AboutPage),
    path('signup/', SignUp),
    path('signup/<int:id>/<str:str>/<slug:slug>', SignUp),
    path('delete/<int:id>/', DeleteCar, name='delete'),
    path('update/<int:id>/', UpdatePage, name='update')
]
