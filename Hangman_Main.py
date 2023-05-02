import random
from WordList import words

running = True
tempNum = 0

RandomHangmanWord=random.choice(words).lower()
print(RandomHangmanWord)

blanks='_' * len(RandomHangmanWord)



while (running):
    print(blanks)
    PlayerGuess=input("Type a letter that you think is in the computers word: ")
    if PlayerGuess.encode().isalpha() and len(PlayerGuess)==1 :
        for i in range(len(RandomHangmanWord)):
            if RandomHangmanWord[i] == PlayerGuess.lower() :
                tempNum = tempNum + 1
                blanks = blanks[:i] + RandomHangmanWord[i] + blanks[i+1:]
                
    else:
        print("You have to type an english character. Not number symbols or series of letters.")
    if tempNum == len(RandomHangmanWord) or PlayerGuess == 'exit':
        running = False
        print("You found the word" + RandomHangmanWord)
        
    

