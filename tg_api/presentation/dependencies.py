from dependencies import Injector
from tg_api.infrastructure.repository.cache_repository import CacheRepository
from tg_api.infrastructure.repository.queries_repository import QueriesRepository
from tg_api.infrastructure.database import database
from tg_api.infrastructure.redis import redis


def application_container():
    yield Injector(
        redis=redis,
        database=database,
        queries_repository=QueriesRepository,
        cache_repository=CacheRepository,
    )
