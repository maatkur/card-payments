import sys
from db_handler import DatabaseHandler


def order_handler() -> None:
    handler = DatabaseHandler()
    handler.connect()

    order_number = str(sys.argv[1])
    cashier_number = str(sys.argv[2])
    cash_flow = str(sys.argv[3])
    transaction_type = sys.argv[4].lower()
    order_value = float(sys.argv[5])
    company_unity = int(sys.argv[6])

    check_transaction_type = transaction_type == 'credit' or transaction_type == 'debit'

    if check_transaction_type:
        handler.insert_in_order_stage(order_number, cashier_number, cash_flow, transaction_type,
                                      order_value, company_unity)
    else:
        handler.delete_order(order_number)

    handler.disconnect()


if __name__ == "__main__":
    order_handler()
