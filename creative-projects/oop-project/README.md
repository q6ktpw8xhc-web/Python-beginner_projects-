# Fantasy Battle System

A small Python project created to practice and combine the four core Object-Oriented Programming (OOP) concepts:

* **Encapsulation**
* **Inheritance**
* **Polymorphism**
* **Abstraction**

## Project Overview

This project simulates a simple fantasy battle system with three character types:

* Warrior — swings a sword
* Mage — casts a spell
* Archer — shoots an arrow

All three character types inherit common functionality from the `Character` parent class while implementing their own attack behavior.

## OOP Concepts Demonstrated

### 1. Encapsulation

The character's health is stored using a private attribute:

```python
self.__health
```

The health cannot be accessed directly from outside the class. Instead, methods such as `take_damage()`, `heal()`, and `get_health()` control how the health is changed or accessed.

The health is also protected by rules:

* Health cannot go below `0`.
* Health cannot go above `100`.

### 2. Inheritance

`Warrior`, `Mage`, and `Archer` inherit from the `Character` class:

```python
class Warrior(Character):
class Mage(Character):
class Archer(Character):
```

This allows the child classes to share functionality provided by the parent class.

### 3. Polymorphism

Each character class implements its own version of `attack()`:

```python
fighters = [Warrior("Thor" , 100) , Mage("Merlin" , 100) , Archer("Robin" , 100)]


for fighter in fighters:
    fighter.attack()
    
```

The same method name produces different behavior depending on the object.

### 4. Abstraction

`Character` is an abstract base class using Python's `ABC` module.

The `attack()` method is marked with `@abstractmethod`, meaning subclasses must provide their own implementation.

```python
@abstractmethod
def attack(self):
    pass
```

This defines what every character must be able to do while allowing each character to decide how the attack works.

## Example Output

```text
Thor swings sword
Merlin casts a spell
Robin shoots arrow

Thor's health went down by: 150
Thor's remaining health: 0
Thor's health increased by: 200
Thor's remaining health: 100
```

## What I Practiced

Through this project, I practiced:

* Creating classes and objects
* Abstract base classes
* Abstract methods
* Inheritance
* Method overriding
* Polymorphism
* Private attributes using `__`
* Getters and controlled access
* Data validation
* Lists of objects
* Iterating through objects and calling methods

## Technologies

* Python 3
* Object-Oriented Programming
* `abc` module

## Status

Completed as a Python OOP learning project.
