import imp
import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))

import Frontend.Menu as Menu
import Frontend.Home as Home
import Backend.Downloader as Downloader
from pytube import YouTube

def DownloadPage():
    Menu.SelectionMenu("Download", [
        Menu.MenuOption("Download video", DownLoadSubPage),
        Menu.MenuOption("Download playlist", ),
        Menu.MenuOption("Go home", Home.homescreen),
        Menu.MenuOption("Exit", exit)
    ]
    ).display()

def DownLoadSubPage():
    Link = input("Enter the link for the video you want to download: ")
    Video = Downloader.GetVideoInfo(Link)
    #DisplayVideoInfo(video)
    Menu.SelectionMenu(f"Title: {Video.title} \n        Views: {Video.views} \n        Length: {Video.length}\n\n        Is this the video you want to download?", 
        [
            Menu.MenuOption("Yes", lambda: FormatSelection(Video)),
            Menu.MenuOption("No", DownloadPage),
        ]
    ).display()

def FormatSelection(video):
    Menu.SelectionMenu("Select the format you want to download", 
        [
            Menu.MenuOption("Video", lambda: Downloader.Youtube_Downloader(video, "video")),
            Menu.MenuOption("Audio", lambda: Downloader.Youtube_Downloader(video, "audio")),
            Menu.MenuOption("Go back", DownloadPage)
        ]
    ).display()

def DownloadPlaylist():
    Link = input("Enter the link for the playlist you want to download: ")
    Playlist = Downloader.GetPlaylistInfo(Link)
    #DisplayPlaylistInfo(Playlist)
    Menu.SelectionMenu(f"Title: {Playlist.title} \n        Views: {Playlist.views} \n        Length: {Playlist.length}\n\n        Is this the playlist you want to download?", 
        [
            Menu.MenuOption("Yes", lambda: FormatSelection(Playlist)),
            Menu.MenuOption("No", DownloadPage),
        ]
    ).display()