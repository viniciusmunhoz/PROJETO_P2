from django.contrib import admin
from .models import Vendas, Cliente, Funcionario, Calcado


# Register your models here.
admin.site.register(Vendas)
admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Calcado)
