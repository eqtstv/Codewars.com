def is_pangram(s):
    alph = set('abcdefghijklmnopqrstuvwxyz')
    s_set = set(s.lower())

    if alph - alph.intersection(s_set):
        return False
    else:
        return True