from django import forms
from .models import Taller, Instructor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class CustomUserCreationForm(UserCreationForm):
   def clean_nombre(self):
      nombre = self.cleaned_data['nombre']
      existe = User.objects.filter(nombre__iexact=nombre).exists()
      
      if existe:
         raise ValidationError("Nombre ya existe")
   class Meta:
      model = User
      fields =['username', "password1","password2"]

class FormTaller (forms.ModelForm):

   class Meta:
          model = Taller
          fields = '__all__'
          

