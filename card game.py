import random
import time
done= False
start = False
end = False

balance =100
cbalance = 100
suit=('Spades','Hearts','Diamond','Clubs')
if start == False:
    print("Dealing the cards")
    start= True
time.sleep(2)
if done == False:

    rad=random.choice(suit)
    radd=random.randint(1,13)
    print('Player:',rad,radd)

    rad2=random.choice(suit)
    radd2=random.randint(1,13)
    print('Computer:',rad2,radd2)

    done = True
    end= True

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

while end == True:
    play=print(input('Do you want to continue playing? (Yes/No)'))
    again =input('Do you want to play again?')
    print(again)
    if again =='yes':
        done=False
        start=False
    if again == 'no':
        print('Thank you for playing')
    end=False

