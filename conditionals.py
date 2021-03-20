# Example
a = int(input())
leap_year = a % 4 == 0
print(leap_year is True)
# Comparison and logical Operators


n = input()
print('3' in str(n) and '7' in str(n))
# Logical Operators

# Example
a = int(input("a:"))
b = int(input("b:"))
if a % 2 == 1 and b % 2 == 1:
    print('a and b are odd numbers')
else:
    print('a or b is even number')
# Comparison operators and conditional Statements if: and else:

# Example
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("First quarter")
if x > 0 and y < 0:
    print("Fourth quarter")
if x < 0 and y > 0:
    print("Second quarter")
if x < 0 and y < 0:
    print("Third quarter")
# Comparison and logical operators and conditional statement if:

# Example
speed = int(input("Enter wind speed:"))
if speed in [0, 1, 2, 3, 4]:
    print('Weak wind')
elif speed in [5, 6, 7, 8, 9, 10]:
    print('Moderate wind')
elif speed in [11, 12, 13, 14, 15, 16, 17, 18]:
    print('Strong wind')
elif speed >= 19:
    print('Hurricane')
# Comparison and logical operators and conditional statements if: and elif:

# Example
user = input("Enter your username:")
password = input("Enter your password:")
user_database = {'user': 'password', 'iseedeadpeople': 'greedisgood', 'hesoyam': 'tgm'}
if user in user_database.keys():
    if password in user_database.values():
        print('Welcome', user)
else:
    print('No user with such name or password')
# Dictionary, methods .keys() and .values(), logical operators and conditional statements if: and else:

# Example
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
if a < 45 and b >= 45 and c >= 45:
    print('One number is less than 45')
elif a >= 45 and b < 45 and c >= 45:
    print('One number is less than 45')
elif a >= 45 and b >= 45 and c < 45:
    print('One number is less than 45')
else:
    print('More than one number is less than 45')
# Comparison and logical operators and conditional statements if:, elif: and else:

# Example
a = int(input())
if -10 <= a <= 0:
    print('a is in interval [-10:0]')
elif 2 <= a <= 15:
    print('a is in interval [2:15]')
else:
    print("a is not in either interval")
# Comparison operators and conditional statements if:, elif: and else

# Example
a = int(input('Enter two digit number:'))
if a % 10 == 5 or a // 10 == 5:
    print("a has 5 in it")
else:
    print("a has no 5 in it")
# Comparison and logical operators and conditional statements if: and else

# Example
L = [1, 2, 3, 3]
if len(L) == len(set(L)):
    print('All symbols are unique')
else:
    print('Not all symbols are unique')
# Comparison operators, functions len() and set() and conditional statements if: and else

# Example
number = int(input())
string1 = str(number)
string2 = string1[::-1]
if string1 == string2:
    print('Number is palindrome')
else:
    print('Number is not palindrome')
# Comparison operators, slices, function str() and conditional statements if: and else
