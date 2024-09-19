from django import forms
from .models import *

class CreateTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

class UpdateTaskForm(forms.ModelForm):
    completed = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

