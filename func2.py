def getGuessedWord (secretWord, lettersGuessed):
    
        x = secretWord
        
        for char in secretWord:
            if char not in lettersGuessed:
                x = x.replace(char," _ ")
        
        return x