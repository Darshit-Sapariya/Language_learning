registered_emails = {"a@gmail.com", "b@gmail.com"}
new_email = "ad@gmail.com"

if new_email in registered_emails:
    print("Already exists")
else:
    registered_emails.add(new_email)
    print("New Registered Successfully")