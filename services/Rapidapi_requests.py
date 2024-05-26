from typing import Dict, Any
import requests
from constants import *

class RapidapiRequests():
    
    @staticmethod
    def search(query: str, 
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
        
        response = requests.get(url=URL_SEARCH, headers=HEADERS, params=query_string)
        return response.json()
    
    @staticmethod
    def get_tracks(track_id: str) -> Dict[str, Any] | None:
        query_string = {"ids": track_id}
        response = requests.get(url=URL_TRACKS, headers=HEADERS, params=query_string)
        return response.json()
    
    @staticmethod
    def track_lyrics(track_id: str) -> Dict[str, Any] | None:
        query_string = {"id": track_id}
        response = requests.get(url=URL_LYRICS, headers=HEADERS, params=query_string)
        return response.json()
    
    @staticmethod
    def get_artist(artist_id: str) -> Dict[str, Any] | None:
        query_string = {"ids": artist_id}
        response = requests.get(url=URL_ARTISTS, headers=HEADERS, params=query_string)
        return response.json()
    
    @staticmethod
    def artist_related(artist_id: str) -> Dict[str, Any] | None:
        query_string = {"ids": artist_id}
        response = requests.get(url=URL_RELATED, headers=HEADERS, params=query_string)
        return response.json()