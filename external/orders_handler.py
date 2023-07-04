import os
import sys


from dotenv import load_dotenv

from database.repositories.repository_manager import RepositoryManager

from helpers.uuid_helpers import UuidHelpers

load_dotenv(r"F:\MK\Apps\cards_login_view\.env")


def order_handler() -> None:

    order = {"orderNumber": str(sys.argv[1]),
             "cashierNumber": str(sys.argv[2]),
             "cashFlow": str(sys.argv[3]),
             "orderValue": str(sys.argv[4]),
             "storeUnit": RepositoryManager.stores_repository().get_store_by_id(str(sys.argv[5])),
             "isCommit": "0",
             "uId": UuidHelpers.generate_uuid()}

    RepositoryManager.order_stage_repository().insert(order)

    RepositoryManager.checked_orders_repository().delete({"orderNumber": order["orderNumber"]})


if __name__ == "__main__":
    order_handler()
