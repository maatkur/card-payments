from database.repositories.users_repository import UsersRepository
from database.repositories.stores_repository import StoresRepository
from database.repositories.card_flags_repository import CardFlagsRepository
from database.repositories.order_stage_repository import OrderStageRepository
from database.repositories.checked_orders_repository import CheckedOrdersRepository
from database.repositories.old_payments_repository import OldPaymentsRepository


class RepositoryManager:
    _users_repository = None
    _stores_repository = None
    _card_flags_repository = None
    _order_stage_repository = None
    _checked_orders_repository = None
    _old_payments_repository = None

    @staticmethod
    def users_repository():
        if RepositoryManager._users_repository is None:
            RepositoryManager._users_repository = UsersRepository()
        return RepositoryManager._users_repository

    @staticmethod
    def stores_repository():
        if RepositoryManager._stores_repository is None:
            RepositoryManager._stores_repository = StoresRepository()
        return RepositoryManager._stores_repository

    @staticmethod
    def card_flags_repository():
        if RepositoryManager._card_flags_repository is None:
            RepositoryManager._card_flags_repository = CardFlagsRepository()
        return RepositoryManager._card_flags_repository

    @staticmethod
    def order_stage_repository():
        if RepositoryManager._order_stage_repository is None:
            RepositoryManager._order_stage_repository = OrderStageRepository()
        return RepositoryManager._order_stage_repository

    @staticmethod
    def checked_orders_repository():
        if RepositoryManager._checked_orders_repository is None:
            RepositoryManager._checked_orders_repository = CheckedOrdersRepository()
        return RepositoryManager._checked_orders_repository

    @staticmethod
    def old_payments_repository():
        if RepositoryManager._old_payments_repository is None:
            RepositoryManager._old_payments_repository = OldPaymentsRepository()
        return RepositoryManager._old_payments_repository
