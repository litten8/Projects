import random
rows=100
cols=100
tiletypes=["sand","rock","water","grass","dirt"]
enemytypes=[["slime", 30, 10, 0, ["water"]], ["ent", 50, 5, 5, ["water", "sand", "rock"]], ["piranha", 5, 25, 0, ["sand","rock","grass","dirt"]], ["zombie", 20, 20, 0, []]]
itemtypes=[["potion", 40, 0, 0, 0], ["armor", 0, 5, 0, 5], ["sword", 0, 0, 10, 0]]
terrain = [["" for c in range(cols)] for r in range(rows)]
enemies={}
items={}
for r in range(rows):
    for c in range(cols):
        terrain[r][c] = tiletypes[random.randint(0, len(tiletypes)-1)]
        if random.randint(1,8) == 8:
            enemyi=random.randint(0, len(enemytypes)-1)
            if not (terrain[r][c] in enemytypes[enemyi][4]):
                enemies[(r,c)] = enemytypes[enemyi]
        if random.randint(1,8) == 8:
            itemi=random.randint(0, len(itemtypes)-1)
            items[(r,c)] = itemtypes[itemi]
r=int(rows/2)-1
c=int(cols/2)-1
maxhp=100
hp=100
attack = 10
defense = 0
inventory=[["potion", 40, 0, 0, 0]]
while hp>0:
    print("You are standing on " + terrain[r][c] + ".")
    if (r,c) in enemies:
        print("There is a " + enemies[(r,c)][0] + " near you.")
    if (r,c) in items:
        print("There is a " + items[(r,c)][0] + " near you.")
    print("North is " + terrain[(r-1)%len(terrain)][c] + ".")
    if ((r-1)%len(terrain),c) in enemies:
        print("There is a " + enemies[(((r-1)%len(terrain),c))][0] + " north of you.")
    print("South is " + terrain[(r+1)%len(terrain)][c] + ".")
    if ((r+1)%len(terrain),c) in enemies:
        print("There is a " + enemies[(((r+1)%len(terrain),c))][0] + " south of you.")
    print("East is " + terrain[r][(c+1)%len(terrain[r])] + ".")
    if (r,(c+1)%len(terrain)) in enemies:
        print("There is a " + enemies[(r,(c+1)%len(terrain))][0] + " east of you.")
    print("West is " + terrain[r][(c-1)%len(terrain[r])] + ".")
    if (r,(c-1)%len(terrain)) in enemies:
        print("There is a " + enemies[(r,(c-1)%len(terrain))][0] + " west of you.")
    if (r,c) in enemies:
              print("The " + enemies[(r,c)][0] + " deals " + str(enemies[(r,c)][2]-defense) + " damage to you.")
              hp -= enemies[(r,c)][2]-defense
              print("You now have " + str(hp) + " health.")
    if hp>0:
        print("What would you like to do?(use n s e w to move, a to attack an enemy near you, t to take an item near you, u to use an item in your inventory)")
        command=input()
        if command == "n":
            r=(r-1)%len(terrain)
        elif command == "s":
            r=(r+1)%len(terrain)
        elif command == "e":
            c=(c+1)%len(terrain[r])
        elif command == "w":
            c=(c-1)%len(terrain[r])
        elif command == "a":
            if (r,c) in enemies:
                print("You attacked the " + enemies[(r,c)][0] + " dealing " + str(attack-enemies[(r,c)][3]) + " damage.")
                enemies[(r,c)][1] -= attack-enemies[(r,c)][3]
                if enemies[(r,c)][1]<=0:
                    print("You killed the " + enemies[(r,c)][0] + ".")
                    del enemies[(r,c)]
                else:
                    print("The " + enemies[(r,c)][0] + " now has  " + str(enemies[(r,c)][1]) + " health left.")
        elif command == "t":
            if (r,c) in items:
                print("You took the " + items[(r,c)][0] + ".")
                inventory.append(items[(r,c)])
                del items[(r,c)]
            else:
                print("There is item to take.")
        elif command == "u":
            if len(inventory) > 0:
                print("You have the following items in your inventory:")
                for i in range(len(inventory)):
                    print(inventory[i][0])
                print("What item would you like to use?")
                using=input()
                hasitem=False
                for i in range(len(inventory)):
                    if inventory[i][0] == using:
                        hasitem=True
                        usingi=i
                        break
                if hasitem:
                    print("You used a " + using + ".")
                    if inventory[usingi][1] > 0:
                        print("You gained " + str(inventory[usingi][1]) + " health.")
                        hp+=inventory[usingi][1]
                        if hp > maxhp:
                            hp=100
                        print("You now have " + str(hp) + " health.")
                    if inventory[usingi][2] > 0:
                        print("You gained " + str(inventory[usingi][2]) + " max health.")
                        maxhp+=inventory[usingi][2]
                        print("You now have " + str(maxhp) + " max health.")
                    if inventory[usingi][3] > 0:
                        print("You gained " + str(inventory[usingi][3]) + " attack.")
                        attack+=inventory[usingi][3]
                        print("You now have " + str(attack) + " attack.")
                    if inventory[usingi][4] > 0:
                        print("You gained " + str(inventory[usingi][4]) + " defense.")
                        defense+=inventory[usingi][4]
                        print("You now have " + str(defense) + " defense.")
                    del inventory[usingi]
                else:
                    print("You do not have a " + using + ".")
            else:
                print("You have no items.")
        else:
            print(command + " is not a valid command.")
    for k in list(enemies.keys()):
        if k[0] > r and not(((k[0]-1)%len(terrain),k[1]) in enemies) and not(terrain[(k[0]-1)%len(terrain)][k[1]] in enemies[k][4]):
            temp = enemies[k]
            del enemies[k]
            enemies[((k[0]-1)%len(terrain),k[1])]=temp
            k=((k[0]-1)%len(terrain),k[1])
        elif k[1] > c and not((k[0],(k[1]-1)%len(terrain)) in enemies) and not(terrain[k[0]][(k[1]-1)%len(terrain)] in enemies[k][4]):
            temp = enemies[k]
            del enemies[k]
            enemies[(k[0],(k[1]-1)%len(terrain))]=temp
            k=(k[0],(k[1]-1)%len(terrain))
        elif k[0] < r and not(((k[0]+1)%len(terrain),k[1]) in enemies) and not(terrain[(k[0]+1)%len(terrain)][k[1]] in enemies[k][4]):
            temp = enemies[k]
            del enemies[k]
            enemies[((k[0]+1)%len(terrain),k[1])]=temp
            k=((k[0]+1)%len(terrain),k[1])
        elif k[1] < c and not ((k[0],(k[1]+1)%len(terrain)) in enemies) and not(terrain[k[0]][(k[1]-1)%len(terrain)] in enemies[k][4]):
            temp = enemies[k]
            del enemies[k]
            enemies[(k[0],(k[1]+1)%len(terrain))]=temp
            k=(k[0],(k[1]+1)%len(terrain))
print("Game Over...")
