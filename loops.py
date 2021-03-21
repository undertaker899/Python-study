# Example
product = 1
n = 5
for i in range(1, n+1):
    product = product * i
print("product of numbers = ", product)
# Loop for: and function range()

# Example
n = int(input('Enter your number:'))
for i in range(1, n+1):
    print('*' * i)
# Loop for: and function range()

# Example
number = 1
square = 1
while square < 1000:
    number = number + 1
    square = number ** 2
print("Max natural number with its square < 1000:", number-1)
# Loop while: and comparison operator

# Example
number = 1
square = 1
while True:
    number = number + 1
    square = number ** 2
    if square >= 1000:
        break
print("Max natural number with square < 1000:", number-1)
# Loop while:, statement break, logical operator, comparison operator and conditional statement

# Example
list_ = [-5, 2, 4, 8, 12, -7, 5]
index_negative = None
for i, value in enumerate(list_):
    if value < 0:
        print("Negative number:", value)
        index_negative = i
        print("New index of last negative number in list:", index_negative)
    else:
        print("Current positive number:", value)
print('---------------------------------------------')
print("Index of last negative number in list =", index_negative)
# Loop for:, data type None, comparison operator, function enumerate() and conditional statements

# Example
text = """
Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
“’Tis some visitor,” I muttered, “tapping at my chamber door—
            Only this and nothing more.”
"""
text = text.lower()
text = text.replace(" ", "")
text = text.replace("\n", "")
count = {}
for char in text:
    if char in count:
        count[char] = count[char] + 1
    else:
        count[char] = 1
for char, cnt in count.items():
    print(f"Symbol {char} appears in text {cnt} time/times")
# Dictionary, loop for:, f string, methods .lower, .replace and .items, logical operators and conditional statements

# Example
n = int(input('Enter your number:'))
while n > 1:
    if n % 2 == 0:
        n = n / 2
        if n == 1:
            print('Collatz conjecture is true')
            break
    else:
        n = ((n * 3 + 1) / 2)
        if n == 1:
            print('Collatz conjecture is true')
            break
# Loop while:, comparison operators, statement break and conditional statements

# Example
heads = 35
legs = 94
for r in range(heads+1):
    for ph in range(heads+1):
        if (r + ph) > heads or (r * 4 + ph * 2) > legs:
            continue
        if (r + ph) == heads and (r * 4 + ph * 2) == legs:
            print("Rabbits", r)
            print("Pheasants", ph)
            print("---")
# Loop for:, function range(), comparison and logical operators, statement continue and conditional statements
