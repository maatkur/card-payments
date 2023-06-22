import os
import shutil

from dbfread import DBF


class UsersDbfRepository:

    def __init__(self):

        self.users_file_path = r"F:\esmcun\vendedor.dbf"
        self.users_file_destiny = r"./tmp/vendedor.dbf"
        self.user_list = {}
        # self.dbf_read_file = DBF()

    @staticmethod
    def get_users(self) -> None:
        shutil.copy(self.users_file_path, self.users_file_destiny)

    @staticmethod
    def remove_users_file(self) -> None:
        os.remove(fr"{self.users_file_destiny}\vendedor.dbf")

    # def generate_users_list(self) -> dict:
    #
    #     for record in db_file_read:
    #         user_name = db_file_read.records[index]["NOME"]
    #         user_code = db_file_read.records[index]["CODIGO"]
    #         password = str(db_file_read.records[index]["SENHA"])
    #         admin_user = str(db_file_read.records[index]["DEPOSITOS"])
    #         store = str(db_file_read.records[index]["EMPRESA"])
    #
    #         if user_code[0] == "0":
    #             user_code = user_code[1:]
    #
    #         users_info.update(
    #             {user_code: {
    #                 "user": user_name,
    #                 "user_code": user_code,
    #                 "password": password,
    #                 "admin": admin_user,
    #                 "store": store
    #             }
    #             }
    #         )
    #
    #         index += 1
    #
    #     return users_info