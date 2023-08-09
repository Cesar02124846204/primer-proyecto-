from django import forms
from django.contrib.auth.models import User
from .models import Cliente

class clienteformulariobase(forms.Form):
     nombre= forms.CharField(max_length=20)
     edad= forms.IntegerField()
     fecha= forms.DateField()
     nacionalidad= forms.CharField(max_length=20)
     imagen= forms.ImageField(required=False)  

# class clienteformulariobase(forms.ModelForm):
#     class Meta:
#         model=Cliente
#         fields = ["nombre", "edad", "nacionalidad", "imagen"]
    

class Crearclienteformulario(clienteformulariobase):
    ...
    
class modificarclienteformulario (clienteformulariobase):
   ...
   
   
class buscarclienteformulario(forms.Form):
    nombre= forms.CharField(max_length=20,required= False)
   