#really buggy, fix catching
import random, math
pokeList = {
    "Caterpie": 255,
    "Weedle": 255,
    "Pidgey": 255,
    "Rattata": 255,
    "Spearow": 255,
    "Ekans": 255,
    "Sandshrew": 255,
    "Zubat": 255,
    "Oddish": 255,
    "Diglett": 255,
    "Meowth": 255,
    "Poliwag":255,
    "Bellsprout": 255,
    "Geodude": 255,
    "Magikarp": 255,
    "Sentret": 255,
    "Hoothoot": 255,
    "Ledyba": 255,
    "Spinarak": 255,
    "Hoppip": 255,
    "Wooper": 255,
    "Poochyena": 255,
    "Zigzagoon": 255,
    "Wurmple": 255,
    "Lotad": 255,
    "Seedot": 255,
    "Shroomish": 255,
    "Slakoth": 255,
    "Nincada": 255,
    "Nosepass": 255,
    "Skitty": 255,
    "Numel": 255,
    "Spoink": 255,
    "Spinda": 255,
    "Trapinch": 255,
    "Swablu": 255,
    "Baltoy": 255,
    "Feebas": 255,
    "Spheal": 255,
    "Clamperl": 255,
    "Starly": 255,
    "Bidoof": 255,
    "Kricketot": 255,
    "Budew": 255,
    "Bronzor": 255,
    "Bonsly": 255,
    "Patrat": 255,
    "Watchog": 255,
    "Lillipup": 255,
    "Purrloin": 255,
    "Pidove": 255,
    "Roggenrola": 255,
    "Audino": 255,
    "Tympole": 255,
    "Sewaddle": 255,
    "Venipede": 255,
    "Maractus": 255,
    "Minccino": 255,
    "Vanillite": 255,
    "Ferroseed": 255,
    "Unown": 225
    }
playerMons = []
print("Welcome to Pokémon: Cheeseburger Edition!")
print("Professor Cheeseburger gave you some starting items to begin your journey with!")
print("Obtained 10 Poké Balls, 5 Great Balls and 100$!")
dummy = 0
pokeBalls = 10
greatBalls = 5
ultraBalls = 0
masterBalls = 0
cheeseburgers = 0
poke = 0
catch = 0
cash=100
while dummy == 0:
    step = str(input("What will you do? Enter 'h' for help. "))
    if step == "h":
        print("List Pokémon: p \nMove: f, l, b, r\nInventory: i\nSave: save\nLoad: load\nShop: shop")
        step = str(input("What will you do? Enter h for help. "))
    if step == "save":
        print("Here is your save code:")
        print(str(playerMons)+"&"+str(pokeBalls)+"&"+str(greatBalls)+"&"+str(ultraBalls)+"&"+str(masterBalls)+"&"+str(cheeseburgers)+"&"+str(dummy)+"&"+str(cash))
        step = str(input("What will you do? Enter h for help. "))
    if step == "load":
        print("Enter your save code")
        code=input()
        var=0
        inlist=True
        smons=[]
        sballs=""
        sgreat=""
        sultra=""
        smaster=""
        sburger=""
        sdummy=""
        scash=""
        poke=""
        for i in range(len(code)):
            if inlist:
                if code[i]=="," or code[i]=="]":
                    if len(poke)>2:
                        smons.append(poke)
                        poke=""
                if code[i]=="]":
                    inlist=False
                if code[i]!="[" and code[i]!="'" and code[i]!="]" and code[i]!="," and code[i]!=" ":
                    poke+=code[i]
            if code[i]=="&":
                var+=1
                continue
            elif not inlist:
                if var==1:
                    sballs+=code[i]
                if var==2:
                    sgreat+=code[i]
                if var==3:
                    sultra+=code[i]
                if var==4:
                    smaster+=code[i]
                if var==5:
                    sburger+=code[i]
                if var==6:
                    sdummy+=code[i]
                if var==7:
                    scash+=code[i]
        playerMons=smons
        pokeBalls=int(sballs)
        greatBalls=int(sgreat)
        ultraBalls=int(sultra)
        masterBalls=int(smaster)
        cheeseburgers=int(sburger)
        dummy=int(sdummy)
        cash=int(scash)
        step = str(input("What will you do? Enter h for help. "))
    if step == "p":
        print(playerMons)
        step = str(input("What will you do? Enter h for help. "))
    if step == "i":
        print("You have " + str(pokeBalls) + " Poké Balls, "  + str(greatBalls) + " Great Balls, " + str(ultraBalls) + " Ultra Balls,  " + str(masterBalls) + " Master Balls, and " + str(cheeseburgers) + " cheeseburgers!")
        step = str(input("What will you do? Enter h for help. "))
    if step == "shop":
        flag = True
        while flag:
            print("you have $"+ str(cash))
            step = input("type poke, great or ultra. press enter to leave. ")
            if step=="poke" and cash>=100:
                cash-=100
                pokeBalls+=1
                print("You bought a Poké Ball!")
            elif step=="great" and cash>=500:
                cash-=500
                greatBalls+=1
                print("You bought a Great Ball!")
            elif step=="ultra" and cash>=5000:
                cash-=5000
                ultraBalls+=1
                print("You bought a Ultra Ball!")
            elif step=="poke" and cash<100:
                print("not enough money.")
            elif step=="great" and cash<500:
                print("not enough money.")
            elif step=="ultra" and cash<5000:
                print("not enough money.")
            else:
                flag=False
        step = str(input("What will you do? Enter h for help. "))
    if step == "f":
        unoprob = random.random()
        if unoprob > 0.999:
            art1 = input("As you head into the snowy mountains, you feel the glistening snow fall down on your face. ")
            art2 = input("You hear the soft coo of a bird in the distance - and then you see it. ")
            art3 = input("Articuno glides up to you, wanting to join your team. ")
            print("Articuno joined your team!")
            playerMons.append("Articuno")
    if step == "l":
        dosprob = random.random()
        if dosprob > 0.999:
            zap1 = input("The storm grows louder. You try to seek shelter in a cabin. ")
            zap2 = input("You hear something closing in on you. You turn around and see what's going on. ")
            zap3 = input("Zapdos flies up to you, and seems to be beckoning to you. It seems interested in you. ")
            print("Zapdos joined your team!")
            playerMons.append("Zapdos")
    if step == "r":
        tresprob = random.random()
        if tresprob > 0.999:
            mol1 = input("In the forest, everything is quiet. ")
            mol2 = input("Suddenly, Pokémon everywhere run away from their homes. A flock of Pidgey takes off, and all of the Ekans bury deep underground. ")
            mol3 = input("It's a forest fire! You see Moltres slowly flying towards you. It wants to join you. ")
            print("Moltres joined your team!")
            playerMons.append("Moltres")
    if step == "b":
        mewsprob = random.random()
        if mewsprob > 0.999 and mewsprob < 0.9995:
            mol1 = input("Two legendary Pokémon fight in the distance. ")
            mol2 = input("Mew and Mewtwo have vowed to act upon years of resentment by having a massive duel. ")
            mol3 = input("A giant explosion arises, knocking you back. Mew flies out, looking injured but alive. It needs you. ")
            print("Mew joined your team!")
            playerMons.append("Mew")
        if mewsprob >= 0.9995:
            mol1 = input("Two legendary Pokémon fight in the distance. ")
            mol2 = input("Mew and Mewtwo have vowed to act upon years of resentment by having a massive duel. ")
            mol3 = input("A giant explosion arises, knocking you back. Mewtwo walks out, looking injured but alive. It needs you (to die). ")
            print("Mewtwo joined your team!")
            playerMons.append("Mewtwo")
    if step in "fblr":
        pokeProb = random.random()
        if pokeProb < 0.1:
            print("Look! A cheeseburger!")
            print("Obtained a cheeseburger!")
            cheeseburgers += 1
        elif pokeProb < 0.2:
            print("Nothing appeared...")
        elif pokeProb < 0.35:
            print("You saw a Pokémon, but when you got closer, it warped using a portal gun!")
        elif pokeProb < 0.4:
            print("The tall grass remained still...")
        elif pokeProb < 0.56:
            print("You can't really see anything...")
        elif pokeProb < 0.57:
            print("It’s so foggy you walked into a wall!")
        elif pokeProb < 0.58:
            print("You thought a Pokémon appeared, but it was just a tuna sandwich.")
        elif pokeProb < 0.59:
            print("A wild Agumon appeared! Oh wait, wrong franchise.")
        elif pokeProb < 0.6:
            print("You thought a Pokémon appeared, but it was just a remarkably lifelike baked potato.")
        elif pokeProb < 0.7:
            print("You saw a Master Ball on the ground, but when you picked it up, it glitched into a cheeseburger.")
            print("Obtained a cheeseburger!")
            cheeseburgers += 1
        elif pokeProb < 0.75:
            print("A delivery dactyl appeared out of the sky and gave you some items!")
            givenPoke = random.random()
            givenGreat = random.random()
            givenUltra = random.random()
            givenMaster = random.random()
            givenCheeseburger = random.random()
            givenCash = random.randint(0,5)
            if givenPoke < 0.3:
                 givenPoke = 0
            elif givenPoke < 0.55:
                 givenPoke = 1
            elif givenPoke < 0.8:
                givenPoke = 2
            else:
                givenPoke = 3
            if givenGreat < 0.5:
                givenGreat = 0
            elif givenGreat < 0.8:
                givenGreat = 1
            else:
                givenGreat = 2
            if givenUltra < 0.7:
                givenUltra = 0
            else:
                givenUltra = 1
            if givenMaster < 0.99:
                givenMaster = 0
            else:
                givenMaster = 1
            if givenCheeseburger < 0.7:
                givenCheeseburger = 0
            else:
                givenCheeseburger = 1
            givenCash= givenCash*100



            pokeBalls += givenPoke
            greatBalls += givenGreat
            ultraBalls += givenUltra
            masterBalls += givenMaster
            cheeseburgers += givenCheeseburger
            cash+=givenCash
            print("Obtained " + str(givenPoke) + " Poké Balls! ")
            print("Obtained " + str(givenGreat) + " Great Balls! ")
            print("Obtained " + str(givenUltra) + " Ultra Balls! ")
            print("Obtained " + str(givenMaster) + " Master Balls!")
            print("Obtained " + str(givenCheeseburger) + " cheeseburgers!")
            print("Obtained $" + str(givenCash) + "!")
        else:
            wildmon = random.choice(list(pokeList.keys()))
            isBattling = 1
            print("A wild " + wildmon + " appeared! ")
            if wildmon in ["Articuno", "Zapdos", "Moltres", "Mewtwo", "Mew"]:
                print("It's eating a cheeseburger!")
            while isBattling == 1:
                ballUsed = str(input("What item will you use? Type poke, great, ultra, master, cheeseburger, or run. "))
                if ballUsed == "poke" and pokeBalls > 0:
                    pokeBalls -= 1
                    print("You used a Poké Ball!")
                    poke = 1
                elif ballUsed == "poke" and pokeBalls == 0:
                    print("You don't have a Poké Ball!")
                    poke=0
                elif ballUsed == "great" and greatBalls > 0:
                    greatBalls -= 1
                    print("You used one Great Ball!")
                    poke = 1.5
                elif ballUsed == "great" and greatBalls == 0:
                    print("You don't have a Great Ball!")
                    poke=0
                elif ballUsed == "ultra" and ultraBalls > 0:
                    ultraBalls -= 1
                    print("You used one Ultra Ball!")
                    poke = 2
                elif ballUsed == "ultra" and ultraBalls == 0:
                    print("You don't have a Ultra Ball!")
                    poke=0
                else:
                    poke=0
                catch = math.ceil((100*pokeList[wildmon]*poke)/300)
                if random.randint(1,100) <= catch:
                    print(wildmon + " was caught!")
                    playerMons.append(wildmon)
                    isBattling = 0
                elif poke>0:
                    print(wildmon +" broke free!")
                if ballUsed == "master" and masterBalls > 0:
                    masterBalls -= 1
                    print("You used one Master Ball!")
                    print(wildmon + " was caught!")
                    playerMons.append(wildmon)
                    isBattling = 0
                if ballUsed == "run":
                    print("You ran away!")
                    isBattling = 0
                if ballUsed == "":
                    print("type something!!")
                if ballUsed == "cheeseburger" and cheeseburgers > 0:
                    cheeseburgers -=1
                    print("You hurled a cheeseburger at " + wildmon + "!")
                    if random.randint(0,2) == 0:
                        print("Before your very eyes, " + wildmon + " ate the cheeseburger!")
                    if random.randint(0,2) == 1:
                        print("the "+ wildmon + " ignored the cheeseburger.")
                    else:
                        print("the "+ wildmon +" swatted the cheeseburger back at you! Ouch! You think it's laughing at you..")
