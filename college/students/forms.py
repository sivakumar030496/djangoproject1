from .models import Studentdata
from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm


class StudentsForm(forms.ModelForm):
    class Meta:
        model= Studentdata
        fields='__all__'


