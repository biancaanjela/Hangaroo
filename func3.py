def getAvailableLetters(lettersGuessed):
    
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        y = lettersGuessed
        
        for x in alphabet:
            if x in str(lettersGuessed):
               y = y.replace(x, '')    
                
        return y
