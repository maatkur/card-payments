import json
from db_handler import DatabaseHandler
from datetime import datetime


def search(initial_date, final_date):

    initial_date = datetime.strptime(initial_date, '%d/%m/%Y').strftime('%Y-%m-%d')
    final_date = datetime.strptime(final_date, '%d/%m/%Y').strftime('%Y-%m-%d')

    handler = DatabaseHandler()
    handler.connect()
    payments = handler.get_paydays_and_installments(initial_date, final_date)
    handler.disconnect()
    pre_json = {}

    for payment in payments:

        purchase_value = round(float(payment[0]), 2)
        payment_date = payment[1]

        if payment_date in pre_json:
            pre_json[payment_date] += purchase_value
        else:
            pre_json[payment_date] = purchase_value

    for date, value in pre_json.items():
        pre_json[date] = round(value, 2)

    print(pre_json)

    with open("payments.json", 'w') as file:
        json.dump(pre_json, file)


if __name__ == "__main__":
    search('20/03/2023', '19/09/2023')
