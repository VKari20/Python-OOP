# Base class - Vehicle
class Vehicle:
    def move(self):
        pass  # To be implemented by subclasses

# Car class (inherits from Vehicle)
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Bike class (inherits from Vehicle)
class Bike(Vehicle):
    def move(self):
        print("Riding 🚲")

# Plane class (inherits from Vehicle)
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Create objects
car = Car()
bike = Bike()
plane = Plane()

# Test polymorphism
for vehicle in [car, bike, plane]:
    vehicle.move()  # Each subclass defines its own version of move()
