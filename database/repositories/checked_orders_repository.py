from database.repository_config import RepositoryConfig


class CheckedOrdersRepository(RepositoryConfig):

    def __init__(self):
        self.table_name = "checkedOrders"
        super().__init__(self.table_name)

    def get_all_by(self, query):
        options = {
            "select": "orderNumber, cashierNumber, cashFlow, transactionType, flag, orderValue, currentInstallment, "
                      "purchaseDate, storeUnit, NSU, transactionAuthorization, uId",
            "query": query}

        return self.get_all(options)

    def get_first(self, query):
        options = {
            "select": "top 1 orderNumber, cashierNumber, cashFlow, transactionType, flag, orderValue, "
                      "currentInstallment, purchaseDate, storeUnit, NSU, transactionAuthorization, uId, installments",
            "query": query
        }

        checked_order = self.get_all(options)

        if checked_order:
            # Desempacotar os valores da tupla em variáveis
            (
                order_number,
                cashier_number,
                cash_flow,
                transaction_type,
                flag,
                order_value,
                current_installment,
                purchase_date,
                store_unit,
                nsu,
                transaction_authorization,
                uid,
                installments,
            ) = checked_order[0]
            return {
                "orderNumber": order_number,
                "cashierNumber": cashier_number,
                "cashFlow": cash_flow,
                "transactionType": transaction_type,
                "flag": flag,
                "orderValue": order_value,
                "currentInstallment": current_installment,
                "purchaseDate": purchase_date,
                "storeUnit": store_unit,
                "NSU": nsu,
                "transactionAuthorization": transaction_authorization,
                "uId": uid,
                "installments": installments
            }
        return checked_order

    def update(self, data: dict):
        uid = data.pop("uId", None)
        if uid is None:
            raise ValueError("UID is required for updating data.")

        fields = ", ".join([f"{key} = ?" for key in data.keys()])
        values = tuple(data.values())
        command = f"UPDATE {self.table_name} SET {fields} WHERE uid = ?"
        values += (uid,)

        self._execute_and_commit(command, values)

    def insert_debit_order(self, debit_order: dict) -> None:

        self.insert(debit_order)

    def inser_credit_order(self, credit_order: list) -> None:
        credit_orders = len(credit_order)

        for order in range(credit_orders):
            self.insert(credit_order[order])

