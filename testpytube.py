from asyncio import streams
from operator import truediv
from pytube import YouTube


yt = YouTube(input("Enter the link for the video you want to download: "))
#get all the available video streams of the youtube video

#download audio 
yt.streams.filter(adaptive=True, type = "audio", file_extension="webm").first().download()


