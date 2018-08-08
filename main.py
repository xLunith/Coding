import entity
import location
import random
import combat

# Variable that determines game start conditions
saveExists = 0
while(True):
    if(saveExists == 0):
        player = entity.playerGen(input('Name: '))
