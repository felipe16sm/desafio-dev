from django.test import TestCase
from rest_framework.test import APIClient


class TestStoreListCreateView(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.store_to_create = {
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

        self.store_to_create_without_transaction = {
            "nome_loja": "BAR DO JOÃO",
            "dono_loja": "JOÃO MACEDO",
            "transacoes": [],
        }

        self.store_to_create_with_missing_field = {
            "nome_loja": "BAR DO JOÃO",
            "transacoes": [],
        }

    def test_create_store_with_transactions(self):
        response = self.client.post("/api/stores", self.store_to_create, format="json")
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

    def test_create_store_without_transactions(self):
        response = self.client.post(
            "/api/stores", self.store_to_create_without_transaction, format="json"
        )
        expected_response = {
            "id": 1,
            "nome_loja": "BAR DO JOÃO",
            "dono_loja": "JOÃO MACEDO",
            "transacoes": [],
        }

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), expected_response)

    def test_create_store_with_missing_field(self):
        response = self.client.post(
            "/api/stores", self.store_to_create_with_missing_field, format="json"
        )

        self.assertEqual(response.status_code, 400)

    def test_create_store_with_same_name_of_other_store(self):
        self.client.post("/api/stores", self.store_to_create, format="json")

        response = self.client.post("/api/stores", self.store_to_create, format="json")

        self.assertEqual(response.status_code, 409)

    def test_get_stores_empty(self):
        response = self.client.get("/api/stores", format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)

    def test_get_stores_with_registered_store(self):
        self.client.post("/api/stores", self.store_to_create, format="json")

        response = self.client.get("/api/stores", format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
