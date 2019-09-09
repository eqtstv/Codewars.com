def iq_test(numbers):
    nums = list(map(lambda x: int(x), numbers.split()))
    boolean = [True if i%2 == 0 else False for i in nums]

    if boolean.count(True) == 1:
        return boolean.index(True)+1
    else:
        return boolean.index(False)+1