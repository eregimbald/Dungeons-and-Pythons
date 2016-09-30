#ver 0.01
import random


def deathisinevitable(deathtoll):
    army = {"Name": "The bananas", "Type": "human", "Footsoldiers": 10, "Archers": 20, "Cavalry": 30, "Siege weapons": 40}
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



deathisinevitable(15)
