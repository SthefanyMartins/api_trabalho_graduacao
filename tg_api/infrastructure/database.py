import databases
from tg_api.infrastructure.config import settings

database = databases.Database(settings.database_url)
