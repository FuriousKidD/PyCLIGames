# 🔢 Number Guessing Game (Python CLI)

This is a classic **Number Guessing Game** implemented as a **Command-Line Interface (CLI)** program in Python. 
The game challenges the player to guess a randomly selected number within a specified range, providing hints and a leaderboard to track the best scores.

---

## 📸 Screenshots

> To be added soon

---

## 🔧 Features

- 🎯 **Random Number Generation**: The computer selects a number between 1 and 100 by default.
- 📉 **Hint System**: The player receives feedback—"Too high" or "Too low"—after each guess.
- 🎮 **Custom Difficulty**: Users can specify the minimum and maximum bounds for the guessing range.
- ⏱️ **Guess Limit**: Optional limit on number of guesses per game (e.g., 10 attempts).
- 🏆 **Leaderboard / Best Score Tracking**:
  - Tracks the fewest number of attempts needed to guess correctly.
  - Displays best score at the end of each session.
  - Accessible from the **menu system**.

---

## 📚 How It Works

1. **Game Start**: User sets the number range (or uses default 1–100).
2. **Guessing Loop**:
   - The game gives hints after each guess.
   - The number of attempts is tracked.
3. **Game Over**:
   - If guessed correctly: success message + attempt count.
   - If out of attempts: correct number is revealed.
4. **Leaderboard**:
   - Best attempt is stored during session.
   - Players can view the best score via the main menu.

---

## 🧭 Menu Options

- Start New Game
- View Instructions
- View Best Score (Leaderboard)
- Set Custom Range
- Exit

---

## 🛠️ Tech Stack

- **Language**: Python
- **Libraries Used**: `random`
- **Core Concepts**:
  - Loops & conditionals
  - Random number generation
  - User input validation
  - Session state tracking
  - Menu-based program flow
---

## ✅ To Run the Game
  In VSCode
```bash
python number_guessing_game.py
