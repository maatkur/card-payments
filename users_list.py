from dbfread import DBF

db_file = r"F:\MK\tempDBFs\vendedor.dbf"
db_file_read = DBF(db_file, encoding="cp437", load=True)


users_info = {

}


def user_list():
    index = 0

    for record in db_file_read:
        user_name = db_file_read.records[index]["NOME"]
        user_code = db_file_read.records[index]["CODIGO"]
        password = str(db_file_read.records[index]["SENHA"])
        admin_user = str(db_file_read.records[index]["DEPOSITOS"])
        store = str(db_file_read.records[index]["EMPRESA"])

        if user_code[0] == "0":
            user_code = user_code[1:]

        users_info.update(
            {user_code: {
                "user": user_name,
                "user_code": user_code,
                "password": password,
                "admin": admin_user,
                "store": store
            }
            }
        )

        index += 1

    return users_info


if __name__ == "__main__":
    user_list()
