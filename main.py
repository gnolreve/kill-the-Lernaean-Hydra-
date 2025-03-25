import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number: 
        guess = int(input(f'Guess a number betwenn 1 and {x}: ') )
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess agin. Too high.')   

    print(f'Yay, good job. You are correct. {random_number} correctly!!') 

def computer_guess(x):
    low = 1
    high = x 
    feedback = ''     
    while feedback != 'c':
        if low != high: 
           guess = random.randint(low, high)
        else:
            guess = low # could alo be high b/c low = high 
        feedback = input(f'is {guess} too high (H), too low(L), or correct(C)??').lower()
        if feedback =='h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1   

    print(f'Yay! the computer guessed your number, {guess}, correctly! ')         

computer_guess(100)    