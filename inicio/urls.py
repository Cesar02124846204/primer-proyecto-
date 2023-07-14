from django.urls import path
from  inicio import views

urlpatterns = [
    path("",views.inicio, name="inicio"),
    path("About/",views.acercademi, name="acercademi"),
    path("segunda vista",views.segunda_vista, name="segunda_vista"),
    path("fecha_de_hoy/",views.fecha_de_hoy, name="fecha_de_hoy"),
    path("saludo/", views.saludo, name= "saludo"),
    path("bienvenido/<str:nombre>/<str:apellido>/", views.bienvenido, name= "saludar"),
    path("clientes/", views.Listaclientes.as_view(), name="lista_de_clientes"),
    path("cliente/crear/", views.CrearCliente.as_view(), name="craer_cliente"),
    path("cliente/eliminar/<int:pk>/", views.Eliminarcliente.as_view(), name="eliminar_cliente"),
    path("cliente/modificar/<int:pk>/", views.ModificarCliente.as_view(), name="modificar_cliente"),
    path("cliente/<int:pk>/", views.Descripciondelcliente.as_view(), name="descripcion_del_cliente"),
]