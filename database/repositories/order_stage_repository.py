from database.repository_config import RepositoryConfig


class OrderStageRepository(RepositoryConfig):

    def __init__(self):
        self.table_name = "orderStage"
        super().__init__(self.table_name)

    def get_uncommited_orders(self, store_id, cashier_number=None):
        command = f"""SELECT orderNumber, orderValue, dateUpdate, uId
                      FROM orderStage AS o
                      JOIN stores AS s
                      ON o.storeUnit = s.storeUnit
                      WHERE s.id = ? AND o.isCommit = 0"""
        values = [store_id]

        if cashier_number is not None:
            command += " AND o.cashierNumber = ?"
            values.append(cashier_number)

        return self._search_and_fetch_all(command, tuple(values))

    def filter_uncommited_order(self, store_id, order_number, cashier_number=None):
        command = f"""SELECT orderNumber, orderValue, dateUpdate, uId
                      FROM orderStage AS o
                      JOIN stores AS s
                      ON o.storeUnit = s.storeUnit
                      WHERE s.id = ? AND o.orderNumber = ? AND o.isCommit = 0"""
        values = [store_id, order_number]

        if cashier_number is not None:
            command += " AND o.cashierNumber = ?"
            values.append(cashier_number)

        return self._search_and_fetch_all(command, tuple(values))

    def update_order_value(self, value: float, uid: str) -> None:

        command = f"""
                    UPDATE orderStage 

                    SET orderValue = {value}

                    WHERE uid = '{uid}'
                """

        self._execute_and_commit(command)

    def commit_order(self, uid: str) -> None:

        command = f"""
                    UPDATE orderStage 

                    SET isCommit = 1

                    WHERE uId = '{uid}'
                """

        self._execute_and_commit(command)

    def uncommit_order(self, uid: str) -> None:

        command = f"""
                    UPDATE orderStage 

                    SET isCommit = 0

                    WHERE uId = '{uid}'
                """

        self._execute_and_commit(command)

    def get_order_to_check(self, uid) -> dict:

        options = {
            "distinct": True,
            "query": {
                "uid": uid,
                "isCommit": 0
            }
        }

        order_data = self.get_all(options)

        if order_data:
            # Desempacotar os valores da tupla em variáveis
            (
                _,  # Descartar o primeiro elemento (não utilizado)
                order_number,
                cashier_number,
                cash_flow,
                order_value,
                store_unit,
                purchase_date,
                _,  # Descartar o elemento (não utilizado)
                uid,
            ) = order_data[0]

            # Retornar os valores em um dicionário
            return {
                "orderNumber": order_number,
                "cashierNumber": cashier_number,
                "cashFlow": cash_flow,
                "orderValue": order_value,
                "storeUnit": store_unit,
                "purchaseDate": purchase_date,
                "uId": uid
            }
