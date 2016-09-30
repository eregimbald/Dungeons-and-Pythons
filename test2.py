#ver 0.01
from random import randint


def deathisinevitable(deathtoll):
    army = {"Name": "The bananas", "Type": "human", "Footsoldiers": 0, "Archers": 0, "Cavalry": 0, "Siege weapons": 0}
    transport = {"Footsoldiers": 0, "Archers": 0, "Cavalry": 0, "Siege weapons": 0}

    while deathtoll > 0:
        pick = randint(2, 5)
        print "pick: " + str(pick)
        dead = randint(1, deathtoll)
        print "dead: " + str(dead)
        print "armybefore: " + str(army[pick])
        if army[pick] > 0:
            army[pick] -= dead
            transport[pick - 2] += dead
            deathtoll -= dead
            print "deathtoll: " + str(deathtoll)
            print "armyafter %s: " % pick + str(army[pick])
            print "====="

    for key, value in transport.iteritems():
        print key + str(value) + " remain."


deathisinevitable(15)
