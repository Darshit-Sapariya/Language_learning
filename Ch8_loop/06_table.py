# Multiplication table in normal order
n = int(input("Enter a number to print its table: "))

for i in range(1, 11):
    p = n * i
    print(f"{n} x {i} = {p}")




## Reverse order multiplication table
n = int(input("Enter a number to print its table: "))

for i in range(10, 0, -1):
    p = n * i
    print(f"{n} x {i} = {p}")
