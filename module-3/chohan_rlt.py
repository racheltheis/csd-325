#Rachel Theis
#CSD 325
#11.3.24

#This is a prewritten program for "Cho-Han" with modifications per the module 3.2 assignment 

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number. \nIf you roll a 2 or a 7, you will collect a 10 mon bonus
''')
#adding a notice about the 10 mon bonus when a 2 or 7 is rolled. 

purse = 5000
while True: 
    print('rlt:')
    #changing the input prompt to my initials
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)  
            break  

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot 
        print('The house collects a', pot // 12, 'mon fee.')
        #changing the house fee to 12%
        purse = purse - (pot // 12)
        #changing the house fee to 12%
    else:
        purse = purse - pot 
        print('You lost!')
        
    #adding 10 mon bonus when player rolls a 2 or 7
    if dice1 == 2 or dice1 == 7 or dice2 == 2 or dice2 == 7:
        print ('Congrats! You rolled a 2 or 7 with your roll of:', dice1 ,'&' , dice2 ,'. Take your 10 mon bonus!')
        purse = purse + 10
    
    else:
        purse = purse

    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
