import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro(number):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that there are {number} trolls somewhere "
                "around here, that have been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def choices():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?\n")


def valid_input(prompt, options):
    while True:
        choice = input(prompt)
        for option in options:
            if choice == option:
                return choice
            elif choice == "quit":
                exit()


def house(trolls, weapons, number, defence):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens.")
    print_pause(f"Out steps a {trolls}. One of the {number} trolls!")
    print_pause(f"Eep! This is the {trolls}'s house!")
    print_pause(f"The {trolls} attacks you!\n")


def uncertainty(trolls, weapons, number, defence):
    if weapons not in defence:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.\n")


def cave(trolls, weapons, number, defence):
    print_pause("You peer cautiously into the cave.")
    if weapons in defence:
        print_pause("You've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.\n")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You have found the magical {weapons} of Ogoroth!")
        print_pause(f"You discard the silly old dagger and take the {weapons} "
                    "with you.")
        defence.append(weapons)
    print_pause("You walk back out to the field.\n")
    start_adventure(trolls, weapons, number, defence)


def fight(trolls, weapons, number, defence):
    if weapons in defence:
        print_pause(f"As the {trolls} moves to attack, "
                    "you unsheath your new weapon.")
        print_pause(f"The {weapons} of Ogoroth shines brightly in "
                    "your hand as you brace yourself for the attack.")
        print_pause(f"The {trolls} takes one look at your shiny new toy "
                    "and tries to wrestle it out of your hand.")
        print_pause(f"A fight ensues and you hit the {trolls} {number} times!")
        print_pause(f"Scared, the injured {trolls} runs away!")
        print_pause(f"You have rid the town of the {trolls}. "
                    "You are victorious!\n")
    else:
        print_pause("You do your best ...")
        print_pause(f"Your dagger is no match for the {trolls}, "
                    "but at least you live to fight another day.")
        print_pause(f"You may, one day, save your people from the trolls")
        print_pause("For today, you have been defeated!\n")
    print_pause("GAME OVER\n")
    play_again(trolls, weapons, number, defence)


def play_again(trolls, weapons, number, defence):
    choice = valid_input("Would you like to play again? (y/n)\n", ["y", "n"])
    if choice == "n":
        print_pause("Thanks for playing! See you next time.")
    elif choice == "y":
        print_pause("Excellent! Restarting the game ...\n")
        if weapons in defence:
            defence.remove(weapons)
        play_adventure_game()


def field(trolls, weapons, number, defence):
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.\n")
    start_adventure(trolls, weapons, number, defence)


def start_adventure(trolls, weapons, number, defence):
    choices()
    choice = valid_input("(Please enter 1 or 2)\n", ["1", "2"])
    if choice == "1":
        house(trolls, weapons, number, defence)
        uncertainty(trolls, weapons, number, defence)
        choice = valid_input("Would you like to (1) fight "
                             "or (2) run away?\n", ["1", "2"])
        if choice == "1":
            fight(trolls, weapons, number, defence)
        elif choice == "2":
            field(trolls, weapons, number, defence)
    elif choice == "2":
        cave(trolls, weapons, number, defence)


def play_adventure_game():
    trolls = random.choice(["dragon", "wicked fairie",
                            "pirate", "gorgon", "wicked sorcerer"])
    weapons = random.choice(["Sword", "Knife", "Sling"])
    number = random.randint(2, 5)
    defence = []
    intro(number)
    start_adventure(trolls, weapons, number, defence)


if __name__ == "__main__":
    play_adventure_game()
