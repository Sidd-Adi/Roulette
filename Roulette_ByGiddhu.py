import random
import numpy as np

i=0

# 1 round means 1 roulette spin


guess_list =[] #Value given by the user for each guess
count_list =[] #List of number of bets made by user in each round
size_list  =[] #Bet size for each guess
win_list   =[] #Money won/lost by user in each round


game_dict = {'black':[15,4,2,17,6,13,11,8,10,24,33,20,31,22,29,28,35,26],
             'red':[32,19,21,25,34,27,36,30,23,5,16,1,14,9,18,7,12,3],
             'even':range(2,37,2),'odd':range(1,36,2),'column-a':[1,4,7,10,13,16,19,22,25,28,31,34],
             'column-b':[2,4,8,11,14,17,20,23,26,29,32,35],'column-c':[3,6,9,12,15,18,21,24,27,30,33,36],
             'dozen-a':range(1,13),'dozen-b':range(13,25),'dozen-c':range(25,37),'18-a':range(1,19),'18-b':range(19,37),
             'street-a':range(1,4),'street-b':range(4,7),'street-c':range(7,10),'street-d':range(10,13),'steet-e':range(13,16),
             'street-f':range(16,19),'street-g':range(19,22),'street-h':range(22,25),'street-i':(25,28),'street-j':(28,31),
             'street-k':range(31,34),'street-l':range(34,37),'line-a':range(1,7),'line-b':range(7,13),'line-c':range(13,19),
             'line-d':range(19,25),'line-e':range(25,31),'line-f':range(31,37)}
double_dict = {'black':[15,4,2,17,6,13,11,8,10,24,33,20,31,22,29,28,35,26],'red':[32,19,21,25,34,27,36,30,23,5,16,1,14,9,18,7,12,3],'even':range(2,37,2),'odd':range(1,36,2),'18-a':range(1,19),'18-b':range(19,37)}
triple_dict = {'column-a':[1,4,7,10,13,16,19,22,25,28,31,34],'column-b':[2,4,8,11,14,17,20,23,26,29,32,35],'column-c':[3,6,9,12,15,18,21,24,27,30,33,36],'dozen-a':range(1,13),'dozen-b':range(13,25),'dozen-c':range(25,37)}
line_dict = {'line-a':range(1,7),'line-b':range(7,13),'line-c':range(13,19),'line-d':range(19,25),'line-e':range(25,31),'line-f':range(31,37)}
street_dict = {'street-a':range(1,4),'street-b':range(4,7),'street-c':range(7,10),'street-d':range(10,13),'steet-e':range(13,16),'street-f':range(16,19),'street-g':range(19,22),'street-h':range(22,25),'street-i':(25,28),'street-j':(28,31),'street-k':range(31,34),'street-l':range(34,37)}


def game_count(): #The number of rounds user wants to play
    try:
        r = int(input('How many rounds do you want to play? '))
        if r<=0:
            print('Type a positive integer!')
            game_count()
    except ValueError:
        print('Type a positive integer!')
        game_count()
    return r


def bet_count(): #The number of bets, the user wants to place in one round
    try:
        n = int(input('Enter the number of bets you want to place in this round: '))
        if n<=0:
            print('Type a positive integer!')
            bet_count()
    except ValueError:
        print('Type a positive integer!')
        bet_count()
    count_list.append(n)


def guess(): #The number the user guesses, where the ball will fall
    spl = input('Do you want to make special bets(other than straight bets), type "yes" or "no": ')
    if spl.lower() == 'no':
        try:
            g = int(input('Enter your guess: '))
            if g>=0 and g<=36:
                guess_list.append([g])
            else:
                print('Type an integer from 0 to 36!')
                guess()
        except ValueError:
            print('Type an integer from 0 to 36!')
            guess()
    elif spl.lower() =='yes':
        g=input('Type your special bet: ')
        if game_dict.get(g) != None:
           guess_list.append(game_dict.get(g))
        else:
            print('Type a valid bet!')
            guess()
    else:
        print('Type "yes" or "no" only!')
        guess()
            
def max_bet(i):
    if len(guess_list[i])==18:
        return '8000'
    elif len(guess_list[i])==12:
        return '4000'
    elif len(guess_list[i])==6:
        return '2000'
    elif len(guess_list[i])== 3:
        return '1000'
    elif len(guess_list[i])== 1:
        return '500'
       
def bet_size(): #The amount of money the user wants to place on a single bet
    try:
        s = float(input(f'Enter your bet size for this guess (Minimum bet size is $ 5.00 and maximum is $ {max_bet(j)}): $ '))
        if s>=5 and s<=int(max_bet(j)):
            size_list.append(s)
        else:
            print(f'Invalid input!! Minimum bet size is $ 5.00 and maximum bet size is {max_bet(j)}.')
            bet_size()
    except ValueError:
        print('Invalid input!')
        bet_size()
        

def user_input(): #Retracts the user guess and corresponding bet size
    guess()
    bet_size()
    
    
def win_size(i): #The profit or loss of the user
    w = 0
    for x in guess_list[-count_list[i]:]:
        for k in x:
            if k == y:
                w += (36/len(x))*size_list[guess_list.index(x)]
    w-=np.sum(size_list[-count_list[i]:])
    win_list.append(w)
    return w
        
  
print('Welcome to Digital European Roulette!')
print('Roulette Bets & Payouts:')
print(' 1. Single number bet pays 35 to 1, which means you can get $ 35 if you put in $ 1. This is called a straight bet.')
print(' 2. Three number bet pays 11 to 1. Also called a “street”. In this game, we have 12 streets: street-a to street-l.')
print(' 3. Six number bets pays 5 to 1. Example: 7, 8, 9, 10, 11, 12. Also called a “line”.In this game, we have 6 lines: line-a to line-f.')
print(' 4. Twelve numbers or dozens (first, second, third dozen) pays 2 to 1. In this game, we have 3 dozens: dozen-a to dozen-c.')
print(' 5. Column bet (12 numbers in a row) pays 2 to 1. In this game, we have 3 columns: column-a to column-c.')
print(' 6. 18 numbers (1-18) pays even money(1 to 1) refered as 18-a.')
print(' 7. 18 numbers (19-36) pays even money(1 to 1) refered as 18-b.')
print(' 8. Red or black also pays even money.')
print(' 9. Odd or even also pays even money.')

r = game_count()
while i<r:
    j=0
    bet_count()
    y = random.randint(0,36)
    while j < count_list[i]:
        user_input()
        j+=1
    print(f'Betting over!, The number is {y}')
    if win_size(i)<0:
        print(f'In this round, you have lost $ {-win_list[i]}')
    else:
        print(f'In this round, you have won $ {win_list[i]}')     
    i+=1
if np.sum(win_list)<0:
    print(f'You have lost $ {-np.sum(win_list)}')
else:
    print(f'''
You finished with a profit of $ {np.sum(win_list)}''')
print("Hope you had fun! Come again later!")    
    
    


    
    

