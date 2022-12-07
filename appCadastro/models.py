from django.db import models
from datetime import date

# Create your models here.

class Produto(models.Model):
    tipo_produto = models.CharField(max_length = 100)
    marca_produto = models.CharField(max_length = 30)
    descricao_produto = models.TextField(blank = True, null = True)
    data_cadastro = models.DateField(default = date.today)
    preco_compra = models.FloatField()
    preco_venda = models.FloatField()

    def __str__(self):
        return self.tipo_produto