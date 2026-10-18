# Haunted Treasure Door/ Door of luck

import random

print("Welcome to the Haunted Treasure Door!")
print("You are about to enter a mysterious room with three doors. Behind one of these doors lies a treasure, while the other two doors hide traps. Choose wisely!")

correct_door = random.randint(1, 3)  # Randomly select the correct door (1, 2, or 3) 

choice = int(input("Choose a door (1, 2, or 3): "))  # Get the user's choice of door

if choice == correct_door:
    print("Congratulations! You found the treasure!")
elif choice == 1 or choice == 2 or choice == 3:
    print("Oh no! You fell into a trap! Better luck next time.")
else:
    print("Invalid choice. Please choose a door number between 1 and 3.")

print("Computer Choice :", correct_door)  # Reveal the correct door for transparency