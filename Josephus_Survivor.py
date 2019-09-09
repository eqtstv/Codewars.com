def josephus_survivor(n,k):
    surv = [x for x in range(1, n+1)]
    step = k
    x = k
    while len(surv) != 1:
        while x > len(surv):
            x = x-len(surv)
        del surv[x-1]
        x += step-1

    return surv[0]