from pytube import YouTube
from pytube.cli import on_progress

#function that takes a youtube link and downloads it

#path will be the downloads folder
Download_Path = "C:\\Users\\Downloads"
yt = ""

def GetVideoInfo(link):
    try:
        return YouTube(link)
        #DisplayVideoInfo(yt)
    except:
        print("Connection Error")

def DisplayVideoInfo(video : YouTube):
    print("Title: " + video.title)
    print("Views: " + video.views)
    print("Length: " + video.length)

def Youtube_Downloader(video : YouTube, format : str):
    try:
        #object creation using YouTube which was #imported in the beginning
        get = video.streams.filter(progressive=True, file_extension=format).get_highest_resolution()
        #TODO: add a progress bar
        

        #downloading the video
        get.download()
    except:
        print("Connection Error")

    #filters out all the files with "mp4" extension

    