from database.repository_config import RepositoryConfig


class OldPaymentsRepository(RepositoryConfig):

    def __init__(self):
        self.table_name = "oldPayments"
        super().__init__(self.table_name)

    def get_cash_flow(self, date_period: dict) -> list:
        initial_date = date_period.get("initial_date")
        final_date = date_period.get("final_date")

        if not initial_date or not final_date:
            raise ValueError("initial_date and final_date are required for fetching cash flow.")

        query = f"SELECT installmentValue, payday FROM {self.table_name} WHERE payday BETWEEN '{initial_date}' AND '{final_date}'"

        return self._search_and_fetch_all(query)

    def get_conciliations(self, query):
        options = {
            "select": "payday, tax, installmentValue, currentInstallment, "
                      "installments, NSU, transactionAuthorization, uId, conciliated",
            "query": query
        }

        payment = self.get_all(options)

        if payment:
            # Desempacotar os valores da tupla em variáveis
            (
                payday,
                tax,
                installment_value,
                current_installment,
                installments,
                nsu,
                transaction_authorization,
                uid,
                conciliated
            ) = payment[0]
            return {
                "payday": payday,
                "tax": tax,
                "installmentValue": installment_value,
                "currentInstallment": current_installment,
                "installments": installments,
                "NSU": nsu,
                "transactionAuthorization": transaction_authorization,
                "uId": uid,
                "conciliated": conciliated
            }
        return payment

    def get_unconciliated_orders(self, date_period: dict) -> list:

        initial_date = date_period["initial_date"]
        final_date = date_period["final_date"]

        command = f"""SELECT payday, tax, installmentValue, currentInstallment, installments, 
                        NSU, transactionAuthorization, uId 
                             FROM oldPayments WHERE payday BETWEEN '{initial_date}' AND '{final_date}' 
                                AND conciliated = 0"""

        return self._search_and_fetch_all(command)

    def update_by_nsu_auth(self, data: dict):  # FUNCAO TEMPORARIA PARA O AJUSTE DOS UID´s
        nsu = data.get("NSU")
        auth = data.get("transactionAuthorization")
        if not nsu or not auth:
            raise ValueError("NSU and transactionAuthorization are required for updating data.")

        fields = ", ".join([f"{key} = ?" for key in data.keys()])
        values = tuple(data.values())
        command = f"UPDATE {self.table_name} SET {fields} WHERE NSU = ? AND transactionAuthorization = ?"
        values += (nsu, auth)

        self._execute_and_commit(command, values)

    def conciliate_orders(self, order: dict) -> None:

        payday = order.get("payday")
        current_installment = order.get("currentInstallment")
        uid = order.get("uId")

        command = f"""UPDATE oldPayments
                        SET payday = '{payday}', conciliated = 1
                        WHERE uId = '{uid}' AND currentInstallment = '{current_installment}'
        """

        self._execute_and_commit(command)
