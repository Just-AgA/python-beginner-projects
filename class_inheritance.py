#Create a class that inherits all variables and methods of the parent class

#Parent class
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


#Child class,where we use the super() method to inherit from the parent class
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
        

#Create an instance of the child class
bus = Bus("School Volvo", 180, 12)
print(f"Vehicle Name: {bus.name}",f"Speed: {bus.max_speed}", f"Mileage: {bus.mileage}")
