#!/usr/bin/env python3

import random
answer = random.randint(1,100)
guess = []
i = 0
guess.append(input('Take a guess:'))
while True:
    try:
        if int(guess[i]) <= 100 and int(guess[i]) >= 1:
            if int(guess[i]) == answer:
                print(('Bingo at %sth try')%i)
                break
            elif i == 0 and abs(int(guess[i]) - answer) <= 10:
                print('Warm')
                guess.append(input('Try again:'))
                i += 1
            elif i == 0 and abs(int(guess[i]) - answer) > 10:
                print('Cold')
                guess.append(input('Try again:'))
                i += 1
            elif i > 0 and abs(int(guess[i]) - answer) > abs(int(guess[i-1]) - answer):
                print('Colder')
                guess.append(input('Try again:'))
                i += 1                
            elif i > 0 and abs(int(guess[i]) - answer) < abs(int(guess[i-1]) - answer):
                print('Warmer')
                guess.append(input('Try again:'))
                i += 1                
            elif i > 0 and int(guess[i]) == int(guess[i-1]):
                print('Don\'t put in the same number')
                guess.append(input('Try again:'))
                i += 1                
            else:
                print('Hmm...')
                guess.append(input('Try again:'))
                i += 1                
        else:
            print('Out of Range.')
            guess.pop()
            guess.append(input('Try again:'))
    except Exception as e:
        print('Invalid Input.')
        guess.pop()
        guess.append(input('Try again:'))
