class TransactionService:
    @staticmethod
    def organize_transaction(raw_transactions_data):
        transaction_list = raw_transactions_data.split("\n")
        transaction_list.pop()

        new_transaction_list = []

        for transaction_dados in transaction_list:
            transaction_dict = {}
            transaction_dict["tipo"] = int(transaction_dados[0])
            transaction_dict["data"] = transaction_dados[1:9]
            transaction_dict["valor"] = float(transaction_dados[9:19]) / 100
            transaction_dict["cpf"] = transaction_dados[19:30]
            transaction_dict["cartao"] = transaction_dados[30:42]
            transaction_dict["hora"] = transaction_dados[42:48]
            transaction_dict["dono_loja"] = transaction_dados[48:62].strip()
            transaction_dict["nome_loja"] = transaction_dados[62:].strip()
            new_transaction_list.append(transaction_dict)

        return new_transaction_list
