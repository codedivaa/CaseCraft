# 🕵️ CaseCraft

> A cozy detective mystery game built with Python and Pygame where players explore a small town, gather clues, interrogate suspects, and solve criminal cases.

---

## ✨ Overview

CaseCraft is a 2D detective adventure game developed using Python and Pygame.

Players take on the role of a detective investigating a mysterious museum theft. By exploring the town, talking to NPCs, collecting clues, and analyzing witness statements, players must identify the true culprit and solve the case.

Each playthrough features a randomly selected criminal, creating a unique mystery experience every time.

---

## 🎮 Gameplay

### Objective

Investigate the Museum Theft case and identify the correct suspect.

### How to Play

1. Explore the town using movement controls.
2. Approach NPCs and interact with them.
3. Collect witness statements and clues.
4. Analyze the information gathered.
5. Select the suspect you believe committed the crime.
6. Make your accusation and solve the case.

---

## 🕹 Controls

| Key   | Action                  |
| ----- | ----------------------- |
| W     | Move Up                 |
| A     | Move Left               |
| S     | Move Down               |
| D     | Move Right              |
| E     | Talk to NPCs            |
| 1     | Select Bob              |
| 2     | Select Sarah            |
| 3     | Select Guard            |
| 4     | Select Owner            |
| SPACE | Accuse Selected Suspect |

---

## 🔍 Current Features

* Player movement system
* NPC interaction system
* Dynamic clue collection
* Dialogue system
* Multiple suspects
* Random criminal generation
* Case-solving mechanic
* Simple detective gameplay loop
* Modular project architecture

---

## 🏛 Current Case

### Museum Theft

A priceless painting has vanished from the town museum.

The suspects include:

* Bob
* Sarah
* Guard
* Owner

Talk to everyone, collect evidence, and discover who is lying.

---

## 🧠 Game Loop

```text
Explore Town
      ↓
Talk to NPCs
      ↓
Collect Clues
      ↓
Analyze Statements
      ↓
Select Suspect
      ↓
Accuse
      ↓
Win / Lose
```

---

## 🏗 Project Architecture

```text
CaseCraft/
│
├── main.py
│
├── entities/
│   ├── player.py
│   └── npc.py
│
├── ui/
│   └── dialogue.py
│
├── cases/
│   └── case_manager.py
│
└── assets/
```

### Components

#### Player System

Responsible for:

* Movement
* Collision detection
* Interaction range

#### NPC System

Responsible for:

* Character behavior
* Dialogue delivery
* Clue distribution

#### Dialogue System

Responsible for:

* Conversation rendering
* UI display
* Interaction feedback

#### Case Manager

Responsible for:

* Case generation
* Criminal selection
* Clue assignment
* Win/Lose validation

---

## ⚙️ Tech Stack

### Language

* Python 3

### Framework

* Pygame

### Concepts Used

* Object-Oriented Programming (OOP)
* Game Loops
* Collision Detection
* Event Handling
* State Management
* Modular Architecture

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/codedivaa/CaseCraft.git
cd CaseCraft
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the game:

```bash
python main.py
```

---

## 📦 Requirements

Create a file named `requirements.txt`

```text
pygame
```

Or install manually:

```bash
pip install pygame
```

---

## 🌱 Future Improvements

* Pixel-art character sprites
* Town map and buildings
* Museum crime scene
* Detective notebook system
* Inventory and evidence collection
* Multiple case types
* AI-generated mysteries
* Procedural NPC dialogue
* Save and load system
* Sound effects and background music

---

## 📸 Preview

```text
🏛 Museum
👮 Detective
🧑 Witnesses
🔍 Clues
🕵️ Investigation
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* Python programming
* Pygame development
* Object-Oriented Design
* Game architecture
* Interactive systems
* Event-driven programming
* State management

---

## 👩‍💻 Author

Developed by codedivaa

Built with Python, curiosity, and a love for mystery games.
