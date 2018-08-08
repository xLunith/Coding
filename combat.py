def battleStart(player, enemy):
    turn = 0
    fight = 1
    while(fight == 1):
        if(turn == 0):
            atkDecision = int(
                input('An ' + enemy.name + ' attacks!\n1. Attack'))
            if(atkDecision == 1):
                enemy.dmg(player.atk)
                print('You attack the ' + enemy.name
                      + ' for ' + str(player.atk) + ' damage!')
                turn = 1

        if(turn == 1):
            print(enemy.name + ' attacks you, dealing ' + str(enemy.atk) + '!')
            player.dmg(enemy.atk)
            turn = 0

        if(player.hp < 1):
            player.death()
            print('You died!')
            fight = 0

        if(enemy.hp < 1):
            print(enemy.name + " has died!")
            player.getXp(enemy.xp)
            fight = 0
