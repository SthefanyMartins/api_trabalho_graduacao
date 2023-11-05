from contextlib import asynccontextmanager

from fastapi import FastAPI
from tg_api.infrastructure.database import database
from tg_api.infrastructure.redis import redis
from tg_api.presentation.routes import cached_routes, routes, ttl_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis.flushall()
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(cached_routes.router, prefix="/cached")
app.include_router(routes.router, prefix="/nocached")
app.include_router(ttl_routes.router, prefix="/ttlcached")

# @app.get("/cached/states_count_by_region/", response_model=List[StatesCountByRegion])
# @app.get("/states_count_by_region/", response_model=List[StatesCountByRegion])
# async def get_states_count_by_region(
#     repository: Annotated[QueriesRepository, Depends(queries_repository)],
# ):
#     states = await repository.states_count_by_region()
#     return states
