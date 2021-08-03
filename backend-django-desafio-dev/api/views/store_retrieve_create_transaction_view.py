from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Store, Transaction
from api.serializers.store_serializer import StoreSerializer
from api.serializers.transaction_serializer import TransactionSerializer


class StoreRetrieveCreateTransactionView(APIView):
    def get(self, request, pk):
        store = Store.objects.filter(id=pk).first()

        if not store:
            return Response(
                {"erro": "Não há loja com essa id"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = StoreSerializer(store)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        store = Store.objects.filter(id=pk).first()

        if not store:
            return Response(
                {"erro": "Não há loja com essa id"}, status=status.HTTP_404_NOT_FOUND
            )

        list_store_transactions = []

        for transaction in request.data["transacoes"]:
            serializer = TransactionSerializer(data=transaction)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        for transaction in request.data["transacoes"]:
            Transaction.objects.create(
                tipo=transaction["tipo"],
                data=transaction["data"],
                valor=transaction["valor"],
                cpf=transaction["cpf"],
                cartao=transaction["cartao"],
                hora=transaction["hora"],
                loja=store,
            )

        for store_transaction in store.transacoes.all():
            store_transaction_dict = {}
            store_transaction_dict["tipo"] = store_transaction.tipo
            store_transaction_dict["data"] = store_transaction.data
            store_transaction_dict["valor"] = store_transaction.valor
            store_transaction_dict["cpf"] = store_transaction.cpf
            store_transaction_dict["cartao"] = store_transaction.cartao
            store_transaction_dict["hora"] = store_transaction.hora
            list_store_transactions.append(store_transaction_dict)

        return Response(
            {
                "id": store.id,
                "nome_loja": store.nome_loja,
                "dono_loja": store.dono_loja,
                "transacoes": list_store_transactions,
            },
            status=status.HTTP_201_CREATED,
        )
