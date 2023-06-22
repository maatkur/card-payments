from database.repository_config import RepositoryConfig


class CheckedOrdersRepository(RepositoryConfig):

    def __init__(self):
        self.table_name = "checkedOrders"
        super().__init__(self.table_name)
