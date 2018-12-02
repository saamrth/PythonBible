vowels = 0
consonants = 0


for letter in  "new york knicks":
    if letter.lower() in "aeiuo":
        vowels=vowels+1
        
        

    elif letter == " ":
        pass
    else:
        consonants= consonants+1
        
print("there are {} vowels".format(vowels))

print("there are {} consonants".format(consonants))    
