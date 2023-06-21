from random import *
from playsound import playsound
import os
sounds_dir = os.path.join(os.getcwd(), 'Sounds')
variable_words = [name.replace('.mp3', '') for name in os.listdir(sounds_dir)]
correctguess = 0
incorrectguess = 0
mistakes = []
guess = ''
choose = int(input('1 for full check, 2 for random check'))
while choose!= 1 and choose!= 2 :
    choose = int(input('1 for full check, 2 for random check'))
if choose == 1:
    for i in variable_words:
        playsound(os.path.join(sounds_dir, i + '.mp3'))
        guess = input('Enter your guess or enter "exit" to stop').title()
        if guess == i:
            print ('You are right')
            correctguess+=1
        elif guess == 'Exit':
            break
        else:
            print ('You are wrong. Right word is '+i)
            incorrectguess+=1
            mistakes.append(i)
    print(mistakes)
else:
    while guess != 'Exit':
        word_random = randint(0,len(variable_words)-1)
        playsound(os.path.join(sounds_dir, variable_words[word_random] + '.mp3'))
        guess = input('Enter your guess or enter "exit" to stop').title()
        if guess == variable_words[word_random]:
            print ('You are right')
            correctguess+=1
        elif guess == 'Exit':
            break
        else:
            print ('You are wrong. Right word is '+variable_words[word_random])
            incorrectguess+=1
            mistakes.append(variable_words[word_random])
print('Right answers = ',correctguess, 'Wrong answers = ', incorrectguess)
print(mistakes)
