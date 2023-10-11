import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from engine.conversions import ms_to_min


class SpotifyEngine:
	def __init__(self, playlist_url):
		cid = "8cdb42bee2324b83b78f517d35e59f61"
		secret = "c762f709fba64df091734eca9f126059"
		client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
		self.sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
		self.playlist = playlist_url
	
	def get_playlists(self):
		playlist_link = self.playlist
		playlist_URI = playlist_link.split("/")[-1].split("?")[0]
		track_uris = [x["track"]["uri"] for x in self.sp.playlist_tracks(playlist_URI)["items"]]


		songs = []
		for track in self.sp.playlist_tracks(playlist_URI)["items"]:

			songInfo = {}
			#URI
			track_uri = track["track"]["uri"]
    
			#Track name
			track_name = track["track"]["name"]
    
			#Name, popularity, genre
			artist_name = track["track"]["artists"][0]["name"]
    
			#Album
			album = track["track"]["album"]["name"]

			#length milliseconds
			ms_duration = track['track']['duration_ms']

			#length formatted
			formatted_duration = ms_to_min(int(ms_duration))

			songInfo['uri'] = track_uri
			songInfo['track'] = track_name
			songInfo['artist'] = artist_name
			songInfo['album'] = album
			songInfo['duration_ms'] = ms_duration
			songInfo['duration_formatted'] = formatted_duration

			songs.append(songInfo)
		
		return songs

	def get_playlists_verbose(self):
		playlist_link = self.playlist
		playlist_URI = playlist_link.split("/")[-1].split("?")[0]
		track_uris = [x["track"]["uri"] for x in self.sp.playlist_tracks(playlist_URI)["items"]]

		songs = []
		for track in self.sp.playlist_tracks(playlist_URI)["items"]:

			songs.append(track)

		return songs


	def set_playlist(self, url):
		self.playlist = url
	
	def get_playlist_url(self):
		return self.playlist

	def get_playlist_name(self):
		results = spotipy.user_playlist(user=None, playlist_id="3cqDkXVInhOYPpJyVzvwux", fields="name")
		return(results["name"])


if __name__ == "__main__":
	playlist = input("PLAYLIST URL\n:")
	engine = SpotifyEngine(playlist)
	songs = engine.get_playlists_verbose()
	
	for key in (songs[0])['track']:
#		print(f"{key} -> {(songs[0])[key]}")
		print(key)
		print("-------------------")
		print(f"{((((songs[0])['track'])['duration_ms']))} MS")
		print(f"{((((songs[0])['track'])['duration_ms'])/60000)} MINUTES")
		print("-------------------")
	    
