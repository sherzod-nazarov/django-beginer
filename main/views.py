from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

hozir = datetime.now()
ismlar = ["Bexruz", "Sherzod", "Usmon", "Baxodir"]


def HomePage(request):
    print(request)
    return render(request, 'index.html', {'ismlar': ismlar})


def AboutPage(request):
    return render(request, 'about.html', {'vaqt':hozir})
# Create your views here.

def SignUp(request, id=2025, str="salom", slug="salom-slug"):
    return render(request, 'signup.html', {'id':id, 'str':str, 'slug':slug})