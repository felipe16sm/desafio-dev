from rest_framework import serializers
from api.serializers.transaction_serializer import TransactionSerializer


class StoreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome_loja = serializers.CharField()
    dono_loja = serializers.CharField()
    transacoes = TransactionSerializer(many=True)
