from math import factorial
def get_factoradic(integer):
    factoradic = []
    i = 1
    while integer != 0: 
        factoradic.insert(0, integer%i)
        integer = integer // i
        i += 1
    return factoradic
    
def middle_permutation(string):
    mid = int(factorial(len(string))/2)-1
    mid_fct = get_factoradic(mid)
    str_list = list(string)
    str_list.sort()
    mid_perm = [str_list.pop(i) for i in mid_fct]
    
    if len(string) == 2:
        sor_s = list(string)
        sor_s.sort()
        return ''.join(sor_s)
    else:
        return ''.join(mid_perm)