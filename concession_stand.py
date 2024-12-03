#Simulating a concessionstand in a cinema

#Create a dictionary with all the items available
menu = {
    "pizza": 3.5,
    "coca-cola": 1.2,
    "burger": 2,
    "lemonade": 3.3
}

#Create an empty list where you will put the cart and a total value initialized to 0
cart = []
total = 0

#Iterate over evey item in the dictionary
print("----------MENU----------")
for key, value in menu.items():
    print(f"{key:15}: ${value:.2f}")
print("------------------------")

while True:
    food = input("Enter your food of choice(q to quit): ").lower()

    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print(f"Your selection is: ")
for food in cart:
    total += menu.get(food)
    print(food, end= " ")

print(f"\nYour total price is {total}")
