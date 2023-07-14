from dotenv import load_dotenv
from database.repositories.repository_manager import RepositoryManager
from helpers.uuid_helpers import UuidHelpers

load_dotenv("./development.env")

options_sigle = {
    "select": "NSU, transactionAuthorization",
    "distinct": True}

pedidos = RepositoryManager.old_payments_repository().get_all(options_sigle)

for pedido in pedidos:

    NSU = pedido[0]
    auto = pedido[1]

    order_uid = UuidHelpers.generate_uuid()

    RepositoryManager.old_payments_repository().update_by_nsu_auth(
        {"NSU": NSU, "transactionAuthorization": auto, "uId": order_uid})
