command = ""

while True:
    command = input("> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped...")
    elif command == "help":
        print("""
Start - to start car
Stop - to stop car
Quit - to end game
        """)
    elif command == "quit":
        break
    else:
        print("Wrong command")