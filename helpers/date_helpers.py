from datetime import datetime


class DateHelpers:

    @staticmethod
    def to_sql_format(date: str) -> str:
        date_object = datetime.strptime(date, "%d/%m/%Y")
        formatted_date = date_object.strftime("%Y-%m-%d")

        return formatted_date

    @staticmethod
    def to_default_format(date: str) -> str:
        date_object = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = date_object.strftime("%d/%m/%Y")

        return formatted_date

    @staticmethod
    def to_date_string() -> str:
        date_object = datetime.now()
        formatted_date = date_object.strftime('%d%m%Y%H%M%S')

        return formatted_date

    @staticmethod
    def to_date_obj(date_str: str) -> datetime.date:
        return datetime.strptime(date_str, "%d/%m/%Y").date()
