def get_count(sentence):
    return sum(sentence.count(v) for v in "aeiou")