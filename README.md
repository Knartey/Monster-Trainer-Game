# Monster Trainer Game

A text-based Pokémon-style adventure where players explore, catch, and train creatures, then engage in turn-based battles.  
Developed as part of INST326: Object-Oriented Programming – Fall 2025.

## Overview

Monster Trainer Game is a command-line role-playing game (RPG) built in Python. Players can:
- Catch unique monsters using capture items
- Train and level them up to increase strength
- Battle wild opponents using strategic turn-based combat
- Heal and manage their team between encounters

The project demonstrates Object-Oriented Programming (OOP) principles:
- Classes and objects (Monster, Move, Item, Player)
- Encapsulation of state and behavior
- Polymorphism through varied monster abilities and item effects
- Modular design for readability and scalability

## How to run the game

### Step 1: Clone the repository
```bash
git clone https://github.com/Knartey/Monster-Trainer-Game.git
cd Monster-Trainer-Game
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Start the game
```bash
python main.py
```

Follow the on-screen prompts:
- Enter your trainer name
- Receive a starter monster
- Encounter wild monsters
- Battle, heal, and attempt captures
- Manage your team and inventory

## Game features

- Catch & train monsters – Build a unique team of creatures
- Turn-based battles – Use moves, plan attacks, and defeat opponents
- Random encounters – Wild monsters appear dynamically
- Item system – Heal HP, restore PP, or attempt captures with Monster Balls
- Team management – Add, remove, and view monsters and inventory
- Battle outcomes – Critical hits and type effectiveness matter
- Reset after encounters – Monsters regain HP and PP for fairness

## OOP concepts demonstrated

- Classes & Objects – Monster, Move, Item, Player encapsulate game entities
- Encapsulation – Each class manages its own state and behavior
- Polymorphism – Different monsters and items behave uniquely
- Modular design – Organized files for clarity and maintainability
- Testing – Comprehensive pytest suite ensures correctness and edge case handling

## Technologies used

- Python 3.x
- pytest (for tests)
- random (for wild encounter and battle randomness)

## Project structure

```text
Monster-Trainer-Game/
│
├── main.py            # Entry point and game loop
├── monster.py         # Monster class (HP, level, moves, combat)
├── move.py            # Move class (PP, power, type effectiveness)
├── item.py            # Item class (healing, PP restore, capture items)
├── player.py          # Player class (team and inventory management)
│
├── test_game.py       # Pytest test suite (covers all classes and edge cases)
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

## Running tests

We use pytest to verify behavior of all classes and edge cases.

```bash
# Run the full test suite
pytest -v

# Run a specific test file
pytest -v test_game.py

# Run a single test by name
pytest -v -k "test_move_creation_and_pp_methods"
```

## Contributors

Developed by:
- Ahmed Sachit
- Kabutey Nartey
- Daniel Camacho-Lopez
- James Lieske

For INST326: Object-Oriented Programming – Fall 2025

## Video presentation

A short demo and walkthrough of gameplay and design will be linked here after recording:  
[Video Link – to be added soon]

## Future development ideas

- Expand monster roster and abilities
- Add map navigation (North, South, East, West)
- Implement save/load progress system
- Introduce boss battles and advanced leveling
- Add graphical interface using tkinter or pygame
- Enable multiplayer or online duels

## Team development guide

For setup and Git workflow instructions (pull, push, sync, virtual environment setup), see TEAM_GUIDE.md.

## License

This project is for educational purposes as part of the University of Maryland INST326 course.  
Feel free to fork and build upon it for learning and experimentation.

## Tagline

“Catch. Train. Battle. Evolve.”  
A simple but powerful showcase of teamwork and Python OOP design.
