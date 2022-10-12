
import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))
import Backend.Clearconsole as clearConsole

class SelectionMenu:
    def __init__(self, name, Options):
        self.name = name
        self.Options = Options

    def display(self):
        clearConsole.clearConsole()
        #show simple banner
        print(f"""
        -------------------------------------
        |         Youtube Downloader        |
        |             Welcome               |
        -------------------------------------
        {self.name}
        -------------------------------------
        """)
        self.showOptions()

    def showOptions(self):
        #show options
        for i in range(len(self.Options)):
            print(str(i+1) + ". " + self.Options[i].name)

        #get user input
        choice = input("Enter your choice: ")
        #check if input is valid
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= len(self.Options):
                self.select(choice)
            else:
                print("Invalid choice")
                self.display()

    def select(self, choice):
        self.Options[choice-1].function()

class MenuOption():
    def __init__(self, name, function):
        self.name = name
        self.function = function   


#testmenu = SelectionMenu("test", [MenuOption("test1", "test"), MenuOption("test2", exit)]).display()

