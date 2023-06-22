import datetime
from dateutil.relativedelta import relativedelta
from workalendar.america import Brazil


def paydays(payment_date, installments, transaction_type):
    # Instanciando o calendário do Brasil
    calendar = Brazil()

    payment_date = datetime.datetime.strptime(payment_date, '%Y-%m-%d').date()
    installments = int(installments)

    # Define a data de vencimento da primeira parcela
    if transaction_type == "credit":
        due_date = payment_date + relativedelta(months=1)
    elif transaction_type == "debit":
        due_date = calendar.add_working_days(payment_date, 1)

    # Loop para calcular a data de vencimento de cada parcela
    installments_date = []
    for i in range(installments):
        # Verifica se a data de vencimento é um dia útil e, caso contrário, passa para o próximo dia útil
        while not calendar.is_working_day(due_date):
            due_date = calendar.add_working_days(due_date, 1)

        installments_date.append(due_date.strftime("%Y-%m-%d"))

        # Calcula a data de vencimento da próxima parcela
        due_date += relativedelta(months=1)

    # Retorna a lista de datas de vencimento das parcelas
    return installments_date


if __name__ == "__main__":
    p = paydays("2023-05-31", 2, "credit")
    print(p)
