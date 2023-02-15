import random

rand_num = random.randrange(1,100) #get random number between 1-100
user_guess = int(input('Please enter a number between 1-100: '))
attempt = 0 

while rand_num != user_guess:
    attempt += 1 #increment attempt by 1
    if user_guess > rand_num:
        print('Too big! Guess lower!')
        user_guess = int(input('Please enter a number again: '))
    elif user_guess < rand_num:
        print('Too smol! Guess higher!')
        user_guess = int(input('Please enter a number again: '))
    else:   
        break
print('Wow! You are correct! It took you', attempt, 'attempt to guess')
       