from django.db import models

# Create your models here.

class Estado(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome: ", help_text="Digite o nome do seu estado")
    sigla = models.CharField(max_length=2, unique=True, verbose_name="Sigla: ")    
    def __str__(self):
        return self.sigla + " - " + self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome: ", help_text="Digite o nome da sua cidade")
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + " - " + self.estado.sigla

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome: ", help_text="Digite seu nome completo")
    nascimento = models.DateField(verbose_name='Data de Nascimento: ')
    email = models.CharField(max_length=100, verbose_name="Email: ", help_text="Digite seu e-mail")

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + ' - ' + str(self.nascimento)

class Ferramenta(models.Model):
    nome = models.CharField(max_length=30, verbose_name="Nome: ", help_text="Digite o nome da ferramenta")
    descricao = models.CharField(max_length=100, verbose_name="Descrição: ")

    def __str__(self):
        return self.nome + " - " + self.descricao

class Madeira(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome: ", help_text="Digite o nome da madeira")
    cor = models.CharField(max_length=40, verbose_name="Cor: ", help_text="Digite a cor da madeira")
    descricao = models.CharField(max_length=100, verbose_name="Descrição: ")

class Material(models.Model):
    nome = models.CharField(max_length=30, verbose_name="Nome: ", help_text="Informe o nome do material")
    descricao = models.CharField(max_length=50, verbose_name="Descrição: ")

    def __str__(self):
        return self.nome + " - " + self.descricao

class Produto(models.Model):
    nome = models.CharField(max_length=30, verbose_name="Nome: ", help_text="Informe o nome do produto")
    tipo = models.CharField(max_length=30, verbose_name="Tipo: ", help_text="Informe o tipo do produto")
    descricao = models.CharField(max_length=50, verbose_name="Descrição: ")

    def __str__(self):
        return self.nome + " - " + self.tipo + " - " + self.descricao