from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Perro
from django.shortcuts import render
# v1
# def inicio(request):
#     return  HttpResponse("hola soy tu inicio")
# v2
# def inicio(request):
#     archivo= open(r"C:\Users\cessa\OneDrive\Escritorio\mi_primer_django\templates\inicio.html", "r")
#     template= Template (archivo.read())
#     archivo.close()
#     segundos = datetime.now().second
#     diccionario={
#         "mensaje": "este es el mensaje de inicio",
#         "segundos" : segundos ,
#         "segundos_par": segundos%2 == 0 ,
#         "segundo_redondo":segundos %10 == 0 ,
#         "listado_segundos": list(range(25))
#     }
#     contexto=Context(diccionario)
#     renderizar_template= template.render(contexto)
#     return HttpResponse(renderizar_template)
# v3
# def inicio(request):
#     template= loader.get_template("inicio.html")
#     segundos = datetime.now().second
#     diccionario={
#         "mensaje": "este es el mensaje de inicio",
#         "segundos" : segundos ,
#         "segundos_par": segundos%2 == 0 ,
#         "segundo_redondo":segundos %10 == 0 ,
#         "listado_segundos": list(range(25))
#     }
    
#     renderizar_template= template.render(diccionario)
#     return HttpResponse(renderizar_template)
# v4
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



def segunda_vista(request):
    return HttpResponse("<h1>soy la segunda vista</h1>")


def fecha_de_hoy(request):
    fecha= datetime.now()
    return HttpResponse(f"fecha actual {fecha}")


def saludo(request):
    return HttpResponse("bienvenido")


def bienvenido(request, nombre , apellido):
    return HttpResponse(f"bienvenido {nombre.title()}, {apellido.title()}")
#v1
# def crear_perro(request, nombre , edad):
#     template= loader.get_template("crear_perro.html")
#     perro= Perro(nombre= nombre, edad= edad)
#     perro.save()
    
#     diccionario={
#         "perro": perro
#     }
#     renderizar_template= template.render(diccionario)
#     return HttpResponse(renderizar_template)

def crear_perro(request, nombre , edad):
    perro= Perro(nombre= nombre, edad= edad)
    perro.save()
    
    diccionario={
        "perro": perro
    }
    return render(request, "inicio/crear_perro.html", diccionario)