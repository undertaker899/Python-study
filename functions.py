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
