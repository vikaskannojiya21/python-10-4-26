from playlist import add_song, remove_song, display_playlist


playlist = []

playlist = add_song("Kesariya", playlist)
playlist = add_song("Shape of You", playlist)
playlist = add_song("Believer", playlist)

print("After Adding Songs:")
display_playlist(playlist)


playlist = remove_song("Shape of You", playlist)

print("\nAfter Removing Song:")
display_playlist(playlist)
