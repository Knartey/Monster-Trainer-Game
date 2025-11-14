# README.md
#  Monster Trainer Game

A Pokémon-style adventure where players can explore, catch, and train creatures, then engage in turn-based battles.  
Developed as part of **INST326: Object-Oriented Programming – Fall 2025**.

---

##  Overview

**Monster Trainer Game** is a text-based role-playing game (RPG) built in Python.  
Players can:
- Catch unique monsters
- Train them to increase strength
- Battle opponents using strategic turn-based combat
- Heal and manage their team between battles

The game demonstrates **Object-Oriented Programming (OOP)** principles, including classes, inheritance, and modular design.

---

##  How to Run the Game

### Step 1: Clone the Repository

git clone https://github.com/Knartey/Monster-Trainer-Game.git
cd Monster-Trainer-Game

Step 2: Install Dependencies

If you don’t have the required packages installed, run:

pip install -r requirements.txt

Step 3: Start the Game
python main.py


Then follow the on-screen prompts:

Enter your trainer name

Catch and train monsters

Battle opponents

Heal and level up your team

 Game Features

 Catch & Train Monsters – Build a unique team of creatures.
 Turn-Based Battles – Use skills, plan attacks, and defeat opponents.
 Random Encounters – Wild monsters appear dynamically.
 Save/Load System (coming soon) – Persistent progress between sessions.
 Colorful Text Output – Using the colorama library.

 OOP Concepts Demonstrated

Classes & Objects (Monster, Trainer, Battle)

Encapsulation – Data and behavior contained in each class

Inheritance – Shared properties across monster types

Polymorphism – Different monsters with unique abilities

Modular Design – Organized files for readability and scalability

 Technologies Used

Python 3.x

colorama – Colorful terminal text

pytest – Unit testing framework

random – Wild encounter and battle randomness

 Project Structure
Monster-Trainer-Game/
│
├── main.py                # Game entry point
├── trainer.py             # Trainer class
├── monster.py             # Monster class
├── battle.py              # Battle logic and interactions
│
├── tests/
│   └── test_game.py       # Automated pytest file
│
├── requirements.txt       # Python dependencies
├── README.md              # Public documentation (this file)
└── TEAM_GUIDE.md          # Internal team setup instructions

 Contributors

Developed by:
Ahmed Sachit
Kabutey Nartey
Daniel Camacho-Lopez
James Lieske

 For INST326: Object-Oriented Programming – Fall 2025

 Video Presentation

A short video demo and walkthrough of gameplay and design will be linked here after recording:
 [Video Link – to be added soon]

 Future Development Ideas

Expand monster roster and abilities

Add map navigation (North, South, East, West)

Implement save/load progress system

Introduce boss battles and leveling system

Add graphical interface using tkinter or pygame

Enable multiplayer or online duels

 Team Development Guide

For setup and Git workflow instructions (pull, push, sync, virtual environment setup), see:
 TEAM_GUIDE.md

 License

This project is for educational purposes as part of the University of Maryland INST326 course.
Feel free to fork and build upon it for learning and experimentation.

 “Catch. Train. Battle. Evolve.”

A simple but powerful showcase of teamwork and Python OOP design.


---

