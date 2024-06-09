from typing import Dict, List, Any
from services.api_service import ApiService

class DataProcessor:
    def __init__(self, api_service: ApiService) -> None:
        self.api_service = api_service
        
    async def search(self, query: str, search_type: str) -> List[Dict[str, Any]]:
        data = await self.api_service.search(type=search_type, query=query)
        if data is None:
            return
    
        result = []
        if 'tracks' in data and 'items' in data['tracks']:
            for track in data['tracks']['items']:
                track_data = track['data']
                track_name = track_data.get('name', 'No Name')
                track_id = track_data.get('id', 'No id')
                
                artists = track_data['artists']['items']
                artist_names = [artist['profile']['name'] for artist in artists[:5]]
                
                album_of_track = track_data['albumOfTrack']
                cover_art = album_of_track['coverArt']['sources']
                image_url = cover_art[0]['url'] if cover_art else 'No Image'
                
                track_info = {
                    "track_name": track_name,
                    "track_id": track_id,
                    "artist": ', '.join(artist_names),
                    "track_image": image_url
                }
                
                result.append(track_info)
                
        elif 'artists' in data and 'items' in data['artists']:
            for artist in data['artists']['items']:
                artists_data = artist['data']
                
                artist_id = str(artists_data.get('uri', 'No id')).split(':')[-1]
                
                artist_profile = artists_data['profile']
                artist_name = artist_profile.get('name', 'No name')
                
                artist_visuals = artists_data.get('visuals', None)
                if artist_visuals is not None:
                    avatar_image = artist_visuals.get('avatarImage', None)
                    if avatar_image is not None:
                        artist_avatar = avatar_image.get('sources', [])[0].get('url', 'No Image')
                    else:
                        artist_avatar = 'No Image'
                else:
                    artist_avatar = 'No Image'
                
                track_info = {
                    'artist_name': artist_name,
                    'artist_id': artist_id,
                    'artist_avatar': artist_avatar
                }
                
                result.append(track_info)
                      
        return result
    
    async def get_tracks(self, track_id: str) -> List[Dict[str, Any]]:
        data = await self.api_service.get_tracks(track_id=track_id)
        if data is None or 'tracks' not in data:
            return
        
        result = []
        for track in data['tracks']:
            track_name = track.get('name', 'No name')
            track_url = track.get('preview_url', 'No url')
            
            track_external = track['external_urls']
            track_spotify_url = track_external.get('spotify')
            
            artists = track['artists']
            artist_names = [artist['name'] for artist in artists]
            
            track_info = {
                "track_name": track_name,
                "track_url": track_url,
                "track_spotify_url": track_spotify_url,
                "artists_names": artist_names
            }
            
            result.append(track_info)
                    
        return result
                       
    async def get_lyrics(self, track_id: str) -> List[Dict[str, Any]]:
        data = await self.api_service.track_lyrics(track_id=track_id)
        if data is None or 'lyrics' not in data:
            return
        
        lyrics = ""
        result = []
        for line in data['lyrics']['lines']:
            lyrics += f"{line.get('words', '?')}\n"
            
        track_lyrics = {
            "track_lyrics": lyrics
        }
        
        result.append(track_lyrics)
        
        return result
    
    async def get_artist(self, artist_id: str) -> List[Dict[str, Any]]:
        data = await self.api_service.get_artist(artist_id=artist_id)
        if data is None or 'artists' not in data:
            return
        
        result = []
        for artist in data['artists']:
            artist_name = artist.get('name', 'No name')
            images = artist['images']
            
            atrist_image = images[0]['url'] if images else 'No image'
            
            spotify_url = artist['external_urls']
            artist_spotify_url = spotify_url.get('spotify', "No spotify url")  
            
            artist_geners =  artist['genres']
            
            artist_info = {
                'artist_name': artist_name,
                'artist_image': atrist_image,
                'artist_spotify_url': artist_spotify_url,
                'artist_geners': artist_geners
            }  
            
            result.append(artist_info)
                
        return result
    
    # async def get_palylist_tracks(self, playlist_id: str) -> List[Dict[str, Any]]:
    #     data = await self.api_service.get_playlist_tracks(playlist_id=playlist_id)
    #     if data is None or 
        