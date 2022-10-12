import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))
import Frontend.Menu as Menu
from Frontend.Downloadpage import DownloadPage
from colorama import Fore, Back, Style


#add welcome to youtube downloader homescreen and add a button to go to the download page

def homescreen():
    Menu.SelectionMenu("Home", [
        Menu.MenuOption("Download", DownloadPage),
        Menu.MenuOption("Settings (WIP)", "Settings" ),
        Menu.MenuOption(Fore.RED + "Exit" , exit)
    ]
    ).display()
    #Homescreen.display()