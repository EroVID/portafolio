from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,"pages/inicio.html",{})

def portafolio(request):
    return render(request,"pages/portafolio.html",{})

def resume(request):
    return render(request,"pages/resume.html",{})

def contact(request):
    return render(request,"pages/contact.html",{})