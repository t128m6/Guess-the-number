import languages
import random


#LANGUAGES SETTING DOCUMENTATION

#TEXT OUTPUT (DONT FORGET "" OR '')
# #0 - Help how to
# #1 - Help output
# #2 - What's your guess?
# #3 - To high
# #4 - To low
# #5 - You're right
# #6 - number was
# #7 - output number of tries
# #8 - exiting program
# #9 - invalid input

#COMMANDS
# #51 - help
# #52 - close the program

##################################LANGUAGES##################################







def start():
    set_language()

def set_language():
    lang_selection = str(input('deutsch/english: '))
    global lang
    

    if lang_selection == 'deutsch':
        lang = languages.german
    elif lang_selection == 'english':
        lang = languages.english
    else:
        set_language()
    


    lang[404] = 'debug'
    start_game()

def start_game():

    #range of the random numbers
    minimum = 1
    maximum = 1000
 
    secret = random.randint(minimum, maximum ) 
    guess = -1
    counter = 0

    print(lang[0])

    while guess != secret:
        guess = (input(lang[2]))
        if guess.isnumeric():
            guess = int(guess)
            if guess > secret:
                print(lang[3])
            elif guess < secret:
                print(lang[4])
        elif type(guess) is str:
            if lang['help'] in guess: 
                 print(lang[1], minimum, '-', maximum ) 
            elif lang['quit'] in guess:
                print(lang[8])
                exit()

            #### DEBUG: directly giving the secret number
            elif lang[404] in guess:
                print('DEBUG STARTED')
                print('The secret is: ', secret)
                exit()
            else:
                print(lang[9])

        counter = counter+1


    print(lang[5])
    print(lang[6], secret)
    print(lang[7], counter)

start()