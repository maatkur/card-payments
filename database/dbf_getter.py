import os

users_file_path = r"F:\esmcun\vendedor.dbf"
file_destiny = r"F:\MK\tempDBFs"


def get_users():
    os.system(fr"copy {users_file_path} {file_destiny}\vendedor.dbf")


def remove_users_file():
    os.remove(fr"{file_destiny}\vendedor.dbf")
