from django.urls import path
from . views import index, contacto, evaluacion, postulaciones, talleres
urlpatterns = [
    path('', index, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('evaluacion/', evaluacion, name="evaluacion"),
    path('postulaciones/', postulaciones, name="postulaciones"),
    path('talleres/', talleres, name="talleres"),
]