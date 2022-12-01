from django.urls import path
from . views import index, contacto, nosotros
urlpatterns = [
    path('', index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('nosotros/', nosotros, name="nosotros"),
]