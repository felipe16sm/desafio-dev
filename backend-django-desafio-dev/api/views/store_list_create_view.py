from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Store, Transaction
from api.serializers.store_serializer import StoreSerializer
from api.serializers.transaction_serializer import TransactionSerializer


class StoreListCreateView(APIView):
    def get(self, request):
        store_list = Store.objects.all()

        return Response(
            [StoreSerializer(store).data for store in store_list],
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        store = Store.objects.filter(nome_loja=request.data["nome_loja"]).first()

        if store:
            return Response(
                {"erro": "Essa loja já existe"}, status=status.HTTP_409_CONFLICT
            )

        serializer = StoreSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        store = Store.objects.create(
            nome_loja=request.data["nome_loja"],
            dono_loja=request.data["dono_loja"],
        )

        list_store_transactions = []

        for transaction in request.data["transacoes"]:
            serializer = TransactionSerializer(data=transaction)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            Transaction.objects.create(
                tipo=transaction["tipo"],
                data=transaction["data"],
                valor=transaction["valor"],
                cpf=transaction["cpf"],
                cartao=transaction["cartao"],
                hora=transaction["hora"],
                loja=store,
            )
            list_store_transactions.append(transaction)

        return Response(
            {
                "id": store.id,
                "nome_loja": store.nome_loja,
                "dono_loja": store.dono_loja,
                "transacoes": list_store_transactions,
            },
            status=status.HTTP_201_CREATED,
        )
