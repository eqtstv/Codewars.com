import string
from functools import reduce

def is_pangram(s):
    repls = (' ', ''), (',', ''), ('!', ''), ('.', '')
    alph = set('abcdefghijklmnopqrstuvwxyz')
    nums = set('1234567890')
    comp_set = set(reduce(lambda a, kv: a.replace(*kv), repls, s).lower())     
    comp_set = comp_set - nums
    
    if comp_set == alph:
        return True
    else:
        return False