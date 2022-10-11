from Backend import Downloader
from Frontend import Home

def DownloadPage():
    print("Welcome to the download page")
    print("Enter the link of the video you want to download")
    print("Enter 1 to go back to the homescreen")
    print("Enter 2 to exit")
    Link = input("Enter the link of the video: ")

    if Link == "1":
        Home.homescreen()
    elif Link == "2":
        exit()
    else:
        print("Downloading...")
        Downloader.Youtube_Downloader(Link)
