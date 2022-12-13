from django.urls import path
from . views import index, contacto, evaluacion, postulaciones, talleres, login, evaluacion, postulaciones, registro
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
]