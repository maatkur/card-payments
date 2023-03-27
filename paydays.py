import datetime
from workalendar.america import Brazil


def paydays(payment_date, installments, transaction_type):

    # Instanciando o calendário do Brasil
    calendar = Brazil()

    payment_date = datetime.datetime.strptime(payment_date, '%d-%m-%Y').date()
    installments = 1 if installments == 0 else installments
    transaction_type = transaction_type

    # Define a data de vencimento da primeira parcela
    if transaction_type == "credit":
        due_date = payment_date + datetime.timedelta(days=30)
    elif transaction_type == "debit":
        due_date = calendar.add_working_days(payment_date, 1)

    # Loop para calcular a data de vencimento de cada parcela
    installments_date = []
    for i in range(installments):
        # Define a data de vencimento da parcela
        if i == 0:
            payday = due_date
        else:
            payday = due_date + datetime.timedelta(days=30*i)

        # Verifica se a data de vencimento é um dia útil e, caso contrário, adiciona um dia até que seja um dia útil
        while not calendar.is_working_day(payday):
            payday += datetime.timedelta(days=1)

        installments_date.append(payday)

    # Retorna a lista de datas de vencimento das parcelas
    return installments_date


if __name__ == "__main__":
    p = paydays('27-03-2023', 1, 'debit')
    print(p)
