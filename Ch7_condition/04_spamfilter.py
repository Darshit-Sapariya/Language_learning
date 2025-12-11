p1= "buy now"
p2= "subscribe now"
p3= "click this link"
p4= "payment now"

messages = input("Enter the email messages: ").lower()

if (p1 in messages) or (p2 in messages) or (p3 in messages) or (p4 in messages):
    print("This is a spam email.")  
else:
    print("This is not a spam email.")
