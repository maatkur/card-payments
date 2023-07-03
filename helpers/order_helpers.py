from database.repositories.repository_manager import RepositoryManager
from helpers.paydays_helper import paydays


class OrderHelpers:

    @staticmethod
    def create_debit_order(order: dict) -> dict:
        flag_tax = RepositoryManager().card_flags_repository().get_flag_tax(order["flag"], 0)
        order_value = float(order["orderValue"])
        liquid_value = round((order_value - ((order_value * flag_tax) / 100)), 2)
        installment_value = liquid_value

        return {
            "orderNumber": order["orderNumber"],
            "cashierNumber": order["cashierNumber"],
            "cashFlow": order["cashFlow"],
            "transactionType": "debit",
            "flag": order["flag"],
            "purchaseDate": order["purchaseDate"],
            "orderValue": order["orderValue"],
            "storeUnit": order["storeUnit"],
            "NSU": order["nsu"],
            "transactionAuthorization": order["transactionAuthorization"],
            "installments": 0,
            "currentInstallment": 0,
            "flagTax": flag_tax,
            "payday": paydays(order["purchaseDate"], 1, "debit")[0],
            "liquidValue": liquid_value,
            "installmentValue": installment_value,
            "uId": order["uId"]
        }

    @staticmethod
    def create_credit_order(order: dict) -> list:
        flag_tax = RepositoryManager().card_flags_repository().get_flag_tax(order["flag"], order["installments"])
        order_value = float(order["orderValue"])
        installments = int(order["installments"])
        liquid_value = round((order_value - ((order_value * flag_tax) / 100)), 2)
        installment_value = round(liquid_value / installments, 2)

        checked_order = []

        for installment in range(installments):
            credit_order = {
                "orderNumber": order["orderNumber"],
                "cashierNumber": order["cashierNumber"],
                "cashFlow": order["cashFlow"],
                "transactionType": 'credit',
                "flag": order["flag"],
                "purchaseDate": order["purchaseDate"],
                "orderValue": order_value,
                "storeUnit": order["storeUnit"],
                "NSU": order["nsu"],
                "transactionAuthorization": order["transactionAuthorization"],
                "installments": order["installments"],
                "currentInstallment": f"{installment + 1}/{installments}",
                "flagTax": flag_tax,
                "payday": paydays(order["purchaseDate"], order["installments"], "credit")[installment],
                "liquidValue": liquid_value,
                "installmentValue": installment_value,
                "uId": order["uId"]
            }

            checked_order.append(credit_order)

        return checked_order

    @staticmethod
    def create_checked_order(order: dict) -> list or dict:

        if order["transactionType"] == "Débito":
            checked_order = OrderHelpers.create_debit_order(order)
            return checked_order

        elif order["transactionType"] == "Crédito":
            checked_order = OrderHelpers.create_credit_order(order)
            return checked_order
