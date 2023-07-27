from reports.report_config import ReportConfig
from helpers.date_helpers import DateHelpers


class UnconciliatedsReport(ReportConfig):

    def __init__(self):
        self.header = ["Pedido", "Transação", "Bandeira", "Parcelas", "Valor da parcela", "N° da parcela",
                       "Data da compra", "Pagamento segundo operadora", "Taxa", "Valor liquído", "NSU",
                       "Autorização", "Status"]
        self.second_header = ["Pagamento segundo operadora", "Taxa", "Valor da parcela", "N° da parcela", "Parcelas",
                              "nsu", "Autorização", "Status"]

        self.report_name = "nao_conciliados"
        super().__init__(self.header, self.report_name)


    def add_checked_orders_data(self, data: list) -> None:
        self.worksheet.append(self.header)

        for order in data:
            (
                order_number,
                transaction_type,
                flag,
                installments,
                installment_value,
                current_installment,
                purchase_date,
                payday,
                tax,
                liquid_value,
                nsu,
                transaction_authorization,
                status,
                _,
            ) = order

            transaction_type = "Débito" if transaction_type == "debit" else "Crédito"
            installment_value = round(installment_value, 2)
            purchase_date = DateHelpers.to_default_format(purchase_date)
            payday = DateHelpers.to_default_format(payday)
            liquid_value = round(liquid_value, 2)

            self.worksheet.append(
                [order_number,
                 transaction_type,
                 flag,
                 installments,
                 installment_value,
                 current_installment,
                 purchase_date,
                 payday,
                 tax,
                 liquid_value,
                 nsu,
                 transaction_authorization,
                 status
                 ]
            )

    def add_old_payments_data(self, data: list):

        self.worksheet.append(self.second_header)

        for order in data:
            (
                payday,
                tax,
                installment_value,
                current_installment,
                installments,
                nsu,
                transaction_authorization,
                status,
                _,
            ) = order

            installment_value = round(installment_value, 2)
            payday = DateHelpers.to_default_format(payday)

            self.worksheet.append(
                [
                    payday,
                    tax,
                    installment_value,
                    current_installment,
                    installments,
                    nsu,
                    transaction_authorization,
                    status,
                 ]
            )

    def generate(self, data: tuple):
        checked_orders, old_payments = data
        self.workbook["Sheet"].title = "Pagamentos atuais"
        self.add_checked_orders_data(checked_orders)
        self.create_new_worksheet("Pagamentos conexão")
        self.switch_worksheet("Pagamentos conexão")
        self.add_old_payments_data(old_payments)
        self.set_header_style()
        self.save_workbook()
        self.reset()
