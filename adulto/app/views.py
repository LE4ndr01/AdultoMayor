from django.shortcuts import render, redirect,get_object_or_404
from .models import Taller,Instructor
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


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

#def modificar_taller(request, id):
    
    #taller = get_object_or_404(Taller, id=id)
    #data = {
     #   'taller':tallerform(instance=taller)
    #}
   
   # if request.method == 'POST':
        #formulario = Tallerform(data=request.POST, instance=taller, files=request.FILES)
       # if formulario.is_valid():
      #      formulario.save()
     #       messages.success(request, "Taller modificado correctamente")
    #        return redirect(to="home")
   #     data["form"] = formulario
  #return render(request, 'app/crud/editar_taller.html',data)
#def eliminar_taller(request):
    
    #talleres = get_object_or_404(Taller, id=id)
    #talleres.delete()
    #return redirect(to="home")
  #return render(request, 'app/eliminar_taller.html')
def paginator(request):
  return render(request, 'app/paginator.html')