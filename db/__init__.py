from .tables import metadata
from .base import engine

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


