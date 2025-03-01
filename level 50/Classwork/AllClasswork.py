                                 # 1

def is_isogram(string):
    seen_letters = set()
    for letter in string.lower():
        if letter in seen_letters: return False
        seen_letters.add(letter)
    return True


                                  # 2

def accum(text):

    result = ""
    

    for position in range(len(text)):
        
        character = text[position]
        
        repeated_char = character.upper() + character.lower() * position
        
        result += repeated_char
        
        if position < len(text) - 1:
            result += "-"
    
    return result



                