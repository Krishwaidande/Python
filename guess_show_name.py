import random
import re
import sys

movieNames = ['Harry Potter', 'Friends', 'How I Met Your Mother','Game Of Thrones','Shadow Hunters','Big Bang Theory']
choice = random.choice(movieNames)
choice = choice.lower()
spaceCount=choice.count(' ')
movieGuess=[]

print ('It is ' + str(len(choice) + 1) + ' letters word')

def initializeBlankValues():
    i=0
    while (i < len(choice)):
        movieGuess.append('_')
        i=i+1

    print (movieGuess)

def checkLetter(letter):
    pos = [m.start() for m in re.finditer(letter,choice)]
        
    j=0
    while (j < len(pos)):
        movieGuess[pos[j]]=letter
        j=j+1

def checkGuess(letter):
    underScoreCount=movieGuess.count('_')
    
    if (letter == choice):
        print ('You guessed the movie/series correct')
        sys.exit()

    if underScoreCount == spaceCount:
        print('You guessed the movie/series name right')
        sys.exit()
        
def guessMovie():
    i=0
    while (i < len(choice)):
        letter = input('Enter the letter:')
        letter=letter.lower()
        checkLetter(letter)
        checkGuess(letter)
        i=i+1
        print (movieGuess)

def main():
    initializeBlankValues()
    guessMovie()
    print('You did not gussed it right..No worries better luck next time')

main()
