def capitals(word):
    capital_1 = []  

    for i in range(len(word)):  # 
        if word[i].isupper():  
            capital_1.append(i) 
            
    return capital_1