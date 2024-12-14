#Use the method overload and super() function to inherit from the parent class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

#Overload the fare() method so the Bus class adds a 10% to the seats in the fare
class Bus(Vehicle):
    def __init__(self,name,mileage,capacity):
        super().__init__(name,mileage,capacity)

    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

bus = Bus("School Volvo", 12, 50)
print(f"Total bus fare is: {bus.fare()}")