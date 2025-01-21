def is_isogram(word):
    word = word.lower() 
    seen_letters = []  
    
    for letter in word: 
        if letter in seen_letters:  
            return False
        seen_letters.append(letter) 
    
    return True