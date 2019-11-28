import random
import time
start = True

counter = 1

balance =10
cbalance = 10
suit=('Spades','Hearts','Diamond','Clubs')



while counter == 1:
    print("Dealing the cards")
    
    time.sleep(2)

    rad=random.choice(suit)
    radd=random.randint(1,13)
    print('Player:',rad,radd)

    rad2=random.choice(suit)
    radd2=random.randint(1,13)
    print('Computer:',rad2,radd2)
    time.sleep(1)

    if radd> radd2:
        print('You win')
        balance +=5
        cbalance -=5
        print('your balance is',balance)

    if radd< radd2:
        print('You Lose')
        balance -=5
        cbalance +=5
        print('your balance is',balance)


    if balance == 0:
        print("You lose the game!")
        counter == 0
        break

    if balance==20:
        print('You win the game!')
        counter == 0
        break
    
    
