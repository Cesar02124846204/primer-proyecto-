from django.urls import path
from  inicio import views

urlpatterns = [
    path("",views.inicio),
    path("prueba/",views.prueba),
    path("segunda vista",views.segunda_vista),
    path("fecha_de_hoy/",views.fecha_de_hoy),
    path("saludo/", views.saludo),
    path("bienvenido/<str:nombre>/<str:apellido>/", views.bienvenido),
    path("crear_perro/<str:nombre>/<int:edad>/", views.crear_perro),
]