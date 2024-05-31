"""
URL configuration for djangoproyect project.

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
from django.contrib import admin
from django.urls import path, include 
from .views import inicio, resume
from .views import portafolio
from .views import resume
from .views import contact


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('portafolio/', portafolio),
    path('resumen/', resume),
    path('contacto/', contact),
    path("", include('Aplicaciones.portafolio.urls')),
    path('', include('Aplicaciones.contacts.urls'))

]
