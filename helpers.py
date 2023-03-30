from datetime import datetime


def to_sql_format(date: str) -> str:
    dt_obj = datetime.strptime(date, "%d/%m/%Y")
    formatted_date = dt_obj.strftime("%Y-%m-%d")

    return formatted_date


def to_default_format(date: str) -> str:
    dt_obj = datetime.strptime(date, "%Y-%m-%d")
    formatted_date = dt_obj.strftime("%d/%m/%Y")

    return formatted_date
