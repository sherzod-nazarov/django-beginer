from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import CarAbout

hozir = datetime.now()
ismlar = ["Bexruz", "Sherzod", "Usmon", "Baxodir"]


def HomePage(request):
    moshinalar = CarAbout.objects.all()
    return render(request, 'index.html', {'moshinalar': moshinalar})


def AboutPage(request):
    if request.method == "POST":
        name = request.POST.get('nomi')
        model = request.POST.get('model')
        color = request.POST.get('rang')
        speed = request.POST.get('tezlik')
        CarAbout.objects.create(name=name, model=model, color=color, speed=speed)
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
        car.name=name
        car.model = model
        car.color = color
        car.speed = speed
        car.save()
        return redirect('home')
    return render(request, 'about.html', {'vaqt':hozir})









def DeleteCar(request, id):
    car = CarAbout.objects.get(id=id)
    car.delete()
    return redirect('home')




def SignUp(request, id=2025, str="salom", slug="salom-slug"):
    return render(request, 'signup.html', {'id':id, 'str':str, 'slug':slug})