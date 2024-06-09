from typing import Dict, Any
from aiohttp import ClientSession
from constants import *

class ApiService():
    def __init__(self, client: ClientSession) -> None:
        self.client = client
    
    async def search(self,
               query: str, 
               type: str, 
               offset: int = 0, 
               limit: int = 50, 
               numberOfTopResults: int = 5) -> Dict[str, Any] | None:
        
        query_string = {
            "q": query,
            "type": type,
            "offset": str(offset),
            "limit": str(limit),
            "numberOfTopResults": str(numberOfTopResults)
        }
        async with self.client.get(url=URL_SEARCH, headers=HEADERS, params=query_string) as response:
            return await response.json()
    
    async def get_tracks(self, track_id: str) -> Dict[str, Any] | None:
        query_string = {"ids": track_id}
        async with self.client.get(url=URL_TRACKS, headers=HEADERS, params=query_string) as response:
            return await response.json()
    
    async def track_lyrics(self, track_id: str) -> Dict[str, Any] | None:
        query_string = {"id": track_id}
        async with self.client.get(url=URL_LYRICS, headers=HEADERS, params=query_string) as response:
            return await response.json()
    
    async def get_artist(self, artist_id: str) -> Dict[str, Any] | None:
        query_string = {"ids": artist_id}
        async with self.client.get(url=URL_ARTISTS, headers=HEADERS, params=query_string) as response:
            return await response.json()
        
    async def get_playlist_tracks(self, playlist_id: str) -> Dict[str, Any] | None:
        query_string = {
            "id": playlist_id,
            "offset":"0",
            "limit":"100"}
        async with self.client.get(url=URL_PLAYLIST, headers=HEADERS, params=query_string) as response:
            return await response.json()