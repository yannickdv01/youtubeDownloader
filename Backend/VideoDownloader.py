from pytube import YouTube
from pytube.cli import on_progress
from colorama import Fore, Back, Style
import Frontend.Home as Home
import time

#function that takes a youtube link and downloads it

#path will be the downloads folder
Download_Path = "C:\\Users\\Downloads"
yt = ""

def GetVideoInfo(link):
    try:
        return YouTube(link, on_progress_callback=on_progress)
        #DisplayVideoInfo(yt)
    except:
        print(Fore.RED + "Connection Error" + Style.RESET_ALL)

def DisplayVideoInfo(video : YouTube):
    print("Title: " + video.title)
    print("Views: " + video.views)
    print("Length: " + video.length)

def Youtube_Downloader(video : YouTube, format : str):
    try:
        #object creation using YouTube which was #imported in the beginning
        get = video.streams.filter(progressive=True, file_extension=format).get_highest_resolution()

        print(Fore.GREEN + "Downloading...")
        #downloading the video
        get.download()
        print("Video downloaded, you will be sent back to the homepage in a few seconds :)" + Style.RESET_ALL)

        time.sleep(2)
        Home.homescreen()
    except:
        print(Fore.RED + "Connection Error" + Style.RESET_ALL)

    #filters out all the files with "mp4" extension
   