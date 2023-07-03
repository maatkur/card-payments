from database.repository_config import RepositoryConfig


class StoresRepository(RepositoryConfig):

    def __init__(self):
        self.table_name = "stores"
        super().__init__(self.table_name)

    def get_store_by_id(self, id_number: int or str):

        options = {
            "select": "storeUnit",
            "query": {
                "id": id_number
            }
        }

        result = self.get_all(options)

        if isinstance(result, type(None)):
            return
        else:
            return result[0][0]

    def get_all_stores(self) -> list:

        options = {
            "select": "storeUnit"
        }

        stores = self.get_all(options)

        stores = [store[0] for store in stores]

        return stores
