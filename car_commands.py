command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
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