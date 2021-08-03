from rest_framework import serializers


class TransactionSerializer(serializers.Serializer):
    tipo = serializers.IntegerField()
    data = serializers.CharField()
    valor = serializers.FloatField()
    cpf = serializers.CharField()
    cartao = serializers.CharField()
    hora = serializers.CharField()
