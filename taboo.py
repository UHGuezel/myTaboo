import csv
import random
from unicodedata import name

class Word:
    all = []
    shuffled = []
    absolutePos = 0
    previousPos = 0
    currPos = 0
    
    def __init__(self, index: int, toGuess: str, notAllowed: str):
        self.index = index
        self.toGuess = toGuess
        self.notAllowed = notAllowed
        
        Word.all.append(self)
        
    @classmethod
    def getCurrent(cls):
        return(cls.all[cls.absolutePos])
    
    @classmethod
    def goNext(cls):
        cls.previousPos = cls.currPos
        cls.currPos += 1
        if cls.currPos > len(cls.all):
            print("The Game is finished")
            exit()
        cls.absolutePos = cls.shuffled[cls.currPos]
        
    @classmethod
    def goPrevious(cls):
        cls.previousPos = cls.currPos
        cls.currPos -= 1
        if cls.currPos <= 0:
            cls.currPos += 1
            print("You are at the beginning")
        cls.absolutePos = cls.shuffled[cls.currPos]
        
    @classmethod
    def getDeckSize(cls):
        deckSize = len(Word.all)
        return (deckSize)
    
    @classmethod
    def createDeck(cls):
        cls.shuffled = (list(range(0, Word.getDeckSize())))
        return(cls.shuffled)
        
    @classmethod 
    def shuffleWords(cls):
        cls.shuffled = cls.createDeck()
        return(random.shuffle(cls.shuffled))
        
    @classmethod
    def getFromCSV(cls):
        with open('words.csv', 'r') as content:
            reader = csv.DictReader(content)
            words = list(reader)
        for word in words:
            Word(
                index=word.get('index'),
                toGuess=word.get('toGuess'),
                notAllowed=word.get('notAllowed')
            )
            
    def __repr__(self):
        return f"Word({self.index}, {self.toGuess}, {self.notAllowed})"



def main(): 
    Game = Word    
    Game.getFromCSV()
    Game.shuffleWords()

    userInput = ""

    Game.goNext()
    while (userInput != exit):
        
        Game.getCurrent()
        userInput = input("Please enter your move: ")
        if userInput == "next":
            Game.goNext()
            notAllowed = Game.all[Game.absolutePos].notAllowed.replace(',','\n')
            print(f"Describe:\n{Game.all[Game.absolutePos].toGuess}\nDO NOT USE:\n{notAllowed}")
        elif userInput == "previous":
            Game.goPrevious()
        elif userInput == "exit":
            exit()
        else:
            continue
    
if __name__ == '__main__':
    main()