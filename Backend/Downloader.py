from pytube import YouTube

#function that takes a youtube link and downloads it

#path will be the downloads folder
Download_Path = "C:\\Users\\Downloads"
yt = ""

def Youtube_Downloader(link):
    try:
        #object creation using YouTube which was #imported in the beginning
        #yt = YouTube(link)
        YouTube(link).streams.first().download(Download_Path)
    except:
        print("Connection Error")

    #filters out all the files with "mp4" extension
    mp4files = yt.filter('mp4')

    