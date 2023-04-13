import random
from database.db_handler import DatabaseHandler


handler = DatabaseHandler()
handler.connect()

inserts = 10

for x in range(0, inserts):
    randomic_order_numbers = str(random.randint(202321, 203321))

    cash_flow_number = str(random.randint(1000, 2000))

    min_value = 100.00
    max_value = 5000.00

    order_number = randomic_order_numbers
    cashier_number = '63'
    cash_flow = cash_flow_number
    order_value = round(random.uniform(min_value, max_value), 2)
    company_unity = 3

    handler.insert_in_order_stage(order_number, cashier_number, cash_flow, order_value, company_unity)

handler.disconnect()
