import random

def load():#returns a list represnting a gun with 0 being a blank and 1 being a bullet
    gun = []
    for i in range(6):
        bullet = random.randint(0,1)
        gun.append(bullet)
    b = gun.count(0)
    f = gun.count(1)
    return gun,b,f #gun is the main list and b is blank count and 1 is bullet count

def PvP():
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
    pass

def main():
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
