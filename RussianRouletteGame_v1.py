#help needed : the intended funtion is that after the gun becomes empty then it reloads again but it always relode itself after each player truns so please help me to fix it

import random
def load():
    """Prepares a gun for a round of Russian Roulette.

    This function simulates loading a six-chamber revolver with a random assortment of blanks and live bullets.
    A list is used to represent the gun's chamber, where '0' signifies a blank cartridge and '1' indicates a live bullet.
    The function randomly assigns either a blank or a live bullet to each of the six chambers.

    Returns:
        tuple: A tuple containing three elements:
            - list: The gun's chamber, represented as a list of 0s and 1s.
            - int: The total count of blank cartridges in the chamber.
            - int: The total count of live bullets in the chamber.
    """
    gun = []
    for i in range(6):
        bullet = random.randint(0,1)
        gun.append(bullet)
    b = gun.count(0)
    f = gun.count(1)
    return gun,b,f #gun is the main list and b is blank count and 1 is bullet count

def PvP():
    """Manages a Player-versus-Player (PvP) game of Russian Roulette.

    This function facilitates a two-player game where participants take turns shooting.
    Each player begins with 5 health points, and the objective is to be the last one standing.
    A player loses the game when their health reaches zero. The gun is reloaded after each turn,
    and the number of blanks and live bullets is displayed at the start of each round.

    Players have two choices on their turn:
    1. Shoot themselves: If the chamber contains a blank, they are safe and can continue their turn.
       If it's a live bullet, they lose one health point, and their turn ends.
    2. Shoot their opponent: A blank results in a missed shot, ending their turn.
       A live bullet deals one damage to the opponent, also ending the turn.

    The game concludes when one player's health is depleted, at which point the other player is declared the winner.

    Raises:
        ValueError: If a player enters non-integer input when prompted to make a choice.
    """
    try:
        print("welcome to PvP mode!!")
        p1 = input("enter player 1 name:")
        p2 = input("enter player 2 name:")
        print("\n\n")
        p1_h = 5 #player 1 health
        p2_h = 5 #player 2 health
      # whoevers health will become 0 first will loose ; each bullet cause 1 damage
        while True:
            gun,b,f = load()
            print(f"No. of Blanks:{b}\nNo. of Full:{f}\n") # loading gun list , and printing the bullet and blank count
            while True:
                print(f"{p1}'s turn:")
                play = int(input(f"1. To Shoot Yourself Enter 1\n2. To Shoot {p2} Enter 2:\n"))
                if play == 1:
                    if gun[0]==0:
                        print("puff....(blank shot)")
                        gun.remove(0)
                        continue
                    elif gun[0]==1:
                        print("BANG!!!!!!\nYOU GOT SHOT!!")
                        p1_h -= 1
                        print(f"{p1} health = {p1_h}")
                        gun.remove(1)
                        break
                elif play == 2:
                    if gun[0]==0:
                        print("puff....(blank shot)")
                        gun.remove(0)
                        break
                    elif gun[0]==1:
                        print(f"BANG!!!!!!\n{p2} GOT SHOT!!")
                        p2_h -= 1
                        print(f"{p2} health = {p2_h}")
                        gun.remove(1)
                        break
        
            print(f"\n\n{p1} health = {p1_h}")
            print(f"{p2} health = {p2_h}\n\n")
            if p1_h == 0:
                print(f'{p2} wins!!')
                
                break
            elif p2_h == 0:
                print(f'{p1} wins!!')
                break
            
            while True:
                print(f"{p2}'s turn:")
                play = int(input(f"1. To Shoot Yourself Enter 1\n2. To Shoot {p1} Enter 2:\n"))
                if play == 1:
                    if gun[0]==0:
                        print("puff....(blank shot)")
                        gun.remove(0)
                        continue
                    elif gun[0]==1:
                        print("BANG!!!!!!\nYOU GOT SHOT!!")
                        p2_h -= 1
                        print(f"{p2} health = {p2_h}")
                        gun.remove(1)
                        break
                elif play == 2:
                    if gun[0]==0:
                        print("puff....(blank shot)")
                        gun.remove(0)
                        break
                    elif gun[0]==1:
                        print(f"BANG!!!!!!\n{p1} GOT SHOT!!")
                        p1_h -= 1
                        print(f"{p1} health = {p1_h}")
                        gun.remove(1)
                        break
                    
            print(f"\n\n{p1} health = {p1_h}")
            print(f"{p2} health = {p2_h}\n\n")
            if p1_h == 0:
                print(f'{p2} wins!!')
                dead = True
                break
            elif p2_h == 0:
                print(f'{p1} wins!!')
                dead = True
                break
    except ValueError:
        print("enter correctly!!")
    
def PvE():
    """Placeholder for a Player-versus-Environment (PvE) game mode.

    This function is intended to house the logic for a single-player version of Russian Roulette,
    where the player would compete against an AI opponent. Currently, this mode is not implemented.
    """
    pass

def main():
    """Serves as the main entry point for the Russian Roulette game.

    This function presents the player with the main menu, where they can choose between different game modes.
    The available options are Player-versus-Player (PvP), Player-versus-Environment (PvE), or exiting the game.
    It continuously prompts the user for input until they decide to quit.

    The menu options are:
    1. PvP: Initiates a two-player game.
    2. PvE: A placeholder for a single-player mode against an AI (currently not implemented).
    3. Quit: Terminates the game application.

    The function is designed to handle invalid inputs, such as non-integer values,
    and will prompt the user to enter a correct choice.
    """
    mFlag = True
    while mFlag == True:
        
        
        print("welocome to Russian Roulette!!")
        try:
            flag = int(input("1. For PvP enter 1\n2. For PvE enter 2(coming soon)\n3. To quit enter 3:\n"))
            match flag:
                case 1:
                    PvP()
                case 2:
                    PvE()
                case 3:
                    quit()
                case _:
                    print("enter correctly!")
        except ValueError:
                print("enter correctly!\n")
main()
