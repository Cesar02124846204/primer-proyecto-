from django import forms
class Crearclienteformulario(forms.Form):
    nombre= forms.CharField(max_length=20)
    edad= forms.IntegerField()
    nacionalidad= forms.CharField(max_length=20)

class buscarclienteformulario(forms.Form):
    nombre= forms.CharField(max_length=20,required= False)
   