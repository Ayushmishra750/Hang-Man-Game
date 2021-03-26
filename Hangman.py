import random
import HangmanArt 
import HangmanWord
from os import system ,name 

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
  
    else: 
        _ = system('clear') 

def gameover(outputList , life):
    Count_ = outputList.count("_")
    if Count_ == 0:
        print("You saved Hangman life")
        print("Game Over")
        exit()
    elif life == 0:
        print(f"The correct word is {randomWord} ")
        print("Hangman died R.I.P")
        print("Game Over")
        exit()


clear()

print("\n" , HangmanArt.logo , "\n\n")
print("Welcome to the Hangman Game !!")

randomWord = random.choice(HangmanWord.word_list).lower()

outputList = []

for _ in range(len(randomWord)):
    outputList.append("_")
print(" ".join(map(str,outputList)))



life = 6

while True:
    
    word = input("\nGuess a lettar !  \n")
    flag = 0
    clear()
    if word in outputList:
        print("You already guess this word 😂 !!")

    for i in range(len(randomWord)):
        if word == randomWord[i]:
            outputList[i] = word
            flag = 1
        outputString = " ".join(outputList)
    
    if flag == 0:
        life -=1
        print("Your Guess is WRONG 😱 !!")
    
    else:
        print("Your Guess is RIGHT 😎 !!")

    print(f"{outputString}              Life Remaning == {life}")
    print(HangmanArt.stages[life])

   
    gameover(outputList , life)

    