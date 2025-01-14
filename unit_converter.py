#Convert units from Km to Miles, Celcius to Fahrenheit etc

#Put the possible choices in a set so we can compare for invalid user input
choices = {"km", "miles", "c", "fh"}

#Set an initial is_running variable to True for our while loop
is_running = True

while is_running:
    #Get user input
    choice = input("Please enter the unit that you want to convert from: (Km/Miles, C/Fh)\n")

    #Check if the user input is valid,if not restart the loop again
    if choice not in choices:
        print("Please enter  valid unit to convert from!\n")
        continue
    #Get the amount to be converted from the user
    choice2 = float(input("Please enter the value you want to convert: "))

    #Check the user input and make the appropriate convertions
    if choice.lower() == "km":
        miles = choice2 * 0.621371
        print(f"The following value is {miles} Miles!")
    elif choice.lower() == "miles":
        km = choice2 * 1.60934
        print(f"The following value is {km} Km!")

    if choice.lower() == "c":
        fh = (choice2 * 1.8) + 32
        print(f"The following value is {fh} Fahrenheit!")
    elif choice.lower() == "fh":
        c = (choice2 - 32) * 5/9
        print(f"The following value is {c} Celcius!")

    #Ask the user if they want to continue converting
    retry = input("Do you want to continue converting units? y/n:\n")

    #If yes,then restart the while loop,if no then change the is_running variale to False so the loop ends
    if retry.lower() == "y":
        continue
    elif retry.lower() == "n":
        print("Thank you for using our unit converter! Have a nice day!")
        is_running = False