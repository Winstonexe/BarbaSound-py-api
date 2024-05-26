from fastapi import APIRouter
from services.Data_processor import DataProcessor

router = APIRouter()

@router.get("/search")
async def search(query: str, search_type: str = 'tracks'):
    return DataProcessor().search(query=query, search_type=search_type)

@router.get("/artists")
async def get_artist(artist_id: str):
    return DataProcessor().get_artist(artist_id=artist_id)

@router.get("/tracks")
async def get_track(track_id: str):
    return DataProcessor().get_tracks(track_id=track_id)

@router.get("/lyrics")
async def get_lyrics(track_id: str):
    return DataProcessor().get_lyrics(track_id=track_id)