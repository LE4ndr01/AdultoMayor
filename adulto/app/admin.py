from django.contrib import admin
from .models import Instructor,Taller
# Register your models here.

# Clase taller

class TallerAdmin(admin.ModelAdmin):
    list_display = ["nombre","descripcion","instructor"]
    list_editable = ["descripcion"]
    search_fields =["nombre"]
    list_filter = ["instructor","nuevo"]
    list_per_page = 10
    




admin.site.register(Instructor)
admin.site.register(Taller)