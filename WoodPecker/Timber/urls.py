# módulo do Django para criar urls
from django.urls import path

# Importe todas suas classes do views.py
from .views import *

urlpatterns = [
    # path('caminho/da/url', ClasseLáDoView.as_view(), name="nomeDessaURL" )
	path('', PaginaInicialView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    
    # URLS de Estado
    path('cadastrar/estado/', EstadoCreate.as_view(), name="cadastrar-estado"),
    path('atualizar/estado/<int:pk>/', EstadoUpdate.as_view(), name="atualizar-estado"),
    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name="excluir-estado"),
    path('listar/estado/', EstadoList.as_view(), name="listar-estado"),

    # URLS de Cidade
    path('cadastrar/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade"),
    path('atualizar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="atualizar-cidade"),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name="excluir-cidade"),
    path('listar/cidade/', CidadeList.as_view(), name="listar-cidade"),

    # URLS de Pessoa
    path('cadastrar/pessoa/', PessoaCreate.as_view(), name="cadastrar-pessoa"),
    path('atualizar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name="atualizar-pessoa"),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name="excluir-pessoa"),
    path('listar/pessoa/', PessoaList.as_view(), name="listar-pessoa"),

    # URLS de Ferramenta
    path('cadastrar/ferramenta/', FerramentaCreate.as_view(), name="cadastrar-ferramenta"),
    path('atualizar/ferramenta/<int:pk>/', FerramentaUpdate.as_view(), name="atualizar-ferramenta"),
    path('excluir/ferramenta/<int:pk>/', FerramentaDelete.as_view(), name="excluir-ferramenta"),
    path('listar/ferramenta/', FerramentaList.as_view(), name="listar-ferramenta"),

    # URLS de Madeira
    path('cadastrar/madeira/', MadeiraCreate.as_view(), name="cadastrar-madeira"),
    path('atualizar/madeira/<int:pk>/', MadeiraUpdate.as_view(), name="atualizar-madeira"),
    path('excluir/madeira/<int:pk>/', MadeiraDelete.as_view(), name="excluir-madeira"),
    path('listar/madeira/', MadeiraList.as_view(), name="listar-madeira"),

    # URLS de Material
    path('cadastrar/material/', MaterialCreate.as_view(), name="cadastrar-material"),
    path('atualizar/material/<int:pk>/', MaterialUpdate.as_view(), name="atualizar-material"),
    path('excluir/material/<int:pk>/', MaterialDelete.as_view(), name="excluir-material"),
    path('listar/material/', MaterialList.as_view(), name="listar-material"),

    # URLS de Produto
    path('cadastrar/produto/', ProdutoCreate.as_view(), name="cadastrar-produto"),
    path('atualizar/produto/<int:pk>/', ProdutoUpdate.as_view(), name="atualizar-produto"),
    path('excluir/produto/<int:pk>/', ProdutoDelete.as_view(), name="excluir-produto"),
    path('listar/produto/', ProdutoList.as_view(), name="listar-produto"),
    
    ]
