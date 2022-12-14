from django.shortcuts import render, redirect,get_object_or_404
from .models import Taller,Instructor
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import FormTaller, CustomUserCreationForm


# Create your views here.

def index(request):
    return render(request, 'app/home.html')
def contacto(request):
    return render(request, 'app/contacto.html')
def evaluacion(request):
    return render(request, 'app/evaluacion.html')
def postulaciones(request):
    
 
    
    return render(request, 'app/postulaciones.html')
    
def talleres(request):
    
    talleres = Taller.objects.all()
    data = {
        'talleres':talleres
    }    
    
    return render(request, 'app/talleres.html',data)
def login(request):
    return render(request, 'app/login.html')
def evaluacion(request):
    return render(request, 'app/evaluacion.html')
def postulaciones(request):
    return render(request, 'app/postulaciones.html')    
def registro(request):
    data = {
        'form':CustomUserCreationForm()
    } 
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario   
    
    return render(request, 'registration/registro.html',data)

def agregar_taller(request):
    
    data = {
        'form':FormTaller()
    }
    
    if request.method == 'POST':
        formulario = FormTaller(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request, 'crud/agregar.html',data)

def listar_taller(request):

    return render(request, 'crud/listar.html',data)