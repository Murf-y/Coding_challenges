from collections import Counter
def duplicate_encode(word):
    word = word.lower()
    word = list(word)
    count = Counter(word)
    result = ""
    for char in word:
        if count[char] == 1:
            result += "("
        else:
            result += ")"
    return result
