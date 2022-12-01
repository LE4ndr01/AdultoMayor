from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')
def contacto(request):
    return render(request, 'app/contacto.html')
def nosotros(request):
    return render(request, 'app/nosotros.html')