---

# TEAM_GUIDE.md

## Git Workflow Cheat Sheet (For Team Members)

To avoid conflicts and keep our codebase stable, **follow this daily workflow**:

---

##  Daily Workflow

```bash
# 1. Pull latest changes before starting work
git pull origin main

# 2. Make your changes and test them
python main.py        # run the game interactively
pytest -v test_game.py  # run the test suite

# 3. Stage and commit with a clear message
git add .
git commit -m "For example: Add new monster class with fire abilities"

# 4. Push your changes
git push origin main
```

---

##  If You See Merge Conflicts

### **Option A: Commit or stash your changes**

Commit your local progress:
```bash
git add .
git commit -m "Save local changes"
git pull origin main
```

**OR** stash temporarily:
```bash
git stash
git pull origin main
git stash pop
```

### **Option B: Start fresh (if your local copy is outdated or broken)**

```bash
cd ..
rm -rf Monster-Trainer-Game
git clone https://github.com/Knartey/Monster-Trainer-Game.git
```

---

##  Best Practices

* Always **pull before pushing** to avoid conflicts.  
* **Commit often** with clear, descriptive messages.  
* **Test before pushing** to keep `main` stable.  
* **Communicate** with the team about major changes (new systems, refactors, file moves, etc.).  

---

##  Running Tests with Pytest

We use `pytest` to ensure all classes (`Monster`, `Move`, `Item`, `Player`) and the game logic behave correctly.

### Run the full test suite:
```bash
pytest -v
```

### Run a specific test file:
```bash
pytest -v test_game.py
```

### Run a single test function:
```bash
pytest -v -k "test_move_creation_and_pp_methods"
```

### Notes:
- Always run tests **before pushing** to confirm stability.  
- Tests cover both **happy-path scenarios** and **edge cases** (e.g., no PP left, invalid indices, fainted monsters).  
- If a test fails, fix the issue locally before committing.  

---


