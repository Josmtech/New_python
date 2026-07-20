import random


def moving_target_game():
    print("=== WELCOME TO THE MOVING TARGET GUESSING GAME! ===")
    print("Rules: Guess a number between 1 and 10.")
    print("CRITICAL TWIST: The secret number CHANGES after EVERY guess!\n")

    attempts = 0
    while True:
        # The secret number changes every iteration
        secret_number = random.randint(1, 10)
        attempts += 1

        try:
            user_input = input(f"Attempt #{attempts} -> Guess (1-10) or 'q' to quit: ")
            if user_input.lower() == "q":
                print(f"Thanks for playing! You made {attempts - 1} attempts.")
                break
            guess = int(user_input)
        except ValueError:
            print("❌ Invalid input!")
            attempts -= 1
            continue

        if guess == secret_number:
            print(f"🎉 AMAZING! You got it! It was {secret_number}.")
            break
        else:
            print(f"❌ Missed! The number was {secret_number}. It has changed!\n")


if __name__ == "__main__":
    moving_target_game()
