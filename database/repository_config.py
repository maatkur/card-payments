import pyodbc
import os

from dotenv import load_dotenv
from helpers.dict_helper import dict_merge, dict_to_query

load_dotenv("./development.env")


class RepositoryConfig:
    def __init__(self, table_name):
        self.server = os.getenv("SERVER")
        self.database = os.getenv("DATABASE")
        self.user = 'sa'
        self.password = '$ervid0r'
        self.connection = None
        self.table_name = table_name
        if type(self) is RepositoryConfig:
            raise NotImplementedError("DatabaseConfig class cannot be started directly, you must use it as inheritance")

    def _connect(self) -> None:
        # Cria uma conexão com o banco de dados.
        try:
            self.connection = pyodbc.connect(
                fr'DRIVER={{SQL Server}};Server={self.server}\SQLEXPRESS;Database={self.database};User Id={self.user};Password={self.password};MultipleActiveResultSets=true;')
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def _disconnect(self) -> None:
        # Desconecta do banco de dados.
        self.connection.close()

    def _execute_and_commit(self, command, values=None) -> None:
        # Executa uma consulta que altera dados no banco de dados e realiza um commit.
        try:
            self._connect()
            cursor = self.connection.cursor()
            if values:
                cursor.execute(command, values)
            else:
                cursor.execute(command)

            self.connection.commit()
            self._disconnect()
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()
            self._disconnect()
            raise

    def _search_and_fetch_one(self, command) -> list:
        # Executa uma busca e retorna o resultado em uma tupla
        self._connect()
        command = command
        cursor = self.connection.cursor()
        cursor.execute(command)
        result = cursor.fetchone()
        self._disconnect()
        return result

    def _search_and_fetch_all(self, command, values=()) -> list:
        # Executa uma busca e retorna o resultado em uma lista de tuplas
        self._connect()
        cursor = self.connection.cursor()
        cursor.execute(command, values)
        result = cursor.fetchall()
        self._disconnect()
        return result

    def insert(self, data: dict) -> None:
        keys = ", ".join(data.keys())
        placeholders = ", ".join(
            ["?"] * len(data))  # Cria uma string com a mesma quantidade de placeholders que os valores

        command = f"INSERT INTO {self.table_name} ({keys}) VALUES ({placeholders})"
        values = tuple(data.values())  # Cria uma tupla com os valores do dicionário

        self._execute_and_commit(command, values)

    def get_all(self, options: dict) -> list:
        options = dict_merge({"select": "*", "distinct": False, "order_by": None}, options)
        command = f"SELECT"
        if options.get('distinct'):
            command += " DISTINCT"
        command += f" {options['select']} FROM {self.table_name} "
        if options.get('query'):
            query = dict_to_query(options['query'])
            command += query
        if options.get('order_by'):
            order_by = ", ".join(options['order_by'])
            command += f" ORDER BY {order_by}"

        return self._search_and_fetch_all(command)

    def delete(self, options: dict) -> None:
        keys = ", ".join(options.keys())
        placeholders = " AND ".join(
            [f"{key} = ?" for key in options])  # Cria uma string com os placeholders para as condições

        command = f"DELETE FROM {self.table_name} WHERE {placeholders}"
        values = tuple(options.values())  # Cria uma tupla com os valores das condições

        self._execute_and_commit(command, values)
