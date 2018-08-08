import entity
import random

# Nested dictionary that gives stats for each location type
localeType = {'Town': {'minPop': 5, 'maxPop': 100, 'genType': ['humanoid'],
                       'subLocale': ['Blacksmith', 'Townhall', 'Market', 'Barracks']},
              'Forest': {'minPop': 1, 'maxPop': 200, 'genType': 'beast',
                         'subLocale': ['Forest Outskirts', 'Deep Thicket', 'Cave']}
              }

subLocaleType = {'Blacksmith': {'minPop': 1, 'maxPop': 5,
                                'genType': ['smith'],
                                'repeatable': 1, 'chance': 2},
                 'Townhall': {'minPop': 1, 'maxPop': 10,
                              'genType': ['mayor', 'guard'],
                              'repeatable': 0, 'chance': 5},
                 'Market': {'minPop': 1, 'maxPop': 10,
                            'genType': ['merchant', 'guard'],
                            'repeatable': 1, 'chance': 2},
                 'Barracks': {'minPop': 1, 'maxPop': 20,
                              'genType': ['captain', 'guard'],
                              'repeatable': 1, 'chance': 3},
                 'Forest Outskirts': {'minPop': 1, 'maxPop': 50,
                                      'genType': ['forest beast'],
                                      'repeatable': 1, 'chance': 5},
                 'Deep Thicket': {'minPop': 1, 'maxPop': 100,
                                  'genType': ['forest beast', 'forest elite'],
                                  'repeatable': 1, 'chance': 4},
                 'Cave': {'minPop': 1, 'maxPop': 20,
                          'genType': ['cave beast'],
                          'repeatable': 1, 'chance': 1}}

worldStats = {'width': 0, 'height': 0, 'age': 0}


class location:

    name = ''
    type = ''
    age = 0
    pop = 0
    coord = []
    subLocations = []
    popTable = []

    def __init__(self, name, type):
        self.name = name
        self.type = type


class subLocation:

    parentLocation = ''

    def __init__(self, name, type, parent):
        self.name = name
        self.type = type
        self.parentLocation = parent


def subLocationGen(parent):
    cardDir = 0
    cardDirMem = []
    cardDirName = ''

    def cardDirRoll():
        cardDir = random.randint(1, 4)
        if(cardDirMem.count(cardDir) == 1):
            cardDirRoll()
        if(cardDir == 1):
            cardDirName = 'North'
        if(cardDir == 2):
            cardDirName = 'South'
        if(cardDir == 3):
            cardDirName = 'East'
        if(cardDir == 4):
            cardDirName = 'West'
        cardDirMem.append(cardDir)
        return cardDirName

    for x in localeType[parent.type]['subLocale']:
        cardDirMem.clear()
        if(random.randint(1, 5) <= subLocaleType[x]['chance']):
            cardDirName = cardDirRoll()
            newSubLocation = subLocation(
                (cardDirName + ' ' + x), x, parent)
            parent.subLocations.append(newSubLocation)

            repeats = 0
            while(subLocaleType[x]['repeatable'] == 1):
                if(random.randint(1, 5) <= subLocaleType[x]['chance'] - repeats):
                    cardDirName = cardDirRoll()
                    newSubLocation = subLocation(
                        (cardDirName + ' ' + x), x, parent)
                    parent.subLocations.append(newSubLocation)
                    repeats += 1
                else:
                    break

# Generates and returns a new location with a table of characters


def locationGen(name, type):
    newLocation = location(name, type)
    newLocation.pop = random.randint(localeType[type]['minPop'],
                                     localeType[type]['maxPop'])
    newLocation.coord.append(random.randint(
        (-worldStats['width']/2), worldStats['width']/2))

    subLocationGen(newLocation)

    for x in range(newLocation.pop):
        npc = entity.npcGen(str(name) + str(x))
        newLocation.popTable.append(npc)

    return newLocation


locationtest = locationGen('test', 'Town')
for x in locationtest.subLocations:
    print(x.name)

for x in range(len(locationtest.popTable)):
    print(locationtest.popTable[x].name)
    for y in locationtest.popTable[x].stats:
        print(locationtest.popTable[x].con)
