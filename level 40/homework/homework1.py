def remove_duplicate_words(s):
    words = s.split()  
    unique_words = []  
    
    for word in words:
        if word not in unique_words:
            unique_words.append(word)  

    result = ' '.join(unique_words)  
    return result
