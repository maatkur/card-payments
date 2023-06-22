import shutil

import bcrypt
from dbfread import DBF

from database.repository_config import RepositoryConfig


class UsersRepository(RepositoryConfig):

    def __init__(self) -> None:
        self.table_name = "users"
        super().__init__(self.table_name)

    def update_users_repository(self, user_info: dict) -> None:
        command = """
            MERGE INTO users AS target
            USING (VALUES (?, ?, ?, ?)) AS source (userCode, userName, password, store)
            ON target.userCode = source.userCode
            WHEN MATCHED THEN
                UPDATE SET userName = source.userName, password = source.password
            WHEN NOT MATCHED THEN
                INSERT (userCode, userName, password, store)
                VALUES (source.userCode, source.userName, source.password, source.store);
        """

        values = list(user_info.values())

        self._execute_and_commit(command, values)

    @staticmethod
    def get_users_file() -> None:
        shutil.copy(r"F:\esmcun\vendedor.dbf", r"./tmp/vendedor.dbf")

    @staticmethod
    def get_users_info() -> dict:

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
                "password": UsersRepository.encrypt_password(password),
                "store": store,
            }

            users_info.update(
                {user_code: user}

            )

        return users_info

    def update_users_from_dbf(self):
        UsersRepository.get_users_file()
        users_info = UsersRepository.get_users_info()

        for user_code, user_details in users_info.items():
            self.update_users_repository(user_details)

    @staticmethod
    def encrypt_password(password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')
