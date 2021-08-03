from django.db import models
from api.models.store_model import Store


class Transaction(models.Model):
    tipo = models.IntegerField()
    data = models.CharField(max_length=255)
    valor = models.FloatField()
    cpf = models.CharField(max_length=255)
    cartao = models.CharField(max_length=255)
    hora = models.CharField(max_length=255)
    loja = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="transacoes")
