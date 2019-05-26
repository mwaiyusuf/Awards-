from django import forms
from .models import Image,Review,Profile,Project 
from django.forms import ModelForm,Textare,IntegerField  

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user',]

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user',]
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'usability_rating', 'design_rating', 'content_rating' , 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }