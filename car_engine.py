#enter start to start engine
#enter stop to stop engine
#enter quit to exit

engine_status = input("Enter keyword: ")
engine_status.lower()

while engine_status != "quit":
    if engine_status == "start":
        print("Car started")
        break
    elif engine_status == "stop":
        print("Cart stopped")
        break
    elif engine_status == "help":
        print("""
Start - to start the car
Stop - to stop the car
Quit - to exit
        """)
        break
    else:
        print("You entered wrong command")
        break