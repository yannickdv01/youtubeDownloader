from random import vonmisesvariate
import sys
from os.path import dirname, abspath
from time import time
sys.path.append(dirname(dirname(abspath(__file__))))

import Frontend.Menu as Menu
import Frontend.Home as Home
import Backend.VideoDownloader as VideoDownloader
from pytube import YouTube
import Backend.Clearconsole as Clearconsole
from colorama import Fore, Back, Style

def DownloadPage():
    Menu.SelectionMenu("Download", [
        Menu.MenuOption("Download video", DownLoadSubPage),
        Menu.MenuOption("Download playlist", "Playlist"),
        Menu.MenuOption("Go home", Home.homescreen),
        Menu.MenuOption("Exit", exit)
    ]
    ).display()

def DownLoadSubPage():
    Link = input("Enter the link for the video you want to download: ")
    Video = VideoDownloader.GetVideoInfo(Link)
    if Video == None:
        Clearconsole.clearConsole()
        print(Fore.RED + "Invalid link" + Style.RESET_ALL)
        time.sleep(2)
        DownLoadSubPage()

    #DisplayVideoInfo(video)
    Menu.SelectionMenu(f"Title: {Video.title} \n        Views: {Video.views} \n        Length: {Video.length}\n\n        Is this the video you want to download?", 
        [
            Menu.MenuOption("Yes", lambda: FormatSelection(Video)),
            Menu.MenuOption("No", DownloadPage),
        ]
    ).display()

def FormatSelection(video: YouTube):
    #print all resolutions
    Menu.SelectionMenu("Select the format you want to download", 
        [
            Menu.MenuOption("Video", lambda: VideoDownloader.Youtube_Downloader(video, "mp4")),
            Menu.MenuOption("Audio", lambda: VideoDownloader.Youtube_Downloader(video, "mp3")),
            Menu.MenuOption("Go back", DownloadPage)
        ]
    ).display()

#-----------------RESOLUTION SELECTION-----------------#For future use, need to add a way to get all the resolutions because of youtube's adaptive streaming
def ResolutionSelection(video : YouTube):
    #Clearconsole.clearConsole()
    #print("Getting available resolutions...")

    options=[
        Menu.MenuOption("360p", lambda: VideoDownloader.Youtube_Downloader(video, "mp4", "360p")),
        Menu.MenuOption("720p", lambda: VideoDownloader.Youtube_Downloader(video, "mp4", "720p")),
        #add go back and exit option
        Menu.MenuOption("Home", Home.homescreen),
        Menu.MenuOption("Go back to download page", DownloadPage),
        Menu.MenuOption("Exit", exit),
    ]
    
    Menu.SelectionMenu("Select the resolution you want to download", 
        options
    ).display()
    
#-----------------Playlist-----------------#
def DownloadPlaylist():
    Link = input("Enter the link for the playlist you want to download: ")
    Playlist = VideoDownloader.GetPlaylistInfo(Link)
    #DisplayPlaylistInfo(Playlist)
    Menu.SelectionMenu(f"Title: {Playlist.title} \n        Views: {Playlist.views} \n        Length: {Playlist.length}\n\n        Is this the playlist you want to download?", 
        [
            Menu.MenuOption("Yes", lambda: FormatSelection(Playlist)),
            Menu.MenuOption("No", DownloadPage),
        ]
    ).display()


