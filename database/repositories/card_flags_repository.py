from database.repository_config import RepositoryConfig


class CardFlagsRepository(RepositoryConfig):

    def __init__(self):
        self.table_name = "cardFlags"
        super().__init__(self.table_name)

    def get_flag_tax(self, card_flag, installment):
        options = {
            "select": "tax",
            "query": {
                "flag": card_flag,
                "installments": installment,
            }
        }

        return float(self.get_all(options)[0][0])
