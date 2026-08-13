# Lost Library

**Lost Library** is a text-based Python adventure game built to practice **Object-Oriented Programming (OOP)** concepts through an interactive story.

The player explores a mysterious library, collects magical books and keys, solves puzzles, interacts with a librarian, and makes choices that determine the ending.

##  Game Features

* Explore different areas of the Lost Library
* Collect and interact with magical books
* Player inventory system
* Health system
* Collect keys and solve locked areas
* Riddles and challenges
* Librarian encounter and tests
* Ancient Door challenge
* Player choices and branching paths
* Multiple endings
* Replay the game with different choices

## OOP Concepts Practiced

This project was built while learning Python Object-Oriented Programming.

### Inheritance

The game uses parent and child classes.

For example:

* `Character`

  * `Player`
  * `Librarian`

* `Book`

  * `StoryBook`
  * `HealingBook`
  * `ClueBook`
  * `KeyBook`
  * `MapBook`

### `super()`

Child classes use `super()` to initialize attributes inherited from their parent classes.

### Attributes

Objects store information such as:

* Player health
* Books collected
* Keys collected
* Book title
* Book color
* Number of pages

### Methods

Objects perform actions through methods such as:

* Exploring
* Collecting books
* Checking inventory
* Restoring health
* Giving clues
* Revealing key locations
* Showing distance
* Solving challenges

##  Multiple Endings

The player's decisions determine how the story ends.

###  Escape Ending

The player chooses to escape the Lost Library.

###  Hero Ending

The player successfully meets the requirements to break the library's curse.

Requirements include:

* Solving the Ancient Door
* Collecting the required magical books
* Passing the librarian's test
* Having at least 50 health

###  Secret Ending

The player chooses to discover the truth behind the Lost Library instead of simply escaping or breaking the curse.

##  Technologies

* **Python 3**
* Object-Oriented Programming
* Conditional statements
* Loops
* Functions
* Lists
* User input
* String methods

##  How to Run

Make sure Python is installed.

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project:

```bash
cd Lost-Library
```

Run the game:

```bash
python lost_library.py
```

##  Project Structure

```text
Lost-Library/
│
├── lost_library.py
└── README.md
```

##  What I Learned

Building Lost Library helped me practice combining multiple Python concepts into one complete project rather than learning each concept separately.

The main focus of this project was understanding how **classes, inheritance, `super()`, attributes, methods, and objects** can work together to create a larger program.

This project was also my first larger OOP-based adventure game.

##  Future Improvements

Possible future improvements include:

* Add a graphical interface
* Add images and animations
* Add sound effects and music
* Add more puzzles and rooms
* Add more characters
* Add save/load functionality
* Add more endings
* Improve the game map and navigation

---

**Project:** Lost Library
**Language:** Python
**Focus:** Object-Oriented Programming
