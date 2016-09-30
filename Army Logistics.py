###############################################################################
import random
import time


# ver 0.01

# Here is the schema of the army dictionary
# army[name] Name
# army[type] Race
# army[supp] Supplies
# army[f%] [a%] [c%] [s%] for Footmen, Archers, Cavalry and Siege weaponry
# army[%num] [%ski] [%mor] for Numbers, Skill and Morale
# Example: army[aski] is the skill level of the archer unit
# army[name] 0
# army[type] 1
# army[fnum] 2
# army[anum] 3
# army[cnum] 4
# army[snum] 5
# army[] 6
# army[] 7
# army[] 8
# army[] 9
# army[] 10
# army[] 11
# army[] 12

def prompt(army):

    while True:
        commandlist = {"help : " : "Display a list of commands", "setup : " : "Create a new army", "danger : " : "March your army through dangerous terrain",
                       "exit : " : "Exit the program"}

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
        elif command == "print":
            for key, value in army.iteritems():
                print str(value) + " " + key + " have perished."


def armysetup(army):
    print
    print "Welcome to Army Logistics"
    print "What kind of army are you managing?"
    army["race"] = (raw_input("Human? Elf? Dwarf? Orc? Robots? etc. : "))

    print
    army["footsoldiers"] = int(raw_input("How many foot soldiers are in your army? : "))

    print
    army["archers"] = int(raw_input("How many archers are in your army? : "))

    print
    army["cavalry"] = int(raw_input("How many horsemen are in your army? : "))

    print
    army["siege engines"] = int(raw_input("How many siege engies are in your army? : "))

    print
    print "One supply unit will keep a soldier fed and fit for one day."
    army["supplies"] = int(raw_input("How many days worth of supplies does your army have? : "))

    return army

    # print
    # armymora = int(raw_input("How strong is your army's morale? (1 - 5)"))

    # armyraw = armyfoot + armyarch + armycava


def deathisinevitable(deathtoll):
    # army = {"Name": "The bananas", "Type": "human", "Footsoldiers": 10, "Archers": 20, "Cavalry": 30, "Siege weapons": 40}
    transport = {"Footsoldiers": 0, "Archers": 0, "Cavalry": 0, "Siege weapons": 0}

    while deathtoll > 0:
        pick = random.choice(transport.keys())
        print "pick: " + pick
        dead = random.randint(1, deathtoll)
        print "dead: " + str(dead)
        print "armybefore: " + str(army[pick])
        if army[pick] > 0:
            army[pick] -= dead
            transport[pick] += dead
            deathtoll -= dead
            print "deathtoll: " + str(deathtoll)
            print "armyafter %s: " % pick + str(army[pick])
            print "=========="

    for key, value in transport.iteritems():
        print str(value) + " " + key + " have perished."


def dangterrain(army):
    print
    print "Your army is traversing difficult terrain!"
    terrain = raw_input("What kind of terrain? A body of (Water)? A narrow (Ridge) or a (Trap) field?")

    if terrain == "Water":
        flow = int(raw_input("How strong is the flow of the water? Stagnant to raging current (0 - 3)"))
        size = int(raw_input("How large is this water body? Pond to large lake (1 - 5)"))
        boats = int(raw_input("How many boats is your army using?"))
        men = int(raw_input("How many soldiers fit in a boat?"))

        trip = ((army[fnum] + army[anum] + army[cnum] + army[snum]) // men) // boats + 1
        print "With %s soldiers and their gear to a boat, it's going to take %s trips to get to the other side" % men, trip

        risk = 5 * flow + 1
        print "The risk factor is %s!" % risk
        time.sleep(1)
        deathtoll = 0
        supptoll = 0

        for i in range(trip):
            print
            print "Trip number %s is in the water!" % i
            time.sleep(0.2)
            luck = randint(1, 100)
            print "Roll 1d100 is %s!" % luck
            time.sleep(1)

            if luck > risk:
                answer = randint(1, 3)
                if answer == 1:
                    print "So far so good..."
                elif answer == 2:
                    print "No problem!"
                else:
                    print "Smooth sailing, baby!"

            if luck <= risk:
                print "There's been an accident!"
                time.sleep(1)
                if (luck // 3) <= risk:
                    dead = randint(1, 6)
                    deathtoll += dead
                    print "%s soldiers have fallen into the water! There were no survivors..." % (dead)
                    time.sleep(1)
                else:
                    drop = randint(1, 6)
                    supptoll += drop
                    print "%s supplies have fallen into the water! They can't be recovered..." % (drop)
                    time.sleep(1)

        # Embark time + travel time x flow
        time = 10 * trip + trip * ((10 * size) + ((size + 10) * flow))
        print
        print "##########################################"
        print "The journey is complete!"
        print "It took %s trips to reach the other side." % trip
        print "It took %s minutes to load and unload the boats." % 10 * trip
        print "Because of the size and strength of the current, it took %s minutes to traverse the water" % (
        (10 * size) + ((size + 10) * flow))
        print "The complete journey too %s minutes!" % time

        if supptoll == 0:
            print "What's more, luck was on our side! We have not lost any supplies during the trip."
        else:
            print "However, due to carelessness or sheer incompetence, we have lost %s supplies. Names will taken down..." % supptoll

        if deathtoll == 0:
            print "The Gods' favour was with us! Nobody died!"
        else:
            print "Tragedy! We have lost a total of %s soldiers during the voyage!" % deathtoll

        deathisinevitable(deathtoll)


#######################################################

army = dict()

print "============Welcome to Dungeons and Pythons!============"
print "Type --help for a list of commands."

prompt(army)

