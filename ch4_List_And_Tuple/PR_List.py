Mark = [ ]

#taking input from user and storing it in Mark list
S1 = int(input("Enter the number of students: "))
Mark.append(S1)
S2 = int(input("Enter the number of students: "))
Mark.append(S2)
S3 = int(input("Enter the number of students: "))
Mark.append(S3)
S4 = int(input("Enter the number of students: "))
Mark.append(S4)
S5 = int(input("Enter the number of students: "))
Mark.append(S5)

print(Mark)


#sorting the Mark list 
Sorting = sorted(Mark)
print("Sorted List is: ", Sorting)