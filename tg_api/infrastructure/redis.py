from tg_api.infrastructure.config import settings
from redis import asyncio as aioredis

redis = aioredis.Redis.from_url(settings.redis_url, decode_responses=True)
