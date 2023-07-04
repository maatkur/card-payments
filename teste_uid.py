from config.setup_config import setup_config
from database.repositories.repository_manager import RepositoryManager
from helpers.uuid_helpers import UuidHelpers

setup_config()

options_sigle = {
    "select": "orderNumber, cashierNumber, cashFlow, flag, installments, orderValue, purchaseDate, storeUnit, NSU, "
              "transactionAuthorization",
    "distinct": True}

pedidos = RepositoryManager.checked_orders_repository().get_all(options_sigle)

for pedido in pedidos:
    order_number = pedido[0]
    cashier_number = pedido[1]
    cash_flow = pedido[2]
    order_flag = pedido[3]
    order_installments = pedido[4]
    order_value = pedido[5]
    order_date = pedido[6]
    store_unit = pedido[7]
    NSU = pedido[8]
    auto = pedido[9]

    stage_order = {
        "orderNumber": order_number,
        "cashierNumber": cashier_number,
        "cashFlow": cash_flow,
        "orderValue": order_value,
        "storeUnit": store_unit,
        "dateUpdate": order_date,
        "isCommit": 1
    }

    order_uid = UuidHelpers.generate_uuid()
    stage_order["uId"] = order_uid
    RepositoryManager.order_stage_repository().insert(stage_order)
    RepositoryManager.checked_orders_repository().update_by_nsu_auth(
        {"NSU": NSU, "transactionAuthorization": auto, "uId": order_uid, "orderNumber": order_number})
