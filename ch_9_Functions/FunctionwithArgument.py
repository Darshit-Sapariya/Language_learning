# Function without Argument
def sum ():
    print("Function without Argument")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a + b
    print("The sum is:", c)

sum()
print("\n")
print("--------------------------------------------------")
print("\n")

# Function with Argument
def sum (a, b):
    c = a + b
    print("Function with Argument")
    print("first number is:", a)
    print("second number is:", b)
    print("The sum is:", c) 
sum(5, 10)

print("\n")
print("--------------------------------------------------")
print("\n")

# Function with Default Argument
def sum (a=5, b=10):    
    c = a + b
    print("first number is:", a)
    print("second number is:", b)
    print("The sum is:", c) 
    print("Function with Default Argument")
sum()  # using default values
print("")
sum(15, 25)  # using provided values
