# Example
def print_2_add_2():
    print(2+2)


print_2_add_2()
# Function


# Example
def hello_world():
    print("Hello World")


hello_world()
# Function


# Example
def division(a, n):
    if a % n == 0:
        print('n is divider of a')
    else:
        print('n is not divider of a')


division(2, 4)
# Function, comparison operator and conditional statements


# Example
def reverse_ladder(n):
    for i in range(n, 0, -1):
        print('*' * i)


reverse_ladder(5)
# Function, logical operator, function range() and loop for:


# Example
def div_cnt(a, count=0):
    for i in range(1, a+1):
        if a % i == 0:
            count = count + 1
    return count


print(div_cnt(100))
# Function, loop for:, function range(), conditional statement and statement return


# Example
def palindrome(s):
    s = s.lower()
    s = s.replace(' ', '')
    if s == s[::-1]:
        print('Input is palindrome')
    else:
        print('Input is not palindrome')


palindrome(input("Enter your string:"))
# Function, methods .lower and .replace, comparison operator, slice and conditional statements


# Example
x = 3


def func():
    global x
    print(x)
    x = 5
    x = x + 5
    return x


func()
print(x)
# Function, scope


# Example
def get_mul_func(m):
    nonlocal_m = m

    def local_mul(n):
        return n * nonlocal_m

    return local_mul


two_mul = get_mul_func(2)
print(two_mul(int(input("Enter your number:"))))
# Functions, scope and statements return


# Example
def multiple(*nums):
    mul = 1
    for n in nums:
        mul = mul * n
    return mul


print(multiple(2, 2, 2, 2))
# Function, unpacking arguments, loop for: and statement return


# Example
def correct_func(name_arg=None):
    if name_arg is None:
        name_arg = []
    print(name_arg)
    name_arg.append('first change')
    print(name_arg)
    name_arg.append('second change')
    print(name_arg)


correct_func(name_arg=[123, 1])
# Function, data type None, method .append and list type as argument


# Example
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


print('Factorial of this number =', fact(int(input('Enter your number: '))))
# Recursive function, comparison operator, conditional statement and statements return


# Example
def rec_fibb(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return rec_fibb(n - 1) + rec_fibb(n - 2)


print('Fibonacci number =', rec_fibb(int(input('Enter # of fibonacci number: '))))
# Recursive function, comparison operator, conditional statements and statements return
