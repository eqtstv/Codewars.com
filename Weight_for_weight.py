def order_weight(strng):
    kgs = strng.split(' ')
    
    def to_weight(kg):
        return sum(int(i) for i in str(kg))
        
    weights = list(map(to_weight, kgs))   
    sorted_list = [x for _,x in sorted(zip(weights, kgs))]
    sorted_string = ' '.join(sorted_list)
    return sorted_string