def add_song_to_playlist(playlists, user, playlist_name, song, artist):

    if user not in playlists:
        playlists[user] = {}

    if playlist_name not in playlists[user]:
        playlists[user][playlist_name] = []

    playlists[user][playlist_name].append({
        "song": song,
        "artist": artist
    })


playlists = {}

add_song_to_playlist(playlists, "vikas", "Favourite", "Kesariya", "Arijit")
add_song_to_playlist(playlists, "vikas", "Favourite", "Believer", "Imagine Dragons")

print(playlists)
