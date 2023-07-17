from database.repositories.repository_manager import RepositoryManager
from carrier_excel import load_excel_payments


def match_payments():
    cielo_payments = load_excel_payments()

    found_payments = []
    old_found_payments = []
    not_found_payments = []

    for payment in cielo_payments:
        payment_was_found = False

        payment_search = RepositoryManager.checked_orders_repository().get_conciliations({
            "NSU": payment["NSU"],
            "transactionAuthorization": payment["transactionAuthorization"],
            "currentInstallment": f'{payment["currentInstallment"]}/{payment["installments"]}'
        })

        old_payments_search = RepositoryManager.old_payments_repository().get_conciliations({
            "NSU": payment["NSU"],
            "transactionAuthorization": payment["transactionAuthorization"],
            "currentInstallment": payment["oldCurrentInstallment"]
        })

        if payment_search:
            payment_search["payday"] = payment["payday"]
            found_payments.append(payment_search)
            payment_was_found = True

        if old_payments_search:
            old_payments_search["payday"] = payment["payday"]
            old_found_payments.append(old_payments_search)
            payment_was_found = True

        if not payment_was_found:
            not_found_payments.append(payment)

    found_payments = sorted(found_payments, key=lambda x: x['orderNumber'])

    return old_found_payments, found_payments, not_found_payments
