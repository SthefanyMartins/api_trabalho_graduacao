from typing import List

from fastapi import APIRouter, Depends
from tg_api.presentation.dependencies import application_container

router = APIRouter()


@router.post("/flush_cache/")
async def flushall(dependencies=Depends(application_container)):
    await dependencies.cache_repository.flushall()