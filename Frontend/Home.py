from Downloadpage import Downloadpage

#add welcome to youtube downloader homescreen and add a button to go to the download page


def homescreen():
    print("Welcome to Youtube Downloader")
    print("Press 1 to go to the download page")
    print("Press 2 to exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        Downloadpage()
    elif choice == "2":
        exit()
    else:
        print("Invalid choice")
        homescreen()