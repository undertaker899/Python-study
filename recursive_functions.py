# 1
def num_sum(n):
    if n == 1:
        return 1
    return n + num_sum(n-1)


print('Sum of numbers from 1 to your number =', (num_sum(int(input('Enter your number: ')))))
# Example


# 2
def rec_fibb(n):
    if n == 1 or n == 2:
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


# 5
def min_list(list_arg):
    if len(list_arg) == 1:
        return list_arg[0]
    elif list_arg[0] < min_list(list_arg[1:]):
        return list_arg[0]
    else:
        return min_list(list_arg[1:])


print('Minimal element in your list: ', min_list(input('Enter your list: ')))
# Example


# 6
def rev_num(a_num, result=0):
    if a_num:
        return rev_num(a_num // 10, result * 10 + a_num % 10)
    else:
        return result


print(rev_num(int(input('Enter your number without zero in it: '))))
# Example


# 7
def equal(number1, number2):
    if number2 < 0:
        return False
    elif number1 < 10:
        return number1 == number2
    else:
        return equal(number1 // 10, number2 - number1 % 10)


print(equal(int(input('First number: ')), int(input('Second number: '))))
# Example
