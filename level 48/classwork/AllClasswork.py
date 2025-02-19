                                    # 1

def xo(s):
    s = s.lower()
    return s.count("x") == s.count("o")                           



                                     # 2

def find_short(s):
    words = s.split()
    word_lengths = []

    for word in words:
        length = len(word)
        word_lengths.append(length)

    shortest_length = min(word_lengths)
    return shortest_length

                                      # 3

def solution(string, ending):
    return string.endswith(ending)