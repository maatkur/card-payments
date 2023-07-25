from database.repository_config import RepositoryConfig


class CheckedOrdersRepository(RepositoryConfig):

    def __init__(self):
        self.table_name = "checkedOrders"
        super().__init__(self.table_name)

    def get_all_by(self, query):
        options = {
            "select": "orderNumber, cashierNumber, cashFlow, transactionType, flag, orderValue, installments, "
                      "purchaseDate, storeUnit, NSU, transactionAuthorization, uId",
            "distinct": True,
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

    def update_by_nsu_auth(self, data: dict):  # FUNCAO TEMPORARIA PARA O AJUSTE DOS UID´s
        nsu = data.get("NSU")
        auth = data.get("transactionAuthorization")
        order_number = data.get("orderNumber")
        if not nsu or not auth:
            raise ValueError("NSU and transactionAuthorization are required for updating data.")

        fields = ", ".join([f"{key} = ?" for key in data.keys()])
        values = tuple(data.values())
        command = f"UPDATE {self.table_name} SET {fields} WHERE NSU = ? AND transactionAuthorization = ? AND orderNumber = ?"
        values += (nsu, auth, order_number)

        self._execute_and_commit(command, values)

    def insert_debit_order(self, debit_order: dict) -> None:

        self.insert(debit_order)

    def inser_credit_order(self, credit_order: list) -> None:
        credit_orders = len(credit_order)

        for order in range(credit_orders):
            self.insert(credit_order[order])

    def get_cash_flow(self, date_period: dict) -> list:
        initial_date = date_period.get("initial_date")
        final_date = date_period.get("final_date")

        if not initial_date or not final_date:
            raise ValueError("initial_date and final_date are required for fetching cash flow.")

        query = f"SELECT installmentValue, payday FROM {self.table_name} WHERE payday BETWEEN '{initial_date}' AND '{final_date}'"

        return self._search_and_fetch_all(query)

    def get_unconciliated_order(self, query):
        options = {
            "select": "orderNumber, transactionType, flag, installments, installmentValue, currentInstallment, "
                      "purchaseDate, payday, flagTax, liquidValue, NSU, transactionAuthorization, "
                      "status, uId, conciliated",
            "query": query
        }

        payment = self.get_all(options)

        if payment:
            # Desempacotar os valores da tupla em variáveis
            (
                order_number,
                transaction_type,
                flag,
                installments,
                installment_value,
                current_installment,
                purchase_date,
                payday,
                flag_tax,
                liquid_value,
                nsu,
                transaction_authorization,
                status,
                uid,
                conciliated
            ) = payment[0]
            return {
                "orderNumber": order_number,
                "transactionType": transaction_type,
                "flag": flag,
                "installments": installments,
                "installmentValue": installment_value,
                "currentInstallment": current_installment,
                "purchaseDate": purchase_date,
                "payday": payday,
                "flagTax": flag_tax,
                "liquidValue": liquid_value,
                "NSU": nsu,
                "transactionAuthorization": transaction_authorization,
                "status": status,
                "uId": uid,
                "conciliated": conciliated
            }
        return payment

    def get_unconciliated_orders(self, date_period: dict) -> list:

        initial_date = date_period["initial_date"]
        final_date = date_period["final_date"]

        command = f"""SELECT orderNumber, transactionType, flag, installments, installmentValue, currentInstallment, 
                        purchaseDate, payday, flagTax, liquidValue, NSU, transactionAuthorization, status, uId 
                            FROM checkedOrders WHERE payday BETWEEN '{initial_date}' AND '{final_date}' 
                                AND conciliated = 0 ORDER BY orderNumber"""

        return self._search_and_fetch_all(command)

    def conciliate_orders(self, order: dict) -> None:

        payday = order.get("payday")
        current_installment = order.get("currentInstallment")
        status = order.get("status")
        uid = order.get("uId")

        command = f"""UPDATE checkedOrders
                        SET payday = '{payday}', conciliated = 1, status = '{status}'
                        WHERE uId = '{uid}' AND currentInstallment = '{current_installment}'
        """

        print(command)

        self._execute_and_commit(command)

    def get_conciliateds(self, date_period: dict) -> list:

        initial_date = date_period["initial_date"]
        final_date = date_period["final_date"]

        command = f"""SELECT orderNumber, transactionType, flag, installments, installmentValue, currentInstallment, 
                        purchaseDate, payday, flagTax, liquidValue, NSU, transactionAuthorization, status, uId 
                            FROM checkedOrders WHERE payday BETWEEN '{initial_date}' AND '{final_date}' 
                                AND conciliated = 1 ORDER BY orderNumber"""

        return self._search_and_fetch_all(command)

    def update_order_status(self, data: dict):

        uid = data.pop("uId", None)
        current_installment = data.pop("currentInstallment", None)
        if uid is None:
            raise ValueError("UID is required for updating data.")

        fields = ", ".join([f"{key} = ?" for key in data.keys()])
        values = tuple(data.values())
        command = f"UPDATE {self.table_name} SET {fields} WHERE uid = ? AND currentInstallment = ?"
        values += (uid, current_installment)

        self._execute_and_commit(command, values)

