#with return statement
def square(n):
    print(n * n)
square(4)


#without return statement
def square(n):
    return n * n
result = square(4)
print(result)   
print(square(5))  #directly printing the return value


