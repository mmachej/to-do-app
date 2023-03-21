from django import forms
from django.forms import ModelForm

from .models import *


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'deadline']


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class CompleteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['complete']
