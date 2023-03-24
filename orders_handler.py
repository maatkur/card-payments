import sys
from db_handler import DatabaseHandler


def order_handler() -> None:
    handler = DatabaseHandler()
    handler.connect()

    order_number = str(sys.argv[1])
    cashier_number = str(sys.argv[2])
    cash_flow = str(sys.argv[3])
    order_value = float(sys.argv[4])
    company_unity = int(sys.argv[5])

    handler.insert_in_order_stage(order_number, cashier_number, cash_flow,
                                  order_value, company_unity)

    handler.disconnect()


if __name__ == "__main__":
    order_handler()
