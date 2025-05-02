from django.urls import path
from .views import HomePage, AboutPage, SignUp, DeleteCar, UpdatePage, CarPage

urlpatterns = [
    path('', HomePage, name='home'),
    path('about/', AboutPage),
    path('signup/', SignUp),
    path('signup/<int:id>/<str:str>/<slug:slug>', SignUp),
    path('delete/<int:id>/', DeleteCar, name='delete'),
    path('update/<int:id>/', UpdatePage, name='update'),
    path('car/<int:id>/<str:name>/', CarPage, name='car')
]