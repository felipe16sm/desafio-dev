from django.test import TestCase
from rest_framework.test import APIClient


class TestStoreRetrieveCreateTransactionView(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.transaction_to_create = {
            "transacoes": [
                {
                    "tipo": 3,
                    "data": "20190301",
                    "valor": 142.0,
                    "cpf": "09620676017",
                    "cartao": "4753****3153",
                    "hora": "153453",
                },
                {
                    "tipo": 2,
                    "data": "20190301",
                    "valor": 112.0,
                    "cpf": "09620676017",
                    "cartao": "3648****0099",
                    "hora": "234234",
                },
                {
                    "tipo": 1,
                    "data": "20190301",
                    "valor": 152.0,
                    "cpf": "09620676017",
                    "cartao": "1234****7890",
                    "hora": "233000",
                },
            ]
        }

        self.transaction_to_create_with_missing_field = {
            "transacoes": [
                {
                    "data": "20190301",
                    "valor": 142.0,
                    "cpf": "09620676017",
                    "cartao": "4753****3153",
                    "hora": "153453",
                },
                {
                    "tipo": 2,
                    "data": "20190301",
                    "valor": 112.0,
                    "cpf": "09620676017",
                    "cartao": "3648****0099",
                    "hora": "234234",
                },
                {
                    "tipo": 1,
                    "data": "20190301",
                    "valor": 152.0,
                    "cpf": "09620676017",
                    "cartao": "1234****7890",
                    "hora": "233000",
                },
            ]
        }

        self.store_to_create_without_transaction = {
            "nome_loja": "BAR DO JOÃO",
            "dono_loja": "JOÃO MACEDO",
            "transacoes": [],
        }

    def test_create_transaction_of_nonexisting_store(self):
        response = self.client.post(
            "/api/stores/1/transactions/", self.transaction_to_create, format="json"
        )

        self.assertEqual(response.status_code, 404)

    def test_create_transaction_of_a_store(self):
        self.client.post(
            "/api/stores/", self.store_to_create_without_transaction, format="json"
        )

        response = self.client.post(
            "/api/stores/1/transactions/", self.transaction_to_create, format="json"
        )

        expected_response = {
            "id": 1,
            "nome_loja": "BAR DO JOÃO",
            "dono_loja": "JOÃO MACEDO",
            "transacoes": [
                {
                    "tipo": 3,
                    "data": "20190301",
                    "valor": 142.0,
                    "cpf": "09620676017",
                    "cartao": "4753****3153",
                    "hora": "153453",
                },
                {
                    "tipo": 2,
                    "data": "20190301",
                    "valor": 112.0,
                    "cpf": "09620676017",
                    "cartao": "3648****0099",
                    "hora": "234234",
                },
                {
                    "tipo": 1,
                    "data": "20190301",
                    "valor": 152.0,
                    "cpf": "09620676017",
                    "cartao": "1234****7890",
                    "hora": "233000",
                },
            ],
        }

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), expected_response)

    def test_get_transaction_of_a_store(self):
        self.client.post(
            "/api/stores/", self.store_to_create_without_transaction, format="json"
        )

        self.client.post(
            "/api/stores/1/transactions/", self.transaction_to_create, format="json"
        )

        response = self.client.get("/api/stores/1/transactions/", format="json")

        expected_response = {
            "id": 1,
            "nome_loja": "BAR DO JOÃO",
            "dono_loja": "JOÃO MACEDO",
            "transacoes": [
                {
                    "tipo": 3,
                    "data": "20190301",
                    "valor": 142.0,
                    "cpf": "09620676017",
                    "cartao": "4753****3153",
                    "hora": "153453",
                },
                {
                    "tipo": 2,
                    "data": "20190301",
                    "valor": 112.0,
                    "cpf": "09620676017",
                    "cartao": "3648****0099",
                    "hora": "234234",
                },
                {
                    "tipo": 1,
                    "data": "20190301",
                    "valor": 152.0,
                    "cpf": "09620676017",
                    "cartao": "1234****7890",
                    "hora": "233000",
                },
            ],
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    def test_get_transaction_of_nonexisting_store(self):

        response = self.client.get("/api/stores/1/transactions/", format="json")

        self.assertEqual(response.status_code, 404)
