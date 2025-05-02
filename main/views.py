from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import CarAbout
import wikipedia


hozir = datetime.now()
ismlar = ["Bexruz", "Sherzod", "Usmon", "Baxodir"]


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
    moshinalar = CarAbout.objects.all()
    return render(request, 'home.html', {'moshinalar': moshinalar})


def AboutPage(request):
    if request.method == "POST":
        name = request.POST.get('nomi')
        model = request.POST.get('model')
        color = request.POST.get('rang')
        speed = request.POST.get('tezlik')
        rasm = request.FILES.get('rasm')
        print(rasm)
        CarAbout.objects.create(name=name, rasm=rasm, model=model, color=color, speed=speed)
        print(name, model, color, speed)
        return redirect('home')
    return render(request, 'about.html', {'vaqt':hozir})



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




def SignUp(request, id=2025, str="salom", slug="salom-slug"):
    return render(request, 'signup.html', {'id':id, 'str':str, 'slug':slug})