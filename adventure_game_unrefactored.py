import time
import random
trolls =  random.choice(["dragon", "wicked fairie", "pirate", "gorgon", "wicked sorcerer"])
weapons = random.choice(["Sword", "Knife", "Sling"])
number = random.randint(2,5)
defence = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


while True:
    while True:
        print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
        print_pause(f"Rumor has it that there are {number} trolls somewhere around here, that have been terrifying the nearby village.")
        print_pause("In front of you is a house.")
        print_pause("To your right is a dark cave.")
        print_pause("In your hand you hold your trusty (but not very effective) dagger.\n")

        while True:
            print_pause("Enter 1 to knock on the door of the house.")
            print_pause("Enter 2 to peer into the cave.")
            print_pause("What would you like to do?")

            while True:
                first_choice = input("(Please enter 1 or 2.)\n")
                if first_choice == "1":
                    print_pause("You approach the door of the house.")
                    print_pause(f"You are about to knock when the door opens and out steps a {trolls}, one of the {number} trolls!")
                    print_pause(f"Eep! This is the {trolls}'s house!")
                    print_pause(f"The {trolls} attacks you!")
                    if weapons not in defence:
                        print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")
                    second_choice = input("Would you like to (1) fight or (2) run away?\n")
                    if second_choice == "1":
                        if weapons in defence:
                            print_pause(f"As the {trolls} moves to attack, you unsheath your new {weapons}.")
                            print_pause(f"The {weapons} of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
                            print_pause(f"The {trolls} takes one look at your shiny new toy and tries to wrestle it out of your hand.")
                            print_pause(f"A fight ensues and you hit the {trolls} {number} times!")
                            print_pause(f"Scared, the injured {trolls} runs away!")
                            print_pause(f"You have rid the town of the {trolls}. You are victoriuos!\n")
                        else:
                            print_pause("You do your best ...")
                            print_pause(f"but your dagger is no match for the {trolls}.")
                            print_pause("You have been defeated!\n")
                        print_pause("GAME OVER")
                        play_again = input("Would you like to play again? (y/n)\n")
                        if play_again == "n":
                            print_pause("Thanks for playing! See you next time.")
                            break
                        elif play_again == "y":
                            print_pause("Excellent! Restarting the game ...")
                            break
                    elif second_choice == "2":
                        print_pause("You run back into the field. Luckily, you don't seem to have been followed.\n")
                        break
                elif first_choice == "2":
                    print_pause("You peer cautiously into the cave.")
                    if weapons in defence:
                        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.\n")
                        break
                    else:
                        print_pause("It turns out to be only a very small cave.")
                        print_pause("Your eye catches a glint of metal behind a rock.")
                        print_pause(f"You have found the magical {weapons} of Ogoroth!")
                        print_pause(f"You discard your silly old dagger and take the {weapons} with you.")
                        defence.append(weapons)
                    print_pause("You walk back out to the field.\n")
                    break
            if play_again == "y":
                break
            if play_again == "n":
                break
        if play_again == "n":
                break
    if play_again == "n":
                break