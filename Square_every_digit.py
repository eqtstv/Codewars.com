def square_digits(num):
    sol_list = list(map(lambda x: x**2, [int(i) for i in str(num)]))
    sol = ''.join(map(str, sol_list))
    return int(sol)