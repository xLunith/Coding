import random
import item


class entity:

    name = ''
    maxHp = 1
    hp = 1

    # added so non character entities could have hp as well
    def setMHP(x):
        maxHP = x
    # Updates entity health

    def dmg(self, dmg):
        self.hp -= dmg
        if(self.hp > self.maxHp):
            self.hp = self.maxHp


class character(entity):

    atk = 0
    ac = 0
    xp = 0
    level = 1

    eqpWep = item.weapon('None', 1, 1)
    eqpArm = item.armor('None', 1, 1)

    # Character ability scores
    stats = {'str': 0, 'dex': 0, 'con': 0, 'int': 0}

    origin = ''

    # initializer, makes the name
    def __init__(self, name):
        self.name = name

    # adds xp to character
    def getXp(self, xp):
        self.xp += xp

    # Call after every change to stats
    def statUpdate(self):
        self.maxHp = self.stats['con'] + self.level  # Figure out HP scaling!
        self.atk = self.eqpWep.atk + self.stats['str']
        self.ac = self.eqpArm.ac

    def generateStats(self):
        for x in self.stats:
            self.stats[x] = random.randint(1, 6)

    # Called when the character levels up, increases stats randomly.
    def levelUp(self):
        for x in self.stats:
            self.stats[x] += random.randint(1, 6)
        self.statUpdate()

    def death(self):
        self.maxHp = 0


# Generates a new NPC with random stats.
def npcGen(name):
    npc = character(name)
    npc.generateStats()
    npc.statUpdate()
    return npc


def playerGen(name):
    player = character(name)
    statPool = []

    for x in range(4):
        statPool.append(random.randint(1, 6))

    print(str(statPool))

    def allocate(stat):
        player.stats[stat] = int(input(x + ': '))
        if(statPool.count(player.stats[x]) == 0):
            print("Invalid Input")
            player.stats[x] = 0
            allocate(stat)

    for x in player.stats:
        allocate(x)

    return player


'''
class bodyPart(entity):

    #
    def __init__(self, hitpoints):
        self.setMHP = hitpoints


class leg(bodyPart):



class arm(bodyPart):



    #if dead, character dead? but has most health
class torso(bodyPart):



    #lowers accuracy?
class head(bodyPart):
'''
