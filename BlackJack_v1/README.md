# 🃏 Blackjack Game (CLI Version)

A command-line Blackjack game implemented in Python, featuring object-oriented design, betting mechanics, and basic casino-style gameplay against a dealer.

---

## 📌 Overview

This project simulates a simplified version of Blackjack where a human player competes against a dealer. The game includes:

- Card deck generation and shuffling  
- Player betting system  
- Hit/Stand decision flow  
- Dealer logic  
- Score calculation with Basic Ace handling  (limitd support for multiple Aces)
- Balance tracking across rounds  

---

## 🎮 How to Play

1. Run the script in a Python environment.
2. Enter your name and starting balance.
3. Place a bet at the beginning of each round.
4. Receive two cards.
5. Choose:
   - **H (Hit)** → draw another card  
   - **S (Stand)** → end your turn  
6. Dealer plays automatically after you stand.
7. Outcome is determined:
   - Bust (>21) loses
   - Closest to 21 wins
   - Blackjack (21) is recognized
8. Continue playing or add more funds.

---

## 🧠 Skills Demonstrated

### 🧩 Object-Oriented Programming (OOP)
- Custom classes:
  - `Player`
  - `Card`
  - `DeckOfCards`
- Encapsulation of game logic within objects

---

### 🔁 Control Flow & Game Loops
- Nested loops for:
  - Game rounds
  - Player decisions
- Conditional branching for:
  - Win/loss scenarios
  - Input validation

---

### 🎲 Data Structures
- **Tuples** → suits and ranks  
- **Dictionaries** → card values  
- **Lists** → player and dealer hands  

---

### 🎯 Algorithmic Thinking
- Card dealing system using `.pop()`
- Score calculation with conditional Ace values (1 or 11)
- Dealer decision-making logic

---

### 🛡️ Input Validation & Error Handling
- `try/except` blocks for:
  - Numeric input (bets, balance)
- Loop-based validation for user choices

---

## 👤 Author
Created as a learning project to practice python fundementals and game logic design.

## ⚠️ Known Limitations
* Ace handling is simplified and may not cover all edge cases
* Deck is not reshuffled dynamically after depletion
* Game logic and display are tightly coupled
* No support for advanced Blackjack rules:
* Split
* Double down
* Insurance