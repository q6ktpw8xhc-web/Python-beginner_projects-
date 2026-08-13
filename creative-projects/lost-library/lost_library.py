# Lost Library
title = " THE LOST LIBRARY "

header = title.center(80, "*")
print(header)


class Character:
    def __init__(self , name , health):
        self.name = name
        self.health = health

    def show_status(self):
        if self.health > 100:
            self.health = 100
        print(f"{self.name}'s health point: {self.health}")
        
    def move(self):
        print(f"{self.name} is moving through the library...")

class Player(Character):
    def __init__(self, name, health=100):
        super().__init__(name, health)
        self.health = min(health, 100)
        self.keys = 0
        self.books = []
        self.ancient_door_solved = False
        self.librarian_test_passed = False

    def show_status(self):
        if self.health > 100:
            self.health = 100
        print(f"{self.name}'s health point: {self.health}")

    def move(self):
        print(f"{self.name} moves carefully through the library, watching for traps.")

    def collect_key(self):
        self.keys += 1
        print(f"You found a golden key! Keys:{self.keys}")

    def collect_books(self, title):
        self.books.append(title)
        print(f"You collected:{self.books}")

    def inventory(self):
        print("******** INVENTORY *****************")
        print(f"Health: {self.health}")
        print(f"Books : {self.books}")
        print(f"Keys :  {self.keys}")
        print("***********************************")
          
class Librarian(Character):
    def __init__(self, name, health=100):
        super().__init__(name, health)

class Book:
    def __init__(self, title, color,pages):
        self.title = title
        self.color = color
        self.pages = pages

class StoryBook(Book):
    def __init__(self ,title , color, pages):
        super().__init__(title , color, pages)


class HealingBook(Book):
    def __init__(self, title, color,pages):
        super().__init__(title, color, pages)


class ClueBook(Book):
    def __init__(self, title, color, pages):
        super().__init__(title, color, pages)


class KeyBook(Book):
    def __init__(self, title, color, pages):
        super().__init__(title, color, pages)


class MapBook(Book):
    def __init__(self , title , color, pages):
        super().__init__(title, color, pages)

user_input = input("Press Enter to begin your adventure ")
user_name = input("\nEnter name:")
def welcome_message():
    story = StoryBook("Ancient Lore", "blue", 100)
    print(f"You encounter a mysterious book {story.title} that reads:  ")
    print()
    print(f"'Welcome, {user_name}, to the Lost Library!")
    print("Deep within the forgotten mountains lies an ancient library filed with megical hidden secrets.")
    print("Many explores have searched for it's treasures.")
    print("None have ever returned.")
    print("Will you be the one to uncover the mysteries of the Lost Library?'")
def intro():
    print("\nThe library doors creak open...")
    print("A cold wind rushes past you.")
    print("Legends say the library was cursed after a forbidden spell was read.")
    print("\nYour mission: Find the hidden key and escape before the curse consumes you.")
    user_input = input("\nPress Enter to enter the library:")
def enter_library():
    print("\nYou step deeper into the library, the air thick with ancient dust.")
    print("Shelves of strange books tower around you, and a distant glow draws your attention.")
    print()

def discover_story_book(player):
    story = StoryBook("Ancient Lore", "blue", 100)
    print(f"\nYou discover a glowing story book titled '{story.title}'.")
    print("The book whispers secrets from a forgotten age.")
    print()
    player.collect_books(story.title)
    print()
def library_map(player):
    while True:
        print("\n Where would you like to go")
        print("1. Story Room")
        print("2. Hall")
        print("3. Healing Room")
        print("4. Puzzle Room")
        print("5. Acient Archive")
        print("6. Exit")
        print("7. Check Inventory")

        choice = input("Enter your choice(1-7):")

        if choice == "1":
            Story_Room(player)

        elif choice == "2":
           Hall(player)

        elif choice == "3":
           Healing_Room(player)

        elif choice == "4":
           Puzzle_Room(player)

        elif choice == "5":
            Ancient_Archive(player)

        elif choice == "7":
            check_inventory(player) 

        elif choice == "6":
            print("Thanks for playing!")
        else:
            print("Invalid choice.")
            player.show_status()


def Story_Room(player):
    story = StoryBook("Ancient Lore", "blue", 100)
    print("\nYou enter a dusty room...")
    print("The room is full with books .")
    print(f"{story.title} : Beware this room has trap")
    print("A bookshelf suddely falls!")
    while True:
        print("1. Dodege")
        print("2. Hide")
        print("3. push it away")

        correct = int(input("Enter the correct option : "))
        if correct == 3:
                print(f"\n{story.title} You got it right")
                print()
                print("You push the bookshlef away and a hidden passage appears")
                return Hall(player)
        else:
            print("Oops you choice the wrong option")
            print("\nThe curse drains your health by 20 percent")
            player.health -= 20
            player.show_status()

            user_input = input("\nPress Enter to continue the game:")
            return Hall(player)

def Hall(player):
    Clue = ClueBook("Shadow Clue", "red", 100)
    Keys = KeyBook("Ser Keys" , "green" , 100)
    print(f"\nYou find a glowing magic key book that reavels the key's location")
    print(f"{Keys.title} , whispers: 'The key lies where shadows dance.'")
    print()
    story = StoryBook("Ancient Lore", "blue", 100)
    player.collect_books(Clue.title)
    player.collect_books(Keys.title)
    print()
    while True:
        print("1.Left Hall")
        print("2. Dark Corridor")
        print("3. Ancient Archive")

        choice = int(input("Enter choice:"))

        if choice == 2 :
            print("\nThe door is locked")
            print("You need a golden key")
            print("You move your hand around in the dark and found a golden key")
            print(f"{story.title} , you got it")
            print()
            player.collect_key()
            print()
            user_input = input("Press Enter to move to the next stage . your are almost there:")
            print()
            return Healing_Room(player)
        else:
            print("Wrong choice , The curse drains your health.")
            print()
            player.health -= 10
            player.show_status()
            if player.health <= 0:
                player.show_status()
                print("You are out of health")
                print("Game over")
                return
            else:
                input("Press Enter to continue the game:")
                return Healing_Room(player)

def Healing_Room(player):
    Healing = HealingBook("Healing Light", "blue", 100)
    story = StoryBook("Ancient Lore", "blue", 100)
    Clue = ClueBook("Shadow Clue", "red", 100)
    print()
    player.collect_books(Healing.title)
    print(f"\n{story.title} in this room you will find the Healing Book. This book will restore your health")
    print()
    print(f"{Clue.title}... Whispers ... The book is somewhere around something big")
    while True:
        print("1. Search shelf")
        print("2. Look under table")
        print("3. Open chest")
    
        choice = int(input("\nEnter choice:"))
        if choice == 3:
            print(f"\n{story.title}, You found the {Healing.title}")
            print()
            print("The chest open and you saw a glowing blue book and when you touched it your energy got restored by 20 percent:")
            print()
            player.health += 20
            player.show_status()
            print()
            input("Press Enter to continue :")
            return Puzzle_Room(player)
        else:
            print("\nopps you did not get")
            player.health -= 10
            player.show_status()
            if player.health <= 0:
                print("You are out of health")
                print("Game over")
                welcome_message()
                return
            else:
              input("Press Enter to continue the game")
            return Puzzle_Room(player)


def Puzzle_Room(player):
    story = StoryBook("Ancient Lore", "blue", 100)
    print(f"{story.title} , Welcome Explorer to the Puzzle Room in this you have to answer 3 riddle questions")
    print()
    print("If you get all correct you move to the next stage of the game ")
    print()
    print(" You are almost at the end , brave explorer ")
    print()
    questions = [
            {
                "question": "The more of them you take , the more you leave behind?",
                "choices": [
                    "a) Footsteps",
                    "b) A treasure chest",
                    "c) A memory",
                ],
                "answer": "a",
            },
            {
                "question": "I look at you, you look at me. I raise my right, you raise your left?",
                "choices": [
                    "a) Water",
                    "b) A mirror",
                    "c) Shadow",
                ],
                "answer": "b",
            },
            {
                "question": "I have a heart that dose not beat ,and a mouth that does not speak . I burry gold but never buy?",
                "choices": [
                    "a) A coffin",
                    "b) A treasure chest",
                    "c) Gold Coins",
                ],
                "answer": "b",
            },
        ]
    
    all_correct = True
    for question in questions:
            print(question["question"])
            print()
            for choice in question["choices"]:
                print(choice)
                print()
            user_answer = input("Enter Choice: ").strip().lower()
            if user_answer == question["answer"]:
                print("\n Correct!")
                print()
                player.health += 5
            else:
                print("Incorrect.")
                print()
                all_correct = False
                player.health -= 20
                print()
                if player.health <= 0:
                    print("You are out of health : Game Over")
                    print()
                    break
                else:
                    player.show_status()
                    print(f"You have {player.health} left.")
                print()
            user_input = input("Press Enter to continue the game")
    return Ancient_Archive(player)

def check_inventory(player):
    player.inventory()
    return library_map
            
story = StoryBook("Ancient Lore", "blue", 100)
locate = MapBook("Mapy", "green", 100)
Clue = ClueBook("Shadow Clue", "red", 100)
def Ancient_Archive(player):               
    player.collect_books(locate.title)
    print(f"\n{locate.title} , ohh you are very close")
    print()
    print(f"You look around and discover a locked magical wooden door ")
    print()
    print("The locked magic door has three symbols on it.")
    print()
    print(f"{story.title} , You need to choose the right symbol to progress , you have 3 attempts if you choose the wrong symbol the curse will drain your energy")
    print()
    print(f"{Clue.title} ,  Gave you a clue .... 'I rise every morning , disappear every night, and give light to the world.'")
    while True:
        print("1. Triangle")
        print("2. Moon")
        print("3. Sun")
        answer = "3"
        attempts_allow = 3
        for attempt in range(1, attempts_allow +1):
            print()
            guess = input(f"Enter your attempt {attempt}: ")
            if guess == answer:
              print(f"\n{story.title} , you got it right")
              print("The big wooden magic door opens")
              print()
              player.ancient_door_solved = True
              player.show_status()
              return librarian_encounter(player)
            else:
                reamning = attempts_allow - attempt
                if reamning > 0:
                    print(f"Incorrect. you have {reamning} left.")
                else:
                    print("All attempts are used")
                    print(f"{story.title} , you chose the wrong symbol")
                    print("The curse drain your energy")
                    player.health -= 10
                    player.show_status()
                    return librarian_encounter(player)

def librarian_encounter(player):
    print("\nA mysterious librarian appears!")
    print()
    print("She asks you a riddle:")
    print("\n'I have a body , but i can be found in a library. I have no voice , yet i can speak to you.")
    print("I have no feet , yet i can take you to places you have never been.")
    print("The more you open me , the more you discover.'")
    print()
    print("What am i?")
    print()
    answer = "book"
    answer1 = input("Your answer: ")
    if answer1 == answer:
        print("\nCorrect. You may continue.")
        player.librarian_test_passed = True
        user_input = input("\nPress Enter:")
        return choose_the_truth(player)
    else:
        print("Wrong! The curse drains your health.")
        print()
        player.health -= 10
        player.show_status()
        return choose_the_truth(player)

def choose_the_truth(player):
    print("\nThe Librarian ask you somthing you discover in the library")
    print()
    print("'Which book first revealed the history of this library'?")
    while True:
        print("1. The Healing Book")
        print("2. The Ancient Lore")
        print("3. The Map Book")

        anws = "2"

        choice = input("\nEnter choice:")
        if choice == anws:
            print("Correct . You may continue.")
            print()
            user_input = input("Press Enter")
            player.show_status()
            return final_door(player)
        else:
            print("Incorrect. The curse drains your energy")
            player.health -= 10
            player.show_status()
            return final_door(player)
    
def final_door(player):
    Keys = KeyBook("Ser Keys" , "green" , 100)
    print("\nYou enter a secret room...")
    print()
    print(f"{Keys.title} , Whispers... A golden key lies on a pedestal.")
    print()
    player.collect_key()
    print()
    print("The librarian reveals:")
    print()
    print("'The key will open the door....but it will also realse the curse.'")
    while True:
        print("1. Take the key and escape")
        print("2. Stay and break the curse")
        print("3. Ask the librarian for the truth") 

        choice = input("\nEnter choose:")
        if choice == "1":
            print("\nYou escape the library , but behind you , the ancient doors slowly close")
            print()
            print("The curse remains")
            print()
            print("Final Stats:")
            print(f"Health remaining: {player.health}")
            print(f"Books collected: {player.books}")
            print(f"Keys collected: {player.keys}")
            print("Would you like to play again?")
            yes = input("Enter 'yes' or 'no': ").strip().lower()
            if yes == "yes":
                print()
                welcome_message()
                return
            elif yes == "no":
                print("Thank You for playing")
                break
            
        elif choice == "2":
            print("The librarian ,'You choose to break the curse , You will forever be remembered as a hero.")
            print("But you need certain conditions to break the curse...")
            print("Complete all the requirements to break the curse.'")
            choice = input("\nPress Enter")
            all_correct = (
                player.ancient_door_solved 
                and story.title in player.books
                and Clue.title in player.books
                and player.librarian_test_passed 
                and player.health >= 50
            )
            if all_correct:
               print("\nYou place the migical books around the ancient seal")
               print()
               print("The librarian begins chanting the forgotten words")
               print()
               print("The walls shake . The books fly from their shelves")
               print()
               print("Suddenly , the curse shatters.")
               print()
               print("The library becomes slient for the first time in centuries.")
               print()
               print("The librarian smiles and slowly fades away.")
               print()
               print("The lost library is finally free.")
               print()
               print("Final Stats:")
               print(f"Health remaining: {player.health}")
               print(f"Books collected: {player.books}")
               print(f"Keys collected: {player.keys}")
               print("Would you like to play again?")
               yes = input("Enter 'yes' or 'no': ").strip().lower()
               if yes == "yes":
                print()
                welcome_message()
                return
               elif yes == "no":
                print("Thank You for playing")
                break
            else:
                print("\nMust complete all the requirements to break the curse. ")
                print("You faild to break the curse")
                print()
                print("Final Stats:")
                print(f"Health remaining: {player.health}")
                print(f"Books collected: {player.books}")
                print(f"Keys collected: {player.keys}")
                print("Would you like to play again?")
                yes = input("Enter 'yes' or 'no': ").strip().lower()
                if yes == "yes":
                    print()
                    welcome_message()
                    return
                elif yes == "no":
                    print("Thank You for playing")
                    break


        elif choice == "3":
           print("You ask the librarian for the truth about the library and the curse.")
           print()
           print("The librarian finally reavels:")
           print("'You belive this library has been keeping you trapped ....but that was never it's purpose.")
           print("The librarian reveals that she is but a prisoner of the curse herself.")
           print("The magic books weren't created to help people escape, They were created to find someone capable of breaking the curse.'")
           print()
           print("You realizes that you were brought to the library on purpose")
           print()
           print("The librarian disppears , leaving behind one final message")
           print()
           print("'The library chose you.'")
           print()
           print("You walk deeper into the library.")
           print()
           print("The doors close behind you ")
           print()
           print("But this time you were not afraid")
           print()
           print("SECRET ENDIND UNLOCKED")
           print("'The Library Chose You'")
           print()
           print("Final Stats:")
           print(f"Health remaining : {player.health}")
           print(f"Books collected: {player.books}")
           print(f"Keys collected: {player.keys}")
           print()
           print("Would you like to play again?")
           yes = input("Enter 'yes' or 'no': ").strip().lower()
           if yes == "yes":
               print()
               welcome_message()
               return
           elif yes == "no":
                print("Thank You for playing")
                break
        else:
            if player.health <= 0:
                print("You are out of health")
                print("Game over")
                welcome_message()
                return
        
welcome_message()
player1 = Player(user_name, 100)
print()
player1.show_status()

intro()
enter_library()
discover_story_book(player1)

library_map(player1)


