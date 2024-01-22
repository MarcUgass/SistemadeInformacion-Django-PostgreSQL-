from django.urls import path

from . import views

urlpatterns = [
    path("", views.index2, name="index2"),
    path("inicioSesion", views.inicioSesion, name="inicioSesion"),
    path("registro", views.registro, name="registro"),
    path("perfil", views.perfil, name="perfil"),
    path("reservas", views.reservas, name="reservas"),
    path("genBD", views.generarBaseDeDatos, name="genBD"),
]