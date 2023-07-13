from django import forms

class clienteformulariobase(forms.Form):
     nombre= forms.CharField(max_length=20)
     edad= forms.IntegerField()
     nacionalidad= forms.CharField(max_length=20)
     
    

class Crearclienteformulario(clienteformulariobase):
    ...
    
class modificarclienteformulario (clienteformulariobase):
   ...
   
   
class buscarclienteformulario(forms.Form):
    nombre= forms.CharField(max_length=20,required= False)
   