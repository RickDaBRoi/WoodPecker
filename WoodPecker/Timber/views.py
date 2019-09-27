from django.shortcuts import render

# Importa todas as classes do models.py
from .models import *

# Importa função que vai chamar as urls pelo "name" delas
from django.urls import reverse_lazy

# Importar as classes Views para inserir, alterar e excluir utilizando formulários
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Importa o TemplateView para criação de páginas simples
from django.views.generic import TemplateView

# Importa ListView para gerar as telas com tabelas
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# Cria uma classe com herança de TemplateView para exibir
# um arquivo HTML normal (com o conteúdo dele)

class PaginaInicialView(TemplateView):
    # Nome do arquivo que vai ser utilizado para renderizar
    # esta página/método/classe
    template_name = "index.html"

# Página "Sobre"

class SobreView(TemplateView):
    template_name = "sobre.html"

# ============================== INSERIR ===================================

class EstadoCreate(LoginRequiredMixin, CreateView):

    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(EstadoCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novos Estados"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context


class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novas Cidades"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context


class PessoaCreate(LoginRequiredMixin, CreateView):
    model = Pessoa
    fields = ['nome', 'nascimento', 'email']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(PessoaCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novos Usuários"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context


class FerramentaCreate(LoginRequiredMixin, CreateView):
    model = Ferramenta
    fields = ['nome', 'descricao']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(FerramentaCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novas Ferramentas"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context


class MadeiraCreate(LoginRequiredMixin, CreateView):
    model = Madeira
    fields = ['nome', 'cor', 'descricao']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(MadeiraCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novos tipos de Madeiras"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context

class MaterialCreate(LoginRequiredMixin, CreateView):
    model = Material
    fields = ['nome', 'descricao']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(MaterialCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novos Materiais"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context

class ProdutoCreate(LoginRequiredMixin, CreateView):
    model = Produto
    fields = ['nome', 'tipo', 'descricao']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novos Produtos"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context
# ============================== EDITAR ===================================


class EstadoUpdate(LoginRequiredMixin, UpdateView):
    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')


class CidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')


class PessoaUpdate(LoginRequiredMixin, UpdateView):
    model = Pessoa
    fields = ['nome', 'nascimento', 'email']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')


class FerramentaUpdate(LoginRequiredMixin, UpdateView):
    model = Ferramenta
    fields = ['nome', 'descricao']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')


class MadeiraUpdate(LoginRequiredMixin, UpdateView):
    model = Madeira
    fields = ['nome', 'cor', 'descricao']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

class MaterialUpdate(LoginRequiredMixin, UpdateView):
    model = Material
    fields = ['nome', 'descricao']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ['nome', 'tipo', 'descricao']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

    # ============================== EXCLUIR ===================================


class EstadoDelete(LoginRequiredMixin, DeleteView):
    model = Estado
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')


class CidadeDelete(LoginRequiredMixin, DeleteView):
    model = Cidade
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')


class PessoaDelete(LoginRequiredMixin, DeleteView):
    model = Pessoa
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')


class FerramentaDelete(LoginRequiredMixin, DeleteView):
    model = Ferramenta
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')


class MadeiraDelete(LoginRequiredMixin, DeleteView):
    model = Madeira
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

class MaterialDelete(LoginRequiredMixin, DeleteView):
    model = Material
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

class ProdutoDelete(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

    # ============================== LISTAR ===================================
    # Vai gerar uma tela com uma lista de estados


class EstadoList(LoginRequiredMixin, ListView):
    model = Estado  # Informa qual o modelo ...
    template_name = 'listas/list_estado.html'  # e o template


class CidadeList(LoginRequiredMixin, ListView):
    model = Cidade
    template_name = 'listas/list_cidade.html'


class PessoaList(LoginRequiredMixin, ListView):
    model = Pessoa
    template_name = 'listas/list_pessoa.html'


class FerramentaList(LoginRequiredMixin, ListView):
    model = Ferramenta
    template_name = 'listas/list_ferramenta.html'


class MadeiraList(LoginRequiredMixin, ListView):
    model = Madeira
    template_name = 'listas/list_madeira.html'

class MaterialList(LoginRequiredMixin, ListView):
    model = Material
    template_name = 'listas/list_material.html'

class ProdutoList(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'listas/list_produto.html'