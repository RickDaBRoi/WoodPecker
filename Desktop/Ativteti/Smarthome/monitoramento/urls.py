from django.urls import path
from .views import *


urlpatterns = [
    path('', InicioView.as_view(), name="index" ),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('curriculo/', CurriculoView.as_view(), name="curriculo" ),
]
