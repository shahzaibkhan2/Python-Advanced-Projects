from pytube import Playlist

yt_playlist = Playlist("https://www.youtube.com/watch?v=6Zbhvaac68Y&list=PLlL_rsmcRMZfDx2VycMXNYc9bERDgYvPi")

print(f'downloading: {yt_playlist.title}')

for video in yt_playlist.videos:
    video.streams.first().download()