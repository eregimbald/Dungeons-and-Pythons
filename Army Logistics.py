###############################################################################
import random


#TODO
#Alphabetical order in army[]
#Ridge > Add death, revise math
#Trap hall
#Battle simulator

#Two ## signs indicate a debugging print message

def prompt(army):

    while True:
        commandlist = {"help : " : "Display a list of commands", "setup : " : "Create a new army", "danger : " : "March your army through dangerous terrain",
                       "exit : " : "Exit the program", "status": "Display the army's status"}

        print
        command = raw_input("What would you like to do today? : ")

        if command == "help":
            for i in commandlist.iterkeys():
                print i, commandlist[i]
        elif command == "exit":
            break
        elif command == "setup":
            armysetup(army)
        elif command == "danger":
            dangterrain(army)
        #Debugging command
        elif command == "status":
            for key, value in army.iteritems():
                print str(value) + " " + key


def armysetup(army):
    print
    print "Welcome to Army Logistics!"
    print "What kind of army are you managing?"
    print
    army["race"] = (raw_input("Human? Elf? Dwarf? Orc? Robots? etc. : "))
    army["footsoldiers"] = int(raw_input("How many foot soldiers are in your army? : "))
    army["archers"] = int(raw_input("How many archers are in your army? : "))
    army["cavalry"] = int(raw_input("How many horsemen are in your army? : "))
    army["siege weapons"] = int(raw_input("How many siege weapons are in your army? : "))
    print
    print "### One supply unit will keep a soldier fed and fit for one day. ###"
    print
    army["supplies"] = int(raw_input("How many days worth of supplies does your army have? : "))

    return army

    # print
    # armymora = int(raw_input("How strong is your army's morale? (1 - 5)"))

    # armyraw = armyfoot + armyarch + armycava


def deathisinevitable(deathtoll,army):
    #This function splits up the dead between the 4 army categories
    #deathtoll is the total amount of dead, now we have to decide who died

    transport = {"footsoldiers": 0, "archers": 0, "cavalry": 0, "siege weapons": 0}

    #While there are dead, pick one of the categories in transport
    #Select a random number of soldiers less than or equal to deathtoll
    #if there are at least this many soldiers in the selected category in the army, subtract them from army, add them to transport
    #if not, do nothing, restart the loop
    while deathtoll > 0:
        pick = random.choice(transport.keys())
        ##print "pick: " + pick
        dead = random.randint(1, deathtoll)
        ##print "dead: " + str(dead)
        ##print "armybefore: " + str(army[pick])
        if army[pick] >= dead:
            army[pick] -= dead
            transport[pick] += dead
            deathtoll -= dead
            ##print "deathtoll: " + str(deathtoll)
            ##print "armyafter %s: " % pick + str(army[pick])

    #Once the loop is complete and there are no more dead to distribute, display the total deaths by category
    print "=========="
    for key, value in transport.iteritems():
        print str(value) + " " + key + " have perished."


def dangterrain(army):
    import time
    print
    print "Your army is traversing difficult terrain!"
    terrain = raw_input("What kind of terrain? A body of (water)? A narrow (ridge) or a (trap) field? : ")

    if terrain == "water":
        flow = int(raw_input("How strong is the flow of the water? Stagnant to raging current (0 - 3) : "))
        size = int(raw_input("How large is this water body? Pond to large lake (1 - 5) : "))
        boats = int(raw_input("How many boats is your army using? : "))
        men = int(raw_input("How many soldiers fit in a boat? : "))

        #Calculate the number of trips from shore A to shore B
        #Trip = Total men, divided by menperboat - 1, for the guy who returns the boat to Shore A.
        #Multiplied by 2, because boats have to return to shore A to get more soldiers. - 1 because the last trip stays on shore B.
        #Divided by the number of boats, + 1 for the last boat which has less than total capacity.
        #If the number of trips is even, - 1 because we're not bringing back the boats
        trip = ((((army["footsoldiers"] + army["archers"] + army["cavalry"] + army["siege weapons"]) // (men - 1)) * 2) - 1) // boats + 1
        if trip % 2 == 0:
            trip -= 1

        print
        print "With %s soldiers and their gear to a boat, it's going to take %s trips to get to the other side" % (men, trip)
        print

        #DC is Strength of current x 4, + 1 to set a minimum of 1% chance of accidents
        risk = 4 * flow + 1
        print "##### The DC for an accident %s!##### " % risk
        deathtoll = 0
        supplytoll = 0

        raw_input("Press Enter to continue...")

        for i in range(trip):
            print
            print "Trip number %s is in the water!" % (i + 1)
            time.sleep(0.5)
            roll = random.randint(1, 100)
            print "Roll 1d100 = %s!" % roll

            if roll > risk:
                answer = random.randint(1, 3)
                if answer == 1:
                    print "So far so good..."
                elif answer == 2:
                    print "No problem!"
                else:
                    print "Smooth sailing, baby!"

        #If the roll is less that 3x the DC, the accident results in deaths
            if roll <= risk:
                print "There's been an accident!"
                time.sleep(1)
                if (roll // 3) <= risk:
                    dead = random.randint(1, men)
                    deathtoll += dead
                    print "%s soldiers have fallen into the water! There were no survivors..." % (dead)
                else:
                    drop = random.randint(1, men)
                    supplytoll += drop
                    print "%s supplies have fallen into the water! They can't be recovered..." % (drop)
        time.sleep(1.5)

        # Embark time + travel time x flow
        time = 10 * trip // boats + trip * ((10 * size) + ((size + 10) * flow))
        print
        print "##########################################"
        print "The journey is complete!"
        print "It took [%s trips] to reach the other side." % trip
        print "In total, it took [%s minutes] to load and unload the boats." % (10 * trip // boats)
        print "Because of the size of the body and strength of the current, a one-way trip took [%s minutes]." % ((10 * size) + ((size + 10) * flow))
        print "The complete journey took [%s hours, %s minutes]!" % ((time//60), (time%60))

        if supplytoll == 0:
            print "What's more, luck was on our side! We have not lost any supplies during the trip."
        else:
            print "However, due to carelessness or sheer incompetence, we have lost %s supplies. Names will taken down..." % supplytoll
            army["supplies"] -= supplytoll

        if deathtoll == 0:
            print "The Gods' favour was with us! Nobody died!"
        else:
            print "Tragedy! We have lost a total of %s soldiers during the voyage!" % deathtoll
            deathisinevitable(deathtoll,army)

    if terrain == "ridge":
        deconstruct = 0
        distance = raw_input("How long is this ridge? (x feet) : ")
        stability = raw_input("How solid is the ridge? Completely safe or as unstable as a one-legged pirate walking a tightrope?  (0 - 3) : ")
        men = raw_input("By the ridge's width, how many men can walk abreast? : ")
        speed = raw_input("Is the army moving at half-speed, full-speed or are they hauling ass? (1 - 3) : ")

        totalmen = army["footsoldiers"] + army["archers"] + army["cavalry"] + army["siege weapons"]

        if men == 1:
            if army["cavalry"] > 0:
                print "This ridge is too narrow for cavalry, they will have to stay behind."
                answer = raw_input("Shall we leave them behind? (yes/no) : ")
                if answer == "yes":
                    army["cavalry"] = 0
            if army["siege weapons"] > 0:
                print "This ridge is too narrow for siege weapons, they will have to stay behind."
                answer = raw_input("Shall we leave them behind? (yes/no) : ")
                if answer == "yes":
                    army["siege weapons"] = 0

        if men == 2:
            if army["cavalry"] > 0:
                print "Space is tight, it will take longer to bring the horses through."
                answer = raw_input("Shall we leave them behind? (yes/no) : ")
                    if answer == "yes":
                        army["cavalry"] = 0
                    elif answer == "no":
                    totalmen += army["cavalry"]
            if army["siege weapons"] > 0:
                print "This ridge is too narrow for siege weapons, they will have to stay behind unless we deconstruct them and rebuild them on the other side. (60 minutes)"
                answer = raw_input("Shall we leave them behind? (yes/no) : ")
                if answer == "yes":
                    army["siege weapons"] = 0
                elif answer == "no":
                    deconstruct = 60

        if men == 3:
            if army["siege weapons"] > 0
                print "Space is tight, it will take longer to bring the siege weapons through."
                answer = raw_input("Shall we leave them behind? (yes/no) : ")
                if answer == "yes":
                    army["siege weapons"] = 0
                elif answer == "no":
                    totalmen += army["siege weapons"]

        # Convert speed to fpm and float, Match army speed to the speed of siege weapons
        # Calculate travel time + extra for length of the army
        if army["siege weapons"] > 0:
            speed = speed * 5 * 10.0
        else:
            speed = speed * 15 * 10.0

        time = distance / speed + ((math.ceil(totalmen // men) + totalmen % men) * 5) / speed + deconstruct

        print "With %s soldiers moving abreast, the passage took [%s minutes, %s seconds] or [%s rounds] to cross." % (int(time * 60 // 60), int(time * 60 % 60), int(math.ceil(time * 6)))

############################## READY FOR DEATH


        # DC is Strength of current x 4, + 1 to set a minimum of 1% chance of accidents
        risk = 4 * flow + 1
        print "##### The DC for an accident %s!##### " % risk
        deathtoll = 0
        supplytoll = 0

#######################################################

army = dict()

print "============ Welcome to Dungeons and Pythons! ============"
print "Type help for a list of commands."

army["footsoldiers"] = 60
army["archers"] = 20
army["cavalry"] = 0
army["siege engines"] = 10
army["supplies"] = 125

prompt(army)

