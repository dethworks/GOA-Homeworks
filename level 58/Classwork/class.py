def lottery(s):
    seen_numbers = set()
    result = []

    for char in s:
        if char.isdigit() and char not in seen_numbers:
            seen_numbers.add(char)
            result.append(char)

    if result:
        return "".join(result)
    else:
        return "One more run!"
                                       #2


def longest_word(string_of_words):
    words = string_of_words.split()
    longest = ""