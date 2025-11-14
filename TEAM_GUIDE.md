# TEAM_GUIDE.md

#  Monster Trainer Game – Team Guide (Internal)

**For Team Use Only — Not part of the public README**

This guide explains how team members can clone, run, and update the project safely in VS Code.  
Follow these steps to stay synced and avoid Git issues.

---

##  How to Run the Game

### Step 1: Clone the Repository

```
git clone https://github.com/Knartey/Monster-Trainer-Game.git
cd Monster-Trainer-Game
```

### Step 2 (Optional): Create a Virtual Environment & Install Dependencies

```
python -m venv venv
```

**Activate it:**

* On macOS/Linux:

  ```
  source venv/bin/activate
  ```
* On Windows:

  ```
  venv\Scripts\activate
  ```

Then install all required packages:

```
pip install -r requirements.txt
```

### Step 3: Run the Game

```
python main.py
```

Then follow the on-screen prompts:

* Enter your name to begin
* Catch and train monsters
* Battle opponents and level up your team
* Heal your monsters between battles

---

##  Updating Your Local Copy (for Team Members)

If you already cloned the repository before, you **do not need to delete your local folder**.

### Option 1: Update Your Existing Local Repo ( Recommended)

1. Open your project folder in VS Code.
2. Open the terminal (`Ctrl + ``).

Check your branch:

```
git branch
```

Pull the latest updates:

```
git pull origin main
```

This downloads all recent commits, including README updates, new code, or added files.

---

### Option 2: If You Have Merge Conflicts or Old Uncommitted Code

If Git shows merge conflicts or errors:

**A. Commit or stash your work before pulling:**

```
git add .
git commit -m "My local changes"
git pull origin main
```

**Or stash temporarily:**

```
git stash
git pull origin main
git stash pop
```

**B. If your local copy is messy or outdated and you don’t need it:**

```
cd ..
rm -rf Monster-Trainer-Game
git clone https://github.com/Knartey/Monster-Trainer-Game.git
```

---

##  Team Workflow Tips

When multiple people are committing:

Always pull before pushing:

```
git pull origin main
```

Then push your changes:

```
git push origin main
```

 Commit **small, frequent updates** with clear messages.
This keeps everyone’s work in sync and prevents overwriting each other’s code.

---

##  Technologies Used

* **Python 3.x**
* **pytest** – for automated testing
* **colorama** – for colored text output
* **random** – for wild encounters and battle randomness
* **Text-based CLI** – all game interactions are through the console

---

##  Future Improvements

* Add a map navigation system (North, South, East, West)
* Include more monster types and elemental classes
* Implement a save/load feature
* Add background music or sound effects
* Introduce multiplayer battles
* Create a graphical version using `tkinter` or `pygame`

---

##  Team Members

Developed by:
**Ahmed Sachit**, **Kabutey Nartey**, **Daniel Camacho-Lopez**, & **James Lieske**
*For INST326: Object-Oriented Programming – Fall 2025*

---

##  Video Presentation

A short demo and explanation of the game’s design, functionality, and OOP principles will be added here once recorded:
 [Video Link – to be added after recording]

---

##  Repository Structure

```
Monster-Trainer-Game/
│
├── main.py                # Entry point for the game
├── trainer.py             # Trainer class definition
├── monster.py             # Monster class definition
├── battle.py              # Battle logic and interactions
│
├── tests/
│   └── test_game.py       # Pytest test suite
│
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

##  License

This project is for educational purposes as part of the **INST326** course.
Feel free to fork and build upon it for learning and experimentation.

````

---

