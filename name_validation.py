name = input("Please enter your name: ")

if not name.isalpha() or len(name) >=12 or not name.find(" ") == -1:
    print("Please enter a valid and short name,without any spaces!")


print(name)