# ------ For single video only ------
from pytube import YouTube

link = "https://www.youtube.com/watch?v=bKDhmENcKto"
youtube_title = YouTube(link)
# print(youtube_title.title)
# print(youtube_title.thumbnail_url)
videos = youtube_title.streams.all()
# videos_2 = youtube_title.streams.filter(only_video=True) # for videos only
# videos_1 = youtube_title.streams.filter(only_audio=True) # for audio only
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
stream_to_download = int(input('Enter your stream: '))
videos[stream_to_download].download()
print('Successfully downloaded!')