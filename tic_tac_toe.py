import os
from os import system, name


#format(remote[0], remote[1], remote[2], remote[3], remote[4], remote[5], remote[6], remote[7], remote[8])


def logo(*args):
    os.system('cls' if os.name=='nt' else 'clear')
    print('\n\n\t\tTic-Tac-Toe')
    print('\t\t\b*************\n')
    print('''
         _______ _______ _______
        |       |       |       |
        |   {}   |   {}   |   {}   |
        |_______|_______|_______|
        |       |       |       |
        |   {}   |   {}   |   {}   |
        |_______|_______|_______|
        |       |       |       |
        |   {}   |   {}   |   {}   |
        |_______|_______|_______|


'''.format(*args))

def game():
    remote = [1,2,3,4,5,6,7,8,9]
    logo(*remote)
    plr1 = input(('  Player 1, Do you want to be X or O ? '))
    if plr1 == 'X' or plr1 == 'x':
        plr1 = 'X'
        plr2 = 'O'
    else:
        plr1 = 'O'
        plr2 = 'X'
    
    logo(*remote)

    def checker(plr, n=''):
        final = ''
        chances = ['048', '246', '012', '345', '678', '036', '147', '258']
        '''
        0 1 2
        3 4 5
        6 7 8 
        '''
        for i in range(len(remote)):
            if remote[i] == plr:
                final = final + str(i)
            else:
                pass
        print(final)
        for chance in chances:
            if chance.split() in final.split():
                print('Congrats ! Player {} have won the match.'.format(n))
                exit()
            

    for control in range(1,10):
        if control%2 == 0:
            pos1 = int(input('\n  Player 1 can choose his position : '))
            remote.insert(remote.index(pos1), plr1)
            remote.remove(pos1)
            logo(*remote)
            checker(plr1, 1)

        else:
            pos2 = int(input('\n  Player 2 can choose his position : '))
            remote.insert(remote.index(pos2), plr2)
            remote.remove(pos2)
            logo(*remote)
            checker(plr2, 2)

game()