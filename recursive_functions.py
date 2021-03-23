# 1
def num_sum(n):
    if n == 1:
        return 1
    return n + num_sum(n-1)


print('Sum of numbers from 1 to your number = ', (num_sum(int(input('Enter your number: ')))))
# Example


# 2
def rec_fibb(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return rec_fibb(n - 1) + rec_fibb(n - 2)


print('Fibonacci number =', rec_fibb(int(input('Enter # of fibonacci number: '))))
# Example


# 3
def rev_string(string):
    if len(string) == 0:
        return ''
    return string[-1] + rev_string(string[:-1])


print(rev_string(str(input())))
# Example


# 4
def sum_of_num(n):
    if n < 10:
        return n
    return n % 10 + sum_of_num(n // 10)


print(sum_of_num(int(input('Enter your number: '))))
# Example
