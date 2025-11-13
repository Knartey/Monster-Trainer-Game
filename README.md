# README.md
# Monster-Trainer-Game

Monster Trainer Game
A Pokémon-style command-line adventure where players explore, catch, and battle monsters!
________________________________________
Overview
Monster Trainer is a Python-based, text adventure game inspired by the Pokémon series.
Players take on the role of a monster trainer who explores a virtual world, encounters wild creatures, catches them, trains them, and engages in turn-based battles.
The project demonstrates object-oriented programming (OOP) principles in Python including classes, inheritance, encapsulation, and polymorphism to create an interactive and replay able experience.
________________________________________
Key Features
•	Exploration System – Move through different zones and discover wild monsters.
•	Monster Capture – Use capture items to catch wild creatures and expand your team.
•	Turn-Based Battles – Each monster has unique stats, abilities, and elemental attacks.
•	Training & Leveling Up – Win battles to earn experience and make your monsters stronger.
•	Story Progression – Follow a light storyline as you explore and unlock new areas.
•	Save/Load System (optional or planned) – Resume your adventure later.
________________________________________
Object-Oriented Design
This project is structured around multiple interacting classes to model a realistic game system.
Main Classes
Class	Description	Example Methods
Trainer	Represents the player who can own and manage monsters.	catch_monster(), battle(), heal_team(), view_team()
Monster	Defines the stats, moves, and behaviors of each monster.	attack(), take_damage(), level_up(), is_fainted()
Battle	Handles turn-based combat logic between monsters.	start_battle(), player_turn(), enemy_turn(), determine_winner()
Each class includes at least 8 methods, including constructors (__init__) and special methods for custom string representations and comparisons.
________________________________________
Testing
All testing for this project is done using pytest.
The test suite (test_game.py) includes:
•	Object creation tests (Trainer, Monster, Battle)
•	Method behavior tests (attacks, healing, leveling)
•	Edge cases (HP boundaries, invalid inputs, empty teams)
•	Integration tests for class interaction
To run all tests:
pytest
All tests must be passed successfully before final submission.
________________________________________
How to Run the Game
1.	Clone the repository:
2.	git clone https://github.com/Knartey/Monster-Trainer-Game.git
3.	cd Monster-Trainer-Game
4.	(Optional) Create a virtual environment and install dependencies:
5.	python -m venv venv
6.	source venv/bin/activate    # or venv\Scripts\activate on Windows
7.	pip install -r requirements.txt
8.	Run the game:
9.	python main.py
10.	Enter your name and begin your journey!
Gameplay Tips:
•	Catch monsters to build your team.
•	Choose wisely during battles: each monster has unique abilities.
•	Heal your team between battles to stay ready.
________________________________________
________________________________________
Note:
Update Your Local Copy for the Project Team
If You Already Cloned the Repository Before
You do not need to delete your local folder.
Instead, you can update it by pulling the latest version from GitHub.
Option 1: Update Your Existing Local Repo (Recommended)
1.	Open your project folder in VS Code.
2.	Open the built-in terminal (Ctrl + ` ).
3.	Make sure you’re on the correct branch (usually main or master):
4.	git branch
5.	Pull the latest updates:
6.	git pull origin main
(Replace main with your branch name if different.)
This will automatically download all recent commits, including README changes, new code, or added files.
________________________________________
Option 2: If You Have Merge Conflicts or Old Uncommitted Code
If you tried editing locally and it causes conflicts (Git won’t let you pull), you have two choices:
A. Commit or stash your work before pulling
git add .
git commit -m "My local changes"
git pull origin main
or stash temporarily:
git stash
git pull origin main
git stash pop
B. If your local version is messy or outdated and you don’t need it:
Delete and re-clone the repo cleanly:
cd ..
rm -rf Monster-Trainer-Game
git clone https://github.com/Knartey/Monster-Trainer-Game.git

This gives you a fresh start with the latest version.
________________________________________
Quick Tip for Teams
When multiple people are committing:
•	Always pull before pushing:
•	git pull origin main
(Fix any conflicts, then)
git push origin main
•	Commit small, frequent updates with clear messages.
This keeps everyone’s local copies in sync and avoids overwriting each other’s changes.
________________________________________
Technologies Used
•	Python 3.x
•	pytest – for automated testing
•	colorama – for colored text output
•	random – for wild encounters and battle randomness
•	text-based CLI – all game interactions are through the console
________________________________________
Future Improvements
•	Add a map navigation system (North, South, East, West)
•	Include more monster types and elemental classes
•	Implement a save/load feature
•	Add background music or sound effects
•	Introducing multiplayer battles
•	Create a graphical version using tkinter or pygame
________________________________________
Team Members
Developed by:
Ahmed Sachit, Kabutey Nartey, Daniel Camacho-Lopez, & James Lieske
For INST326: Object-Oriented Programming – Fall 2025
________________________________________
Video Presentation
A short demo and explanation of the game’s design, functionality, and OOP principles are available here:
[Video Link – to be added after recording]
________________________________________
Repository Structure
Monster-Trainer-Game/

•	main.py                   # Entry point for the game
•	trainer.py                # Trainer class definition
•	monster.py                # Monster class definition
•	battle.py                 # Battle logic and interactions
•	tests/
o	test_game.py          # Pytest test suite
•	requirements.txt          # Project dependencies
•	README.md                 # Project documentation
________________________________________
License
This project is for educational purposes as part of the INST326 course.
Feel free to fork and build upon it for learning and experimentation.
