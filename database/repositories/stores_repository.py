from database.repository_config import RepositoryConfig


class StoresRepository(RepositoryConfig):

    def __init__(self):
        self.table_name = "stores"
        super().__init__(self.table_name)

    def get_store_by_id(self, id_number: int or str):

        command = f"SELECT storeUnit FROM {self.table_name} WHERE id = {id_number}"

        result = self._search_and_fetch_one(command)

        if isinstance(result, type(None)):
            return
        else:
            return result[0]
