import pandas as pd
from helpers import to_sql_format
from database.db_handler import DatabaseHandler

file = r"c:\users\Matheus\Desktop\oldcards.xlsx"
db_handler = DatabaseHandler()

db_handler.connect()
cursor = db_handler.connection.cursor()

data = pd.read_excel(file)
end_of_file = len(data)
index = 0

for info in range(end_of_file):
    date = to_sql_format(data["DATA_CREDITO"][index])
    order_value = round(data["VALOR"][index], 2)
    tax = data["TAXA"][index]
    installment_value = float(round(data["VALOR_LIQUIDO"][index], 2))
    nsu = data["CV"][index]
    transaction_authorization = data["AUTORIZACAO"][index]

    command = f"""INSERT INTO oldPayments (payday, orderValue, tax, installmentValue, NSU, transactionAuthorization)
        VALUES ('{date}', {order_value}, {tax}, {installment_value}, '{nsu}', '{transaction_authorization}')
        """

    print(index)
    cursor.execute(command)
    cursor.commit()

    index += 1

db_handler.disconnect()
