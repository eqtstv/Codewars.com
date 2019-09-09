import collections

def anagrams(word, words):
    word_list = list(word)
    sol = [comp for comp in words if collections.Counter(word_list) == collections.Counter(list(comp))]
    return sol