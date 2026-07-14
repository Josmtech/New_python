secret_number = 5
guess_count = 0
guess_limit = 4

while guess_count < guess_limit:
    guess = int(input("Guess a number to play "))
    guess_count += 1
    print("Wrong, Try again!")
    if guess == secret_number:
        print("You Win")
        break
else:
    print("Sorry! you Lost")