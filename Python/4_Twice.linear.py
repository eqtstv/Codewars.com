import bisect
from collections import OrderedDict

def dbl_linear(n):
    cache = [1]
    i = 1
    counter = cache[i-1]
    
    while len(cache) < n+n:
        u1 = (2 * counter) + 1
        u2 = (3 * counter) + 1
        
        bisect.insort(cache, u1)
        bisect.insort(cache, u2)
        
        counter = cache[i]
        i += 1
        
    cache = list(OrderedDict.fromkeys(cache)) 
    
    return cache[n]
