from database.repository_config import RepositoryConfig


class OldPaymentsRepository(RepositoryConfig):

    def __init__(self):
        self.table_name = "oldPayments"
        super().__init__(self.table_name)

    def get_cash_flow(self, date_period: dict) -> list:
        initial_date = date_period.get("initial_date")
        final_date = date_period.get("final_date")

        if not initial_date or not final_date:
            raise ValueError("initial_date and final_date are required for fetching cash flow.")

        query = f"SELECT installmentValue, payday FROM {self.table_name} WHERE payday BETWEEN '{initial_date}' AND '{final_date}'"

        return self._search_and_fetch_all(query)
