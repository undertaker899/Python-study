# 1
n = int(input('Enter your number:'))
for i in range(1, n+1):
    print('*' * i)
# Example


# 2
number = 1
square = 1
while True:
    number = number + 1
    square = number ** 2
    if square >= 1000:
        break
print("Max natural number with square < 1000:", number-1)
# Example


# 3
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
# Example


# 4
text = input()
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
# Example


# 5
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
# Example


# 6
heads = 35
legs = 94
for r in range(heads+1):
    for ph in range(heads+1):
        if (r + ph) > heads or (r * 4 + ph * 2) > legs:
            continue
        if (r + ph) == heads and (r * 4 + ph * 2) == legs:
            print("Rabbits:", r)
            print("Pheasants:", ph)
# Example
