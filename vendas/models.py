from django.db import models

class Calcado(models.Model):
    modelo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)

    def __str__(self):
        return self.modelo

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    salario = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Vendas(models.Model):
    calcado = models.ForeignKey(Calcado, on_delete=models.SET_NULL, null=True)
    quantidade = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    datavenda = models.CharField(max_length=50)
    loja = models.CharField(max_length=50)

    def __str__(self):
        return self.calcado.__str__()
