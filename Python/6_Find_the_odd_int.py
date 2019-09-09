def find_it(seq):
    seq_set = set(seq)
    for num in seq_set:
        if seq.count(num)%2 != 0:
            return num