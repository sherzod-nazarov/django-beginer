from django.shortcuts import render, redirect
from datetime import datetime
from .models import CarAbout, Categorys
import wikipedia
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator


hozir = datetime.now()
ismlar = ["Bexruz", "Sherzod", "Usmon", "Baxodir"]

def CategoryPage(request, slug):
    moshinlar = CarAbout.objects.filter(model__slug=slug)
    category = Categorys.objects.get(slug=slug)
    return render(request, 'category.html', {'moshinalar':moshinlar, 'category':category})





def CarPage(request, id, name):
    moshin = CarAbout.objects.get(id=id)
    nomi = moshin.name
    try:
        wikipedia.set_lang('uz')
        car1 = wikipedia.summary(f"{nomi}")
    except:
        car1 = "Malumot topolmadim"
    return render(request, 'car.html', {"car1": car1, 'moshin':moshin})




def HomePage(request):
    if request.user.is_authenticated:
        moshinalar = CarAbout.objects.all()
        paginator = Paginator(moshinalar, 1)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request, 'home.html', {'posts': posts, 'page':page})
    else:
        return redirect('signup')

"""Bu bizning loyiha emas"""
def AboutPage(request):
    categorys = Categorys.objects.all()
    if request.method == "POST":
        name = request.POST.get('nomi')
        model_id = request.POST.get('model')
        color = request.POST.get('rang')
        speed = request.POST.get('tezlik')
        rasm = request.FILES.get('rasm')
        model_name = Categorys.objects.get(id=model_id)
        CarAbout.objects.create(name=name, rasm=rasm, model=model_name, color=color, speed=speed)
        return redirect('home')
    return render(request, 'about.html', {'categorys':categorys})



def UpdatePage(request, id):
    car = CarAbout.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get('nomi')
        model = request.POST.get('model')
        color = request.POST.get('rang')
        speed = request.POST.get('tezlik')
        rasm = request.FILES.get('rasm')
        car.name=name
        car.model = model
        car.color = color
        car.speed = speed
        car.rasm = rasm
        car.save()
        return redirect('home')
    return render(request, 'about.html', {'vaqt':hozir})




def DeleteCar(request, id):
    car = CarAbout.objects.get(id=id)
    car.delete()
    return redirect('home')




def SignUp(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password2 == password1:
            if User.objects.filter(username = username).exists():
                print("bu nom oldin foydalanilgan")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                print("Bu emaildan oldin foydalanilgan")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                login(request, user)
                print("Royhatdan o'tdingiz")
                return redirect('home')
        else:
            print("parollar mos emas")
            return redirect('signup')
    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Royhatdan o'tdingiz")
            return redirect('home')
        else:
            print("Xato qildingiz")
    return render(request, 'login.html')




def LogoutPage(request):
    logout(request)
    return redirect('home')