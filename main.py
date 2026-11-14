import random
import sys
from dataclasses import dataclass
from functools import total_ordering
from turtle import heading

@total_ordering
@dataclass
class PositiveNumber:
    number: int

    def __str__(self):
        return f"${self.number}"

    def __post_init__(self):
        if self.number < 0:
            raise ValueError("You're out of PositiveNumber!")
    
    def __neg__(self):
        return PositiveNumber(-self.number)

    def __iadd__(self, other):
        amount = other.number if isinstance(other, PositiveNumber) else other
        self.number += amount
        return self

    def __isub__(self, other):
        amount = other.number if isinstance(other, PositiveNumber) else other
        if self.number - amount < 0:
            raise ValueError("You're out of PositiveNumber!")
        self.number -= amount
        return self

    def __lt__(self, other):
        if not isinstance(other, PositiveNumber):
            return NotImplemented
        return self.number < other.number

    def __gt__(self, other):
        if not isinstance(other, PositiveNumber):
            return NotImplemented
        return self.number > other.number

opponent_health = 20
player_health = 20
player_PositiveNumber = PositiveNumber(20)
player_gun = 5
opponent_gun = 5
opponent_start_health = 20
round_number = 0

player_name = input(str("Please enter your name to start Potato Shooter!\n"))

print(f"Welcome to Potato Shooter," , player_name , "!")
print("--------------------------------------------------------------------------------")
print("You start with $20, 20 health, and a pistol")
print("Your opponenet has 20 health and the same pistol.")
print("--------------------------------------------------------------------------------")

while True:
    round_number += 1
    opponent_health = opponent_start_health
    print(f"Round {round_number}: the opponent has {opponent_health} health!")

    while opponent_health >= 1:
        

        action = input(str("What would you like to do? Shoot? Dodge? Or buy?\n")).strip().lower()
        print("--------------------------------------------------------------------------------")

        match action:
            case "buy":
                op_shot_hit = random.randint(1,5)
                if op_shot_hit != 1:
                    player_health -= 5
                    print(f"The opponent hit you!, you have", player_health, "health left!")
                    print("--------------------------------------------------------------------------------")
                shop = input(str("What would you like to buy?\nHealth Potion-------------$10\nBetter Gun----------$30\nShield---------$30\n")).strip().lower()
                try:
                    match shop:
                        case "health potion":
                            player_PositiveNumber -= 10   # raises if you can't afford it
                            player_health += 10
                            print("Ok, you get +10 health!")
                            print(f"You now have {player_PositiveNumber} and {player_health} health!")

                        case "better gun":
                            player_PositiveNumber -= 30
                            player_gun += 5
                            opponent_gun += 5
                            print("Ok, you get plus five damage!")
                        case "shield":
                            player_PositiveNumber -= 30
                            player_health += 20
                            print("Ok, you get a shield, +20 health!")
                        case _:
                            print("We don't sell that.")
                        
                except ValueError:
                    print("You can't afford that, broke boy")
                        
            case "shoot":
                shot_hit = random.randint(1,5)
                op_shot_hit = random.randint(1,5)
                if op_shot_hit != 1:
                    player_health -= 5
                    print(f"The opponent hit you! You have {player_health} health left!")
                else:
                    print("The opponent missed!")
                if shot_hit != 1:
                    opponent_health -= player_gun
                    print(f"You hit the opponent! He has {max(opponent_health, 0)} health left!")
                else:
                    print("You missed!")

            case "dodge":
                print("You dodged opponent's bullet!")

            case "quit":
                print("Thanks for playing!")
                sys.exit(0)
            case _:
                print("Not a valid action. Choose shoot, dodge, buy, or quit.")
        if opponent_health <= 0:
            print("You Win! :)\nYou get $10 dollars as a reward!")
            opponent_start_health += 5
            player_PositiveNumber += 10
            break

        if player_health <= 0:
            print("You Lost. :(")
            sys.exit(0)
