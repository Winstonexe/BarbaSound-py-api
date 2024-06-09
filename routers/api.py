from typing import AsyncGenerator, Annotated

from aiohttp import ClientSession
from fastapi import APIRouter, Depends

from services.api_service import ApiService
from services.Data_processor import DataProcessor

async def get_service() -> AsyncGenerator[DataProcessor, None]:
    session = ClientSession()
    processor = DataProcessor(ApiService(session))
    try:
        yield processor
    finally:
        await session.close()

proc_type = Annotated[DataProcessor, Depends(get_service)]
router = APIRouter()

@router.get("/search")
async def search(processor: proc_type, query: str, search_type: str = 'tracks'):
    return await processor.search(query=query, search_type=search_type)

@router.get("/artists")
async def get_artist(processor: proc_type, artist_id: str):
    return await processor.get_artist(artist_id=artist_id)

@router.get("/tracks")
async def get_track(processor: proc_type, track_id: str):
    return await processor.get_tracks(track_id=track_id)

@router.get("/lyrics")
async def get_lyrics(processor: proc_type, track_id: str):
    return await processor.get_lyrics(track_id=track_id)