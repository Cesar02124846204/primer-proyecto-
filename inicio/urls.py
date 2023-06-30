from django.urls import path
from  inicio import views

urlpatterns = [
    path("",views.inicio, name="inicio"),
    
    path("segunda vista",views.segunda_vista, name="segunda_vista"),
    path("fecha_de_hoy/",views.fecha_de_hoy, name="fecha_de_hoy"),
    path("saludo/", views.saludo, name= "saludo"),
    path("bienvenido/<str:nombre>/<str:apellido>/", views.bienvenido, name= "saludar"),
    path("cliente/crear/", views.crear_cliente, name="craer_cliente"),
    path("clientes/", views.lista_de_clientes, name="lista_de_clientes")
]