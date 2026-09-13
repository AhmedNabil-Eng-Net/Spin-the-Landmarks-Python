# 🎰 Spin the Landmarks

A simple command-line slot game built with Python, featuring famous historical landmarks from around the world.

## ✨ Features

* 🎰 Spin three rows of landmark symbols
* 💰 Start with coins and pay for each spin
* 🏆 Win rewards by matching landmarks in the same column
* 📚 Learn a short fact about each winning landmark
* 🔄 Keep playing while you have enough coins
* ⚠️ Validate the play-again input

## 🎮 How to Play

The game starts with a balance of coins and a fixed cost for each spin.

Press **Enter** to start the game.

Each spin generates three shuffled rows of landmark symbols:

```text
   -$ 🏜 | 🏰 | 🕋 | 🏛 $-
   -$ 🕋 | 🏜 | 🏛 | 🏰 $-
   -$ 🏜 | 🏜 | 🏛 | 🏛 $-
```

If the same landmark appears in the same column across all three rows, you win a reward.

For example:

```text
   -$ 🏜 | 🏰 | 🕋 | 🏛 $-
   -$ 🏜 | 🕋 | 🕋 | 🏰 $-
   -$ 🏜 | 🏰 | 🕋 | 🏛 $-
```

Here, the first and third columns are winning columns.

The game then displays the landmark name and a short fact about it.

## 🪙 Game Rules

* Each spin costs **20 coins**
* Each winning column rewards **50 coins**
* Multiple winning columns can earn multiple rewards
* The game ends when you choose to stop or don't have enough coins for another spin

## 🛠️ Technologies & Concepts

* Python
* Dictionaries
* Nested Dictionaries
* Lists
* Tuples
* Functions
* `random.sample()`
* Loops
* Conditional Statements
* Input Validation
* String Formatting
* Basic Game State Management

## 🚀 How to Run

Make sure Python is installed on your computer.

Run the game with:

```bash
main.py
```

## 📚 Learning Goal

This project was created to practice combining Python data structures, randomization, game logic, rewards, and simple interactive CLI design in one project.

## 👨‍💻 Author

 **Ahmed Nabil**
