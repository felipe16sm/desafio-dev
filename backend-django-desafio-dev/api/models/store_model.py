from django.db import models


class Store(models.Model):
    nome_loja = models.CharField(max_length=255)
    dono_loja = models.CharField(max_length=255)
