from payments_conciliation import teste_cielo
from dotenv import load_dotenv
from database.repositories.repository_manager import RepositoryManager

load_dotenv('./development.env')


def match_payments():
    cielo_payments = teste_cielo()
    old_payments = RepositoryManager.old_payments_repository().teste_conciliations()
    checked_orders = RepositoryManager.checked_orders_repository().teste_conciliations()

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


if __name__ == "__main__":
    dd = match_payments()
    # print(f"Pagamentos novos encontrados: {len(found_payments)}")
    # print(f"Pagamentos antigos encontrados: {len(old_found_payments)}")
    # print(f"Pagamentos não encontrados: {len(not_found_payments)}")
    # print(f"Total: {len(cielo_payments)}")
