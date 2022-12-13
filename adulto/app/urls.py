from django.urls import path
from . views import index, contacto, evaluacion, postulaciones, talleres\
    ,login, evaluacion, postulaciones, registro, modificar_taller, eliminar_taller
urlpatterns = [
    path('', index, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('evaluacion/', evaluacion, name="evaluacion"),
    path('postulaciones/', postulaciones, name="postulaciones"),
    path('talleres/', talleres, name="talleres"),
    path('login/', login, name="login"),
    path('evaluacion/', evaluacion, name="evaluacion"),
    path('postulaciones/', postulaciones, name="postulaciones"),
    path('registro/', registro, name="registro"),
    path('modificar_taller/<id>/', modificar_taller, name="modificar_taller"),
    path('eliminar_taller/<id>/', eliminar_taller, name="eliminar_taller"),
]