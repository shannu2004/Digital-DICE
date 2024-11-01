import random
import time

def roll_dice():
    print("Rolling the dice...", end="")
    for _ in range(3):  # Simple rolling animation with dots
        time.sleep(0.5)
        print(".", end="")
    print()
    
    dice_value = random.randint(1, 6)
    print(f"The dice rolled: {dice_value}")
    return dice_value

def main():
    print("Welcome to the Digital Dice Simulator!")
    while True:
        user_input = input("Press Enter to roll the dice or type 'q' to quit: ").strip().lower()
        if user_input == 'q':
            print("Goodbye!")
            break
        else:
            roll_dice()

if __name__ == "__main__":
    main()
