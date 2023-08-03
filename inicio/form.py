from django import forms
from django.contrib.auth.models import User

class clienteformulariobase(forms.Form):
     nombre= forms.CharField(max_length=20)
     edad= forms.IntegerField()
     nacionalidad= forms.CharField(max_length=20)
    #  imagen= forms.ImageField(required=False)  
    

class Crearclienteformulario(clienteformulariobase):
    ...
    
class modificarclienteformulario (clienteformulariobase):
   ...
   
   
class buscarclienteformulario(forms.Form):
    nombre= forms.CharField(max_length=20,required= False)
   