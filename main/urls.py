from django.urls import path
from .views import HomePage, AboutPage, SignUp, DeleteCar, UpdatePage, CarPage, LoginPage, LogoutPage, CategoryPage

urlpatterns = [
    path('', HomePage, name='home'),
    path('about/', AboutPage),
    path('login/', LoginPage, name='login'),
    path('signup/', SignUp, name='signup'),
    path('delete/<int:id>/', DeleteCar, name='delete'),
    path('update/<int:id>/', UpdatePage, name='update'),
    path('car/<int:id>/<str:name>/', CarPage, name='car'),
    path('logout/', LogoutPage, name='logout'),
    path('category/<str:slug>/', CategoryPage, name="category")
]