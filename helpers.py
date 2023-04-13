from datetime import datetime


def to_sql_format(date: str) -> str:
    date_object = datetime.strptime(date, "%d/%m/%Y")
    formatted_date = date_object.strftime("%Y-%m-%d")

    return formatted_date


def to_default_format(date: str) -> str:
    date_object = datetime.strptime(date, "%Y-%m-%d")
    formatted_date = date_object.strftime("%d/%m/%Y")

    return formatted_date


def to_date_string() -> str:
    date_object = datetime.now()
    formatted_date = date_object.strftime('%d%m%Y%H%M%S')

    return formatted_date
