import os
import sys

from dotenv import load_dotenv

from database.repositories.order_stage_repository import OrderStageRepository
from database.repositories.stores_repository import StoresRepository
from database.repositories.checked_orders_repository import CheckedOrdersRepository

load_dotenv(r"C:\Users\Matheus\PycharmProjects\trykat-card\development.env")


def order_handler() -> None:

    stores_repository = StoresRepository()
    order_stage_repository = OrderStageRepository()
    checked_orders_repository = CheckedOrdersRepository()

    order = {"orderNumber": str(sys.argv[1]),
             "cashierNumber": str(sys.argv[2]),
             "cashFlow": str(sys.argv[3]),
             "orderValue": str(sys.argv[4]),
             "storeUnit": stores_repository.get_store_by_id(str(sys.argv[5])),
             "isCommit": "0"}

    order_stage_repository.insert(order)

    checked_orders_repository.delete("orderNumber", order["orderNumber"])


if __name__ == "__main__":
    order_handler()
