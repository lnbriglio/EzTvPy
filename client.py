# V 1.0
# Imports
from config import Configuration
from show import *

# Load/Create config
config = Configuration()

# Load shows
sm = ShowManager()
myShowsList = sm.retrieveShowList()

entry = "";

print("Welcome to eztv dwnldr config manager")
print("Press -h to see available commands")

def process_entry(args):

    if args.startswith("-h"):
        print("-l   List stored shows")
        print("-a   To add a new show")
        print("-rm  To Delete a show by name")
        print("q    To Quit")

    if args.startswith("-l"):
        for s in myShowsList:
            print(s.toString())
    if args.startswith("-a"):
        name = input("Enter show name: ")
        is720 = input("Is 720p (y/n): ").lower() == "y"
        newShow = Show(name, is720)
        myShowsList.append(newShow)
        sm.updateShowList(myShowsList)
    if args.startswith("-rm"):
        name = input("Enter the name of the show to remove: ")
        print(sm.removeByName(myShowsList,name))


while(entry.lower() != "q") and (entry.lower() != "quit"):
    entry = input("Eztv dwnldr> ")
    process_entry(entry)




