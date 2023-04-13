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
                 """
        self._execute_and_commit(command)

    def manually_insert_in_order_stage(self, order_number: str, cashier_number: str, cash_flow: str, order_value: float,
                                       store_id: int, order_date: str) -> None:

        #  Insere uma ordem no banco de dados de stage

        command = f"""
                    INSERT INTO orderStage (
                    orderNumber, 
                    cashierNumber, 
                    cashFlow, 
                    orderValue, 
                    storeUnit,
                    dateUpdate, 
                    isCommit
                    )
                    VALUES (
                    '{order_number}', 
                    '{cashier_number}', 
                    '{cash_flow}',  
                    {order_value}, 
                    (SELECT storeUnit FROM Stores WHERE ID = {store_id}),
                    '{order_date}', 
                    0
                    )
                 """

        self._execute_and_commit(command)

    def delete_staged_order(self, order) -> None:
        command = f"""
                    DELETE FROM orderStage

                    WHERE orderNumber = '{order}'
                """
        self._execute_and_commit(command)

    def verify_and_delete_checked_orders(self, order_number: str) -> None:
        """Deleta um pedido checado do banco de dados."""
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

    def get_orders_by_store_and_cashier(self, store_id, cashier_number) -> list:
        """Seleciona os pedidos com cartão por loja e caixa para visualização de user comum """

        command = f"""
                    SELECT orderNumber, orderValue, dateUpdate
                    FROM orderStage
                    JOIN stores
                    ON orderStage.storeUnit = stores.storeUnit
                    WHERE stores.id = {store_id} AND isCommit = 0 AND cashierNumber = {cashier_number};
                    """
        result = self._search_and_fetch(command)

        return result

    def get_specific_order_by_store(self, store, order_number):
        command = f"""
                    SELECT orderNumber, orderValue, dateUpdate
                            FROM orderStage
                            JOIN stores
                            ON orderStage.storeUnit = stores.storeUnit
                            WHERE stores.id = {store} AND isCommit = 0 AND orderNumber = {order_number};
                    """
        result = self._search_and_fetch(command)

        return result

    def get_all_orders_by_store(self, store_id):
        # Seleciona os pedidos por loja - Usado no Cards para visão dos gerentes
        command = f"""
                            SELECT orderNumber, orderValue, dateUpdate
                            FROM orderStage
                            JOIN stores
                            ON orderStage.storeUnit = stores.storeUnit
                            WHERE stores.id = {store_id} AND isCommit = 0;
                            """
        result = self._search_and_fetch(command)

        return result

    def get_order_by_cashier_filter(self, cashier_number, order_number) -> list:
        """Seleção das caixas por pedido para o filtro de cards.py"""

        command = f"""
                    SELECT orderNumber, orderValue, dateUpdate
                    FROM orderStage
                    WHERE isCommit = 0 AND cashierNumber = {cashier_number} AND orderNumber = {order_number};
                    """
        result = self._search_and_fetch(command)

        return result

    def get_order_details(self, order_number) -> list:
        # Pega um único pedido para a janela card_details

        command = f"""
        SELECT * FROM orderStage WHERE orderNumber = '{order_number}' AND isCommit = 0
        """
        result = self._search_and_fetch(command)

        return result

    def insert_checked_order(self, flag, installments, order_number, current_installment, payday, order_value, NSU,
                             transaction_authorization, transaction_type) -> None:

        command = f"""
            INSERT INTO checkedOrders (orderNumber, cashierNumber, cashFLow, transactionType, flag, installments, installmentValue, currentInstallment, purchaseDate, payday, orderValue, flagTax, liquidValue, storeUnit, NSU, [transactionAuthorization])
                SELECT
                    '{order_number}',
                    os.cashierNumber,
                    os.cashFlow,
                    '{transaction_type}',
                    '{flag}',
                    '{installments}',
                    {order_value} / {'1' if installments == 0 else installments},
                    '{current_installment}',
                    os.dateUpdate,
                    '{payday}',
                    {order_value},
                    (SELECT cf.tax FROM cardFlags cf WHERE cf.flag = '{flag}' AND cf.installments = '{installments}'),
                    {order_value} - ({order_value} * ((SELECT cf.tax FROM cardFlags cf WHERE cf.flag = '{flag}' AND cf.installments = '{installments}') / 100)),
                    os.storeUnit,
                    '{NSU}',
                    '{transaction_authorization}'
                FROM orderStage as os
                WHERE os.orderNumber = '{order_number}' AND isCommit = 0;"""

        self._execute_and_commit(command)

    def get_orders_to_conference_report(self, initial_date: str, final_date: str, cashier_number: str) -> list:

        command = f"""SELECT DISTINCT orderNumber, cashierNumber, cashFlow, transactionType, flag, installments, installmentValue, orderValue, purchaseDate FROM checkedOrders WHERE purchaseDate BETWEEN '{initial_date}' AND '{final_date}' AND cashierNumber = {cashier_number} ORDER BY purchaseDate"""

        result = self._search_and_fetch(command)

        return result

    def get_orders_by_date_management(self, initial_date: str, final_date: str) -> list:
        command = f"""SELECT DISTINCT orderNumber, cashierNumber, cashFlow, transactionType, flag, orderValue, purchaseDate, storeUnit, NSU, transactionAuthorization FROM checkedOrders WHERE purchaseDate BETWEEN '{initial_date}' AND '{final_date}' ORDER BY purchaseDate"""

        result = self._search_and_fetch(command)

        return result

    def get_orders_by_number_management(self, order: str) -> list:
        command = f"""SELECT orderNumber, cashierNumber, cashFlow, transactionType, flag, orderValue, purchaseDate, storeUnit, NSU, transactionAuthorization FROM checkedOrders WHERE orderNumber = '{order}'"""

        result = self._search_and_fetch(command)

        return result

    def get_orders_by_nsu_or_authorization_management(self, nsu_authorization: str) -> list:
        command = f"""IF EXISTS (SELECT NSU FROM checkedOrders WHERE NSU = '{nsu_authorization}')
                    BEGIN
                        SELECT orderNumber, cashierNumber, cashFlow, transactionType, flag, orderValue, purchaseDate, storeUnit, NSU, transactionAuthorization FROM checkedOrders WHERE NSU = '{nsu_authorization}'
                    END

                ELSE IF EXISTS (SELECT transactionAuthorization FROM checkedOrders WHERE transactionAuthorization = '{nsu_authorization}')
                    BEGIN
                        SELECT orderNumber, cashierNumber, cashFlow, transactionType, flag, orderValue, purchaseDate, storeUnit, NSU, transactionAuthorization FROM checkedOrders WHERE transactionAuthorization = '{nsu_authorization}'
                    END
                  """

        result = self._search_and_fetch(command)

        return result

    def get_paydays_and_installments(self, initial_date, final_date) -> list:
        command = f"SELECT installmentValue, payday FROM checkedOrders WHERE payday BETWEEN '{initial_date}' AND '{final_date}'"

        result = self._search_and_fetch(command)

        return result

    def management(self) -> list:
        command = """SELECT orderNumber, cashierNumber, cashFlow, transactionType, flag, orderValue, purchaseDate, storeUnit, NSU, transactionAuthorization FROM checkedOrders WHERE storeUnit = (SELECT storeUnit from stores WHERE id = 4)"""

        result = self._search_and_fetch(command)

        return result

    def get_card_flags(self) -> list:
        command = f"""
        SELECT DISTINCT flag FROM cardFlags
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
