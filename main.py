
# --------- # -- Spin the Landmarks 🎰 -- # --------- #

# Add short delays to simulate natural program response
import time

import random

# Shuffle the symbols and return a new row
def spin(items):
    shuffled_items = random.sample(items, len(items))
    return shuffled_items


# ------------------ # -- Main -- # ----------------- #

# Store each landmark with its name and a short fact
landmarks = {
    "🏜": {
        "name": "Pyramids of Giza",
        "fact": "Built over 4,500 years ago in Egypt!"
    },
    "🕋": {
        "name": "Kaaba",
        "fact": "Located in Mecca, the holiest site in Islam."
    },
    "🏰": {
        "name": "Citadel of Aleppo",
        "fact": "One of the oldest and largest castles in the world!"
    },
    "🗼": {
        "name": "Eiffel Tower",
        "fact": "One of the most recognizable landmarks in Paris."
    },
    "🏛": {
        "name": "Petra",
        "fact": "Famous ancient rock-cut architecture in Jordan."
    }
}

divider = " # " + "-" * 45 + " # "

coins = 100
spin_cost = 20
reward = 50

print("🌟 Welcome to the Historical Landmark Slot Game! 🌟")

# Get the landmark symbols from the dictionary keys
symbols = list(landmarks)

# Show the available symbols
print(f' - | {" | ".join(symbols)} | - ')

print(f"💰 Balance: {coins} coins")
print(f"🎰 Spin Cost: {spin_cost} coins")
print(divider)

input("- Press Enter to play..")


# Keep playing while there are enough coins for a spin
while coins >= spin_cost:

    # Store all winning columns
    wins = []

    # Pay for the spin
    coins -= spin_cost

    # Simulate the spinning animation
    for dots in range(3):
        print(
                f'\r🎰 Spinning the reels.{dots * ".":<2}',
                end="",
                flush=True
             )
        time.sleep(0.7)

    print(f"\n{divider}")

    # Generate three shuffled rows
    row1 = spin(symbols)
    row2 = spin(symbols)
    row3 = spin(symbols)

    # Display the rows gradually
    print(f'   -$ {" | ".join(row1)} $-')
    time.sleep(0.75)

    print(f'   -$ {" | ".join(row2)} $-')
    time.sleep(0.7)

    print(f'   -$ {" | ".join(row3)} $-')
    time.sleep(0.6)

    print(divider)

    # Check each column for three matching symbols
    for i in range(len(symbols)):
        if row1[i] == row2[i] == row3[i]:
            winning_column = i + 1

            landmark_title = landmarks[row1[i]]["name"]
            landmark_fact = landmarks[row1[i]]["fact"]

            wins.append((winning_column, landmark_title, landmark_fact))

    # Handle winning or losing results
    if wins:
        rewards = reward * len(wins)
        coins += rewards

        print(f"🎉 YOU WIN {rewards} COINS! 🎉")

        # Display information about each winning column
        for col, title, fact in wins:
            print(f"--> 🏆 Column {col}: {title}")
            print(f"ℹ️ Info: {fact}")
        print(divider)

    else:
        print("❌ You Lost!")

    time.sleep(0.7)
    print(f" 💰 Balance: {coins} coins")
    time.sleep(0.6)
    print(f" 🎰 Spin Cost: {spin_cost} coins")
    time.sleep(0.5)
    print(divider)

    # Ask whether the player wants another spin
    while coins >= spin_cost:
        time.sleep(0.6)

        print("- Play Again?")
        time.sleep(0.5)
        play_again = input(" -> Press enter or ('n' to quit)..").lower().strip()

        if play_again not in ("", "n"):
            print(" ⚠️ Invalid input, press enter or ('n' to quit).")
            print(divider)
        else:
            break

    # Stop when there are not enough coins for another spin
    if coins < spin_cost:
        break

    # Stop when the player chooses not to continue
    elif play_again == "n":
        time.sleep(0.3)
        print(" 🎮 Game Over, Thanks for playing! 👋")
        break

    print(divider)


# Show a message when the player runs out of coins
if coins < spin_cost:
    time.sleep(0.6)
    print("💸 Game Over! You've run out of coins.")

# ---------------------------------------------------- #