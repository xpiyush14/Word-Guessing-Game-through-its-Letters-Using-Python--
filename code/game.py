#-->Importing Ramdon library so as to select any random name out of the list
import random

words = ["Horizon","Whisper","Lantern","Puzzle","Voyage","Thunder","Canyon","Breeze","Mystery","Kingdom","Shadow","Rocket","Jungle","Mirror","Castle","Desert","Fortune","Phantom","Galaxy","Orbit"]

word = random.choice(words) #-->Chooses any random word from the list word

total_chances = 7  #-->The player will have only 7 chances till failure
guessed_word = "-"*len(word)



#--> Now for the user part
while total_chances != 0:
    print(guessed_word)
    letter = input('Guess a Letter: ').upper()
    if letter in word:
        for index in range(len(word)): #-->This will check if the guessed letter is right
            if word[index]==letter: #-->Will check every index of the word yet to be found and see if we guessed it right or wrong..
                guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]
        if guessed_word == word:
            print("Congratulations You Won")
            break
    else:
        total_chances -= 1
        print("Incorrect Guess")
        print('Remaining Chances -->',total_chances)
else:
    print("YOU LOOSE")
    print("GAME OVER, BETTER LUCK NEXT TIME")
    print("The Correct Word was-->",word)
