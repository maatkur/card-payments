from database.repository_config import RepositoryConfig


class CardFlagsRepository(RepositoryConfig):

    def __init__(self):
        self.table_name = "cardFlags"
        super().__init__(self.table_name)
