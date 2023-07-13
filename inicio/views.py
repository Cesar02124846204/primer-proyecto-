from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Cliente
from django.shortcuts import render, redirect
from inicio.form import Crearclienteformulario, buscarclienteformulario, modificarclienteformulario
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

def inicio(request):
    return render(request,"inicio/inicio.html")
def prueba(request):
    
    
    segundos = datetime.now().second
    diccionario={
        "mensaje": "este es el mensaje de inicio",
        "segundos" : segundos ,
        "segundos_par": segundos%2 == 0 ,
        "segundo_redondo":segundos %10 == 0 ,
        "listado_segundos": list(range(25))
    }
    return render(request, "inicio/prueba.html", diccionario)

    segundos = datetime.now().second
    diccionario={
        "mensaje": "este es el mensaje de inicio",
        "segundos" : segundos ,
        "segundos_par": segundos%2 == 0 ,
        "segundo_redondo":segundos %10 == 0 ,
        "listado_segundos": list(range(25))
    }
    return render(request, "inicio/prueba.html", diccionario)



def segunda_vista(request):
    return HttpResponse("<h1>soy la segunda vista</h1>")


def fecha_de_hoy(request):
    fecha= datetime.now()
    return HttpResponse(f"fecha actual {fecha}")


def saludo(request):
    return HttpResponse("bienvenido")


def bienvenido(request, nombre , apellido):
    return HttpResponse(f"bienvenido {nombre.title()}, {apellido.title()}")

            
            
    formulario = Crearclienteformulario()
    return render(request, "inicio/crear_cliente.html",  {"formulario": formulario})


class CrearCliente(CreateView):
    model= Cliente
    template_name= "inicio/CBV/crear_cliente_CBV.html"
    fields= ["nombre", "edad", "nacionalidad", "descripcion"]
    success_url= reverse_lazy("inicio:lista_de_clientes")
    
class Listaclientes(ListView):
    model = Cliente
    template_name = "inicio/CBV/lista_de_cliente_CBV.html"
    context_object_name="clientes"
    
class ModificarCliente(UpdateView):
    model = Cliente
    template_name = "inicio/CBV/modificar_cliente_CBV.html"
    fields= ["nombre", "edad", "nacionalidad", "descripcion"]
    success_url= reverse_lazy("lista_de_clientes")

class Eliminarcliente(DeleteView):
    model = Cliente
    template_name = "inicio/CBV/eliminar_cliente_CBV.html"
    success_url= reverse_lazy("lista_de_clientes")
    
class Descripciondelcliente(DetailView):
    model = Cliente
    template_name = "inicio/CBV/descripcion_del_cliente_CBV.html"
    