from django.contrib import admin
from .models import Instructor,Taller,postulaciones
# Register your models here.

# Clase taller

class TallerAdmin(admin.ModelAdmin):
    list_display = ["nombre","descripcion","Instructor","imagen","cupos","curso","fecha_inicio","horario"]
    list_editable = ["descripcion"]
    search_fields =["nombre"]
    list_filter = ["nombre","cupos","curso","fecha_inicio"]
    list_per_page = 10
    




admin.site.register(Instructor)
admin.site.register(Taller,TallerAdmin)
admin.site.register(postulaciones)