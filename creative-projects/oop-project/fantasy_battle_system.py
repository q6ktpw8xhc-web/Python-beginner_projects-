# Combining Inheritance , Polymorphism , Encapsulation and Abstraction
# Fantasy Battle System
from abc import ABC , abstractmethod
class Character(ABC):
    def __init__(self ,name, health):
           self.name = name
           self.__health = health

    @abstractmethod
    def attack(self ):
        pass
    

    def take_damage(self , amount):
        if amount > 0:
           self.__health -= amount

           if self.__health < 0:
              self.__health = 0
           print(f"{self.name} , Health went down by : {amount}")

          

    def heal(self, amount):
        if amount > 0:
           self.__health = self.__health  + amount
           if self.__health > 100:
              self.__health = 100 
        print(f"{self.name}'s health increased by: {amount}")
    

    def get_health(self):
        print(f"{self.name}'s remaining health : {self.__health} ")
        return self.__health

class Warrior(Character):
    def attack(self):
        print("Thor  swings sword")

class Mage(Character):
    def attack(self):
        print("Merlin  casts a spell")

class Archer(Character):
    def attack(self):
        print("Robin shoots arrow")


fighters = [Warrior("Thor" , 100) , Mage("Merlin" , 100) , Archer("Robin" , 100)]


for fighter in fighters:
    fighter.attack()
print()
fighters[0].take_damage(150)
print(fighters[0].get_health())
fighters[0].heal(200)
print(fighters[0].get_health())
print()
fighters[1].take_damage(50)
print(fighters[1].get_health())
fighters[1].heal(20)
print(fighters[1].get_health())
print()
fighters[2].take_damage(70)
print(fighters[2].get_health())
fighters[2].heal(30)
print(fighters[2].get_health())





           
           

    



