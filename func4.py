def Hangaroo(secretWord):
    
    life = 5
    lettersGuesssed = ['']
    lettersGuesssed = lettersGuesssed.lower()
    
    print("Welcome to Hangaroo! Are you ready to guess the secret word?")
    print("You now have ", life, "chance/s to guess.")
    
    while isWordGuessed(secretWord,lettersGuessed) == False:
        getGuessWord(secretWord,lettersGuessed)
        lettersGuessed = input("Enter one letter: ")
        lettersGuesssed = lettersGuesssed.lower() 
        
        if isWordGuessed(secretWord,lettersGuessed) == False:
            life = life -1
            print("Engk! Try again.")
            print("You now have ", life, "chance/s to guess.")
            if life == 0:
                print("You now have ", life, "chance/s to guess.")
                print("The word was: ", secretWord)
                print("GAMEOVER")
            
        else:
            print("Great Job! Keep it up!")
            print("You now have ", life, "chance/s to guess.")
            break
        
def isWordGuessed(secretWord,lettersGuessed):
    
    
    for let in secretWord:
        if let not in lettersGuessed:
          return False
        else:
          return True
      
def getGuessedWord (secretWord, lettersGuessed):
    
        x = secretWord
        
        for char in secretWord:
            if char not in lettersGuessed:
                x = x.replace(char," _ ")
        
        return x