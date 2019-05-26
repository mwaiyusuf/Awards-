from django import forms
from .models import Image,Review,Profile,Project 
from django.forms import ModelForm,Textare,IntegerField  

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user',]
