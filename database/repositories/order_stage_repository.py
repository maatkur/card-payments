from database.repository_config import RepositoryConfig


class OrderStageRepository(RepositoryConfig):

    def __init__(self):
        self.table_name = "orderStage"
        super().__init__(self.table_name)

    def get_uncommited_orders(self, store_id, cashier_number=None):
        command = f"""SELECT orderNumber, orderValue, dateUpdate
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
        command = f"""SELECT orderNumber, orderValue, dateUpdate
                      FROM orderStage AS o
                      JOIN stores AS s
                      ON o.storeUnit = s.storeUnit
                      WHERE s.id = ? AND o.orderNumber = ? AND o.isCommit = 0"""
        values = [store_id, order_number]

        if cashier_number is not None:
            command += " AND o.cashierNumber = ?"
            values.append(cashier_number)

        return self._search_and_fetch_all(command, tuple(values))

    def commit_order(self, order_number: str) -> None:

        command = f"""
                    UPDATE orderStage 

                    SET isCommit = 1

                    WHERE orderNumber = '{order_number}'
                """

        self._execute_and_commit(command)
