from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Store, Transaction
from api.serializers.store_serializer import StoreSerializer
from api.services.transaction_service import TransactionService
import ipdb


class StoreBulkTransactionView(APIView):
    def post(self, request):

        raw_transactions_data = request.FILES["file"].read().decode("utf-8")
        transaction_list = TransactionService.organize_transaction(
            raw_transactions_data
        )

        list_store_transactions = []

        for transaction in transaction_list:
            store = Store.objects.filter(nome_loja=transaction["nome_loja"]).first()

            if not store:
                store = Store.objects.create(
                    nome_loja=transaction["nome_loja"],
                    dono_loja=transaction["dono_loja"],
                )
            Transaction.objects.create(
                tipo=transaction["tipo"],
                data=transaction["data"],
                valor=transaction["valor"],
                cpf=transaction["cpf"],
                cartao=transaction["cartao"],
                hora=transaction["hora"],
                loja=store,
            )
            list_store_transactions.append(store)

        return Response(
            [StoreSerializer(loja).data for loja in list_store_transactions],
            status=status.HTTP_201_CREATED,
        )
