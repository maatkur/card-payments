import shutil

import bcrypt
from dbfread import DBF

from database.repository_config import RepositoryConfig


class UsersRepository(RepositoryConfig):

    def __init__(self) -> None:
        self.table_name = "users"
        super().__init__(self.table_name)

    def _get_user_credentials(self, user_code) -> dict:

        options = {"select": "userCode, password",
                   "query": {
                       "userCode": user_code
                   }}

        user_credentials = self.get_all(options)
        (
            user_code,
            password
        ) = user_credentials[0]

        return {
            "userCode": user_code,
            "password": password
        }

    def update_users_repository(self, user_info: dict) -> None:
        command = """
            MERGE INTO users AS target
            USING (VALUES (?, ?, ?, ?)) AS source (userCode, userName, password, store)
            ON target.userCode = source.userCode
            WHEN MATCHED THEN
                UPDATE SET userName = source.userName, password = source.password
            WHEN NOT MATCHED THEN
                INSERT (userCode, userName, password, store, adminUser)
                VALUES (source.userCode, source.userName, source.password, source.store, 0);
        """

        values = list(user_info.values())

        self._execute_and_commit(command, values)

    @staticmethod
    def get_users_file() -> None:
        shutil.copy(r"F:\esmcun\vendedor.dbf", r"./tmp/vendedor.dbf")

    @staticmethod
    def get_dbf_users_data() -> dict:

        dbf_users_file = r"./tmp/vendedor.dbf"
        dbf_users_read = DBF(dbf_users_file, encoding="cp437", load=True)

        users_info = {}

        for record in dbf_users_read:
            user_code = record["CODIGO"]
            user_name = record["NOME"]
            password = str(record["SENHA"])
            store = record["EMPRESA"]

            if user_code[0] == "0":
                user_code = user_code[1:]

            user = {
                "user_code": user_code,
                "user": user_name,
                "password": UsersRepository._encrypt_password(password),
                "store": store,
            }

            users_info.update(
                {user_code: user}

            )

        return users_info

    def update_users_from_dbf(self) -> None:
        UsersRepository.get_users_file()
        users_info = UsersRepository.get_dbf_users_data()

        for user_code, user_details in users_info.items():
            self.update_users_repository(user_details)

    @staticmethod
    def _encrypt_password(password) -> str:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')

    def authenticate_user(self, user_code: str, incomming_password: str) -> bool:
        user_credentials = self._get_user_credentials(user_code)

        if user_credentials:
            stored_password = user_credentials["password"]

            if bcrypt.checkpw(incomming_password.encode('utf-8'), stored_password.encode('utf-8')):
                return True
            else:
                return False
        else:
            return False

    def get_user_info(self, user_code):
        options = {
            "select": "userCode, adminUser, store",
            "distinct": True,
            "query": {
                "userCode": user_code
            }
        }

        user_info = self.get_all(options)

        # Desempacotar os valores da tupla em variáveis
        (
            user_code,
            admin_user,
            store,
        ) = user_info[0]

        # Retornar os valores em um dicionário
        return {
            "userCode": user_code,
            "adminUser": admin_user,
            "store": store,

        }
