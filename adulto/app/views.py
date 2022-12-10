from django.shortcuts import render

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
    return render(request, 'app/talleres.html')
def login(request):
    return render(request, 'app/login.html')
def evaluacion(request):
    return render(request, 'app/evaluacion.html')
def postulaciones(request):
    return render(request, 'app/postulaciones.html')    