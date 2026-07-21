#enter start to start engine
#enter stop to stop engine
#enter quit to exit
from _pyrepl import commands

command = input("Enter keyword: ")
command.lower()


while command != "quit":
    if command == "start":
        print("Car started")
        break
    elif command == "stop":
        print("Cart stopped")
        break
    elif command == "help":
        print("""
Start - to start the car
Stop - to stop the car
Quit - to exit
        """)
        break
    else:
        print("You entered wrong command")
        break