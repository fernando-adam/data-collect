# %%
from pytube import YouTube

link = "https://www.youtube.com/shorts/ie17J2b2vok"

yt = YouTube(link)

stream = yt.streams.get_highest_resolution()
stream.download()
# %%
