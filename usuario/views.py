from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from usuario.form import MiFormalarioDeCreacionDeUsarios, MiFormularioDeEdicionDeDatosDeUsuario,buscarUsuarioformulario
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from usuario.models import InfoExtra, User
from django.views.generic.detail import DetailView



def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']
            
            user = authenticate(username=usuario, password=contrasenia)
            
            django_login(request, user)
            
            InfoExtra.objects.get_or_create(user=user)
           
            
            return redirect('inicio')
        else:
            return render(request, 'usuario/login.html',  {'formulario': formulario})
            
    formulario = AuthenticationForm()
    return render(request, 'usuario/login.html',  {'formulario': formulario})
    # return render(request, "usuario/login.html")
    
def registrarse(request):
    
    if request.method == 'POST':
        formulario = MiFormalarioDeCreacionDeUsarios(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("usuario:login")
        else:
            return render(request, 'usuario/registrarse.html', {'formulario': formulario})


    formulario = MiFormalarioDeCreacionDeUsarios()
    return render(request, 'usuario/registrarse.html', {'formulario': formulario})


@login_required
def edicion_de_perfil(request):
    info_extra_user = request.user.infoextra
    if request.method == 'POST':
        formulario = MiFormularioDeEdicionDeDatosDeUsuario(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            avatar = formulario.cleaned_data.get('avatar')
            if avatar:
                info_extra_user.avatar = avatar
                
            edad = formulario.cleaned_data.get('edad')
            if edad:
                info_extra_user.edad = edad
            
            info_extra_user.save()
            
            formulario.save()
            return redirect('inicio')
    else:
        formulario = MiFormularioDeEdicionDeDatosDeUsuario(initial={'avatar': info_extra_user.avatar, 'edad': info_extra_user.edad}, instance=request.user)
        
    return render(request, 'usuario/edicion_de_perfil.html', {'formulario': formulario})


class ModificarPass(LoginRequiredMixin,PasswordChangeView):
    template_name= "usuario/modificar_pass.html"
    success_url = reverse_lazy('usuario:edicion_de_perfil')
    
    
class perfildelusario(ListView):
    # model = Cliente
    # template_name = "inicio/CBV/lista_de_cliente_CBV.html"
    # context_object_name="clientes"
    model =InfoExtra
    template_name = "usuario/perfil_del_usuario.html"
    context_object_name = 'usuario'
    def get_queryset(self):
        listado_de_usuarios= []
        formulario = buscarUsuarioformulario(self.request.GET)
        if formulario.is_valid():
            nombre_a_buscar = formulario.cleaned_data['Nombre']
            users = User.objects.filter(first_name__icontains=nombre_a_buscar)
            listado_de_usuarios = InfoExtra.objects.filter(user_id__in=users.values("id"))
        return listado_de_usuarios
    
    
# class PerfilDelUsario(DetailView):
#     model =InfoExtra
#     template_name = "usuario/perfil_del_cliente.html"
    