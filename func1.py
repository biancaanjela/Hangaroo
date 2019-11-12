def isWordGuessed(secretWord,lettersGuessed):
    
    
    for let in secretWord:
        if let not in lettersGuessed:
          return False
        else:
          return True