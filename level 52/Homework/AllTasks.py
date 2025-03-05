                                          # 1
def table(num):
    result = ''
    for i in range(1, 11):
        multiply = num * i
        result += f'{num} x {i} = {multiply}\n'
    
    return result.strip()

                                          # 2 
def to_str(arr):
    text = []
    for x in arr:
        text.append(str(x))
    
    return ','.join(text)

                                          # 3
def clean_str(text):
    new_text = ''
    for char in text:
        if not char.isdigit():
            new_text += char
    
    return new_text

                                          # 4 
def no_repeat(words):
    split_words = words.split()
    unique_words = []
    
    for word in split_words:
        if len(unique_words) == 0:
            unique_words.append(word)
        
        if word != unique_words[-1]:
            unique_words.append(word)
    
    return ' '.join(unique_words)

                                            # 5
def range_val(numbers):
    return max(numbers) - min(numbers)