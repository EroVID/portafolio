from posixpath import relpath
from django.urls import path
from . import views

urlpatterns = [ 
    path("proyectos/", views.proyectos, name="Proyectos"),
    relpath("contacts/", views.contactame, name="contactame"),
    relpath(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]