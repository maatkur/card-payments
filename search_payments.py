import json
import os
import sys
from database.db_handler import DatabaseHandler
from helpers import to_sql_format, to_default_format
from dotenv import load_dotenv


load_dotenv(r"F:\MK\Apps\search_payments\.env")


def search():

    initial_date = to_sql_format(sys.argv[1])
    final_date = to_sql_format(sys.argv[2])

    handler = DatabaseHandler()
    print(handler.server)
    handler.connect()

    cursor = handler.connection.cursor()
    payments = handler.get_paydays_and_installments(initial_date, final_date)

    command = f"SELECT installmentValue, payday FROM oldPayments WHERE payday BETWEEN '{initial_date}' AND '{final_date}'"
    cursor.execute(command)

    old_payments = cursor.fetchall()
    handler.disconnect()
    pre_json = {}

    for payment in old_payments:
        purchase_value = round(float(payment[0]), 2)
        payment_date = to_default_format(payment[1])

        if payment_date in pre_json:
            pre_json[payment_date] += purchase_value
        else:
            pre_json[payment_date] = purchase_value

    for payment in payments:

        purchase_value = round(float(payment[0]), 2)
        payment_date = to_default_format(payment[1])

        if payment_date in pre_json:
            pre_json[payment_date] += purchase_value
        else:
            pre_json[payment_date] = purchase_value

    for date, value in pre_json.items():
        pre_json[date] = round(value, 2)

    with open("payments.json", 'w') as file:
        json_list = []
        for date, value in pre_json.items():
            json_list.append({"data": date, "valor": value})
        json.dump(json_list, file)


if __name__ == "__main__":
    search()


