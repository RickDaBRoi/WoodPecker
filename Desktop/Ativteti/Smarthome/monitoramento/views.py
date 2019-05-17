from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

#pagina inicial
class InicioView(TemplateView):
	template_name = "index.html"

#pagina curriculo
class CurriculoView(TemplateView):
	template_name = "curriculo.html"

#pagina sobre
class SobreView(TemplateView):
	template_name = "sobre.html"
