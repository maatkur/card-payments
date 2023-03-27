import pyodbc


class DatabaseHandler:
    def __init__(self):
        self.server = 'OFSERVER'
        self.database = 'card_payments'
        self.user = 'sa'
        self.password = '$ervid0r'
        self.connection = None

    def connect(self) -> None:
        """Cria uma conexão com o banco de dados."""
        try:
            self.connection = pyodbc.connect(
                fr'DRIVER={{SQL Server}};Server={self.server}\SQLEXPRESS;Database={self.database};User Id={self.user};Password={self.password};MultipleActiveResultSets=true;')
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def _execute_and_commit(self, command) -> None:
        """Executa uma consulta que altera dados no banco de dados e realiza um commit."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(command)
            self.connection.commit()
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()
            raise

    def _search_and_fetch(self, command) -> list:

        command = command
        cursor = self.connection.cursor()
        cursor.execute(command)
        result = cursor.fetchall()

        return result

    def insert_in_order_stage(self, order_number: str, cashier_number: str, cash_flow: str, order_value: float,
                              store_id: int) -> None:

        #  Insere uma ordem no banco de dados de stage

        command = f"""
            IF NOT EXISTS (
                SELECT orderNumber 
                FROM orderStage 
                WHERE orderNumber = '{order_number}'
                )
                BEGIN
                    INSERT INTO orderStage (
                    orderNumber, 
                    cashierNumber, 
                    cashFlow, 
                    orderValue, 
                    storeUnit, 
                    isCommit
                    )
                    VALUES (
                    '{order_number}', 
                    '{cashier_number}', 
                    '{cash_flow}',  
                    {order_value}, 
                    (SELECT storeUnit FROM Stores WHERE ID = {store_id}), 
                    0
                    )
                END
            ELSE
                BEGIN
                    UPDATE orderStage
            
                    set cashierNumber = '{cashier_number}', cashFlow = '{cash_flow}', orderValue = {order_value}, isCommit = 0		
            
                    where orderNumber = '{order_number}' 
                END
                 """
        self._execute_and_commit(command)

    def delete_staged_order(self, order):
        command = f"""
                    DELETE FROM orderStage
                    
                    WHERE orderNumber = '{order}'
                """
        self._execute_and_commit(command)

    def verify_checked_orders(self, order_number: str) -> None:
        """Deleta uma ordem do banco de dados."""
        command = f"""
            IF EXISTS (
                SELECT orderNumber 
                FROM checkedOrders 
                WHERE orderNumber = '{order_number}'
            )
            BEGIN
                DELETE FROM checkedOrders WHERE orderNumber = '{order_number}'
            END
        """
        self._execute_and_commit(command)

    def get_orders_by_store(self, store_id) -> list:
        """Seleciona os pedidos com cartão por loja"""

        command = f"""
                    SELECT orderNumber, orderValue, dateUpdate
                    FROM orderStage
                    JOIN stores
                    ON orderStage.storeUnit = stores.storeUnit
                    WHERE stores.id = {store_id} and isCommit = 0;
                    """
        result = self._search_and_fetch(command)

        return result

    def get_order(self, order_number) -> list:
        command = f"""
        select * from orderStage where orderNumber = '{order_number}'
        """
        result = self._search_and_fetch(command)

        return result

    def insert_checked_order(self, flag, installments, order_number, current_installment, payday, NSU,
                             transaction_authorization, transaction_type) -> None:

        command = f"""
            INSERT INTO checkedOrders (orderNumber, cashierNumber, cashFLow, transactionType, flag, installments, installmentValue, currentInstallment, payday, orderValue, flagTax, liquidValue, storeUnit, NSU, [transactionAuthorization])
                SELECT
                    '{order_number}',
                    os.cashierNumber,
                    os.cashFlow,
                    '{transaction_type}',
                    '{flag}',
                    '{installments}',
                    os.orderValue / {'1' if installments == 0 else installments},
                    '{current_installment}',
                    '{payday}',
                    os.orderValue,
                    (SELECT cf.tax FROM cardFlags2 cf WHERE cf.flag = '{flag}' AND cf.installments = '{installments}'),
                    os.orderValue - (os.orderValue * ((SELECT cf.tax FROM cardFlags2 cf WHERE cf.flag = '{flag}' AND cf.installments = '{installments}') / 100)),
                    os.storeUnit,
                    '{NSU}',
                    '{transaction_authorization}'
                FROM orderStage as os
                WHERE os.orderNumber = '{order_number}';"""

        self._execute_and_commit(command)

    def get_payments_by_date(self, initial_date, final_date):
        command = f"SELECT installmentValue, payday FROM checkedOrders WHERE payday BETWEEN '{initial_date}' AND '{final_date}'"

        result = self._search_and_fetch(command)

        return result

    def get_card_flags(self) -> list:
        command = f"""
        select flag from cardFlags
        """

        result = self._search_and_fetch(command)

        return result

    def update_stage(self, order_number) -> None:
        command = f"""
                    UPDATE orderStage
                    
                    SET isCommit = 1
                    
                    WHERE orderNumber = {order_number}    
                """

        self._execute_and_commit(command)

    def disconnect(self) -> None:
        """Desconecta do banco de dados."""
        self.connection.close()
