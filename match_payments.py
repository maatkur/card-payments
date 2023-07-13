from database.repositories.repository_manager import RepositoryManager
from payments_conciliation import teste_cielo


def match_payments():
    cielo_payments = teste_cielo()

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

        if (
                payment_search
                and payment["currentInstallment"] == payment_search["currentInstallment"]
                and payment["NSU"] == payment_search["NSU"]
                and payment["transactionAuthorization"] == payment_search["transactionAuthorization"]
        ):
            found_payments.append(payment_search)
            payment_was_found = True

        if (
                old_payments_search
                and not payment_was_found
                and payment["oldCurrentInstallment"] == old_payments_search["currentInstallment"]
                and payment["NSU"] == old_payments_search["NSU"]
                and payment["transactionAuthorization"] == old_payments_search["transactionAuthorization"]
        ):
            old_found_payments.append(old_payments_search)
            payment_was_found = True

        if not payment_was_found:
            not_found_payments.append(payment)

    return old_found_payments, found_payments, not_found_payments
