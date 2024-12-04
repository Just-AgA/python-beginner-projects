#Splitting an email to the username and domain

#Find the index of the @ symbol
email = input("Enter your email:\n")
index = email.index("@")

#Split the email address by slicing the string based on the index above
username = email[:index]
domain = email[index + 1:]

print(f"Your username is {username} and domain is {domain}")