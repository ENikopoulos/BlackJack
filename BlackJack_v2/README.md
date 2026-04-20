# 🃏 Blackjack Game (Tkinter GUI Version)

A graphical Blackjack game built with Python and Tkinter, featuring an improved game engine, proper card handling, and a user-friendly interface.

---

## 📌 Overview

This project is a GUI-based implementation of Blackjack where a player competes against a dealer. It improves upon a basic CLI version by introducing:

- A graphical interface using Tkinter  
- A more structured game engine  
- Proper Blackjack rules (Ace handling, dealer behavior)  
- Automatic deck reshuffling  
- Real-time game state updates  

---

## 🎮 Features

- 🖥️ **Graphical User Interface (GUI)** using Tkinter  
- 🃏 **Dynamic card dealing system**  
- ♠️ **Accurate hand value calculation with Ace adjustment**  
- 🎯 **Blackjack detection (2-card 21)**  
- 💥 **Bust detection for player and dealer**  
- 🔄 **Automatic deck reshuffling when low on cards**  
- 🎲 **Dealer follows standard rule (hits until 17)**  
- 💰 **Balance tracking system**  
- 🔒 **Round state management (prevents invalid actions)**  
- 🎭 **Hidden dealer card during gameplay**  

---

## 🧠 Skills Demonstrated

### 🧩 Object-Oriented Programming (OOP)
- Classes used:
  - `Card`
  - `Deck`
  - `Hand`
  - `BlackjackGUI`
- Clear separation of responsibilities between components

---

### 🎲 Data Structures
- **Tuples** → suits and ranks  
- **Dictionaries** → card values  
- **Lists** → deck and hands  

---

### 🔁 Control Flow & Game Logic
- Conditional logic for:
  - Hit / Stand decisions  
  - Win / loss / push outcomes  
- Dealer AI logic (draw until 17)  
- Round lifecycle management  

---

### 🧮 Algorithmic Thinking
- Dynamic hand value calculation  
- Multi-Ace adjustment strategy  
- Game outcome evaluation  

---

### 🖼️ GUI Development
- Built with `tkinter`
- Widgets used:
  - `Label`
  - `Button`
- Event-driven programming (button callbacks)

---

### 🔄 State Management
- Tracks:
  - Player balance  
  - Current bet  
  - Game state (`game_over`)  
- Controls flow between rounds  

---

### 🔀 Randomization
```python
import random
random.shuffle(deck)