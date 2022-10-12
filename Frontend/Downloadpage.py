import imp
import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))

import Frontend.Menu as Menu
import Frontend.Home as Home
import Backend.VideoDownloader as VideoDownloader
from pytube import YouTube

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
            Menu.MenuOption("Video", lambda: VideoDownloader.Youtube_Downloader(video, "mp4")),
            Menu.MenuOption("Audio", lambda: VideoDownloader.Youtube_Downloader(video, "mp3")),
            Menu.MenuOption("Go back", DownloadPage)
        ]
    ).display()

def ResolutionSelection(video):
    Menu.SelectionMenu("Select the resolution you want to download", 
        [
            #TODO add a way to get the resolutions
        ]
    ).display()

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