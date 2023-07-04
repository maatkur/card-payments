import json
import sys
from database.repositories.repository_manager import RepositoryManager
from helpers.date_helpers import DateHelpers
from dotenv import load_dotenv

load_dotenv(r"f:\MK\Apps.env")


def search():

    date_period = {
        "initial_date": DateHelpers.to_sql_format(sys.argv[1]),
        "final_date": DateHelpers.to_sql_format(sys.argv[2])
    }

    payments = RepositoryManager.checked_orders_repository().get_cash_flow(date_period)

    old_payments = RepositoryManager.old_payments_repository().get_cash_flow(date_period)
    pre_json = {}

    for payment in old_payments:
        purchase_value = round(float(payment[0]), 2)
        payment_date = DateHelpers.to_default_format(payment[1])

        if payment_date in pre_json:
            pre_json[payment_date] += purchase_value
        else:
            pre_json[payment_date] = purchase_value

    for payment in payments:

        purchase_value = round(float(payment[0]), 2)
        payment_date = DateHelpers.to_default_format(payment[1])

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
