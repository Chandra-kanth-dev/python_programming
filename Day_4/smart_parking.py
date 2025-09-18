from abc import ABC, abstractmethod


'''Smart Parking System:
• -----------Create classes Vehicle, ParkingSpot, and ParkingLot.
•----------------- Create multiple objects (vehicles, spots, parking lot).
• --------------Demonstrate object creation, attribute initialization, and method calls.
•--------- Make sensitive attributes private (e.g., license plate, owner name, spot status).
•----------- Provide getter/setter methods to access/update them safely.
•------------ Show that direct access fails but methods work.
• -------------Vehicle is the base class.


•------- Derived classes:
---------------Bike (extra attribute: helmet_required)
---------------Car (extra attribute: seats)
------------SUV (extra attribute: four_wheel_drive)
----------------Truck (extra attribute: max_load_capacity)
• --------------Each child class overrides display() to print its own details.
• --------------Create a list of different vehicle objects (Bike, Car, SUV, Truck).
• --------------Iterate and call display() → each object responds differently.
• -----------Implement a calculate_parking_fee() method:
-----------Bike → ₹20/hour
------------Car → ₹50/hour
---------------SUV → ₹70/hour
-----------Truck → ₹100/hour
•------------ Demonstrate runtime polymorphism by calling the method on different objects.
• -------------Create an abstract class/interface Payment (using abc module).
• ------------Define an abstract method process_payment(amount).
• ---------------Create child classes:
------------------CashPayment
---------------CardPayment
------------UPIPayment
• ------------------Demonstrate abstraction by processing payments differently (just print “Paid ₹X via UPI”).
Task 1: Vehicle Classes
Implement base and derived vehicle classes with encapsulation.
---------Override display() and calculate_parking_fee().
Task 2: ParkingSpot Class
Implement ParkingSpot with size restrictions (S, M, L, XL).
Methods: assign_vehicle(), remove_vehicle().
Ensure vehicle type fits correct spot size (Bike → S+, Car → M+, SUV → L+, Truck → XL only).
Task 3: ParkingLot Class
Store multiple parking spots.
Methods:
add_spot() → add new parking spots.
show_spots() → display all spots and their status.
park_vehicle(vehicle) → find suitable spot and park.
unpark_vehicle(vehicle) → remove from spot and calculate fee.
Task 4: Payment (Abstraction + Polymorphism)
When un-parking a vehicle, calculate fee (based on hours).
Ask user for payment method → process payment using appropriate child class.
Task 5: Main Program
Create a parking lot with mixed spots.
Create multiple vehicle objects.
Park/unpark vehicles.
Demonstrate encapsulation, inheritance, polymorphism, and abstraction throughout.'''
class Vehicle:
    def __init__(self, vehicle_id, vehicle_owner, vehicle_name, license_no):
        self.vehicle_id = vehicle_id
        self.__vehicle_owner = vehicle_owner   
        self.vehicle_name = vehicle_name
        self.__license_no = license_no         
    
    def get_vehicle_id(self):
        return self.vehicle_id

    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def get_owner_name(self):
        return self.__vehicle_owner

    def set_owner_name(self, name):
        self.__vehicle_owner = name

    def get_vehicle_name(self):
        return self.vehicle_name

    def set_vehicle_name(self, vehicle_name):
        self.vehicle_name = vehicle_name

    def get_license_no(self):
        return self.__license_no

    def set_license_no(self, license_no):
        self.__license_no = license_no
    def display(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Owner Name: {self.__vehicle_owner}")
        print(f"Vehicle Name: {self.vehicle_name}")
        print(f"License No: {self.__license_no}")
    def calculate_parking_fee(self,hours):
        pass



class ParkingLot:
    def __init__(self, name, location, capacity, available_spots):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.available_spots = available_spots

    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_available_spots(self):
        return self.available_spots

    def set_available_spots(self, available_spots):
        self.available_spots = available_spots
    def add_spot(self, spot):

        self.spots.append(spot)
        print(f"Spot {spot.spot_id} ({spot.size}) added to parking lot {self.name}")

    def show_spots(self):
        
        print(f"\nParking Lot: {self.name}")
        print("Spot ID | Size | Status")
        print("-----------------------")
        for spot in self.spots:
            print(f"{spot.spot_id}     | {spot.size}   | {spot.status}")

    def park_vehicle(self, vehicle):
        
        for spot in self.spots:
            if spot.status == "Free":  
                if spot.assign_vehicle(vehicle):
                    print(f"{vehicle.vehicle_type} parked successfully in {spot.spot_id}")
                    return
        print(f"No suitable spot available for {vehicle.vehicle_type}")

    def unpark_vehicle(self, vehicle):
            for spot in self.spots:
                if spot.vehicle == vehicle:
                    spot.remove_vehicle()
                    print(f"Parking fee for {vehicle.vehicle_type}: ₹50 (flat rate)")
                    return
                print(f"Vehicle {vehicle.vehicle_name} not found in parking lot.")

class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size          
        self.status = "Free"      
        self.vehicle = None       

    def assign_vehicle(self, vehicle):

        if self.status == "Occupied":
            print(f"Spot {self.spot_id} is already occupied.")
            return False


        if vehicle.vehicle_type == "Bike" and self.size in ["S", "M", "L", "XL"]:
            self.vehicle = vehicle
            self.status = "Occupied"
            print(f"Bike parked in spot {self.spot_id}")
            return True
        elif vehicle.vehicle_type == "Car" and self.size in ["M", "L", "XL"]:
            self.vehicle = vehicle
            self.status = "Occupied"
            print(f"Car parked in spot {self.spot_id}")
            return True
        elif vehicle.vehicle_type == "SUV" and self.size in ["L", "XL"]:
            self.vehicle = vehicle
            self.status = "Occupied"
            print(f"SUV parked in spot {self.spot_id}")
            return True
        elif vehicle.vehicle_type == "Truck" and self.size == "XL":
            self.vehicle = vehicle
            self.status = "Occupied"
            print(f"Truck parked in spot {self.spot_id}")
            return True
        else:
            print(f"{vehicle.vehicle_type} does not fit in spot {self.spot_id} ({self.size})")
            return False

    def remove_vehicle(self):
        if self.status == "Free":
            print(f"Spot {self.spot_id} is already empty.")
            return None
        print(f"Vehicle removed from spot {self.spot_id}")
        removed_vehicle = self.vehicle
        self.vehicle = None
        self.status = "Free"
        return removed_vehicle

spot = ParkingSpot("A1", "EV", "Free", 1)


print("Spot ID (getter)", spot.get_spot_id())
print("Spot Type (getter)", spot.get_spot_type())
print("Spot Status (getter)", spot.get_status())

# Direct access to private variable  failed
try:
    print("Spot Status ", spot.__status)  
except :
    print("Direct access failed:", e)

spot.set_status("Occupied")
print("Spot Status after setter:", spot.get_status())
class Bike(Vehicle):
    def __init__(self, vehicle_id, vehicle_owner, vehicle_name, license_no,helmet_required):
        super(). __init__(self, vehicle_id, vehicle_owner, vehicle_name, license_no)
        self.helmet_required=helmet_required
    def display(self):
        super().display()
        print("Helmet required =", self.helmet_required)
    def calculate_parking_fee(self,hours):
        return 20*hours








class Car(Vehicle):
    def __init__(self, vehicle_id, vehicle_owner, vehicle_name, license_no,seats):
        super(). __init__(self, vehicle_id, vehicle_owner, vehicle_name, license_no)
        self.seats=seats
    def display(self):
        super().display()
        print("Seats =", self.seats)
    def calculate_parking_fee(self,hours):
        return 50*hours
        
class SUV(Vehicle):
    def __init__(self, vehicle_id, vehicle_owner, vehicle_name, license_no,four_wheel_drive):
        super(). __init__(self, vehicle_id, vehicle_owner, vehicle_name, license_no)
        self.four_wheel_drive=four_wheel_drive
    def display(self):
        super().display()
        print("Four wheel drive =", self.four_wheel_drive)
    def calculate_parking_fee(self,hours):
        return 70*hours

class Truck(Vehicle):
    def __init__(self, vehicle_id, vehicle_owner, vehicle_name, license_no,capacity):
        super(). __init__(self, vehicle_id, vehicle_owner, vehicle_name, license_no)
        self.capacity=capacity
    def display(self):
        super().display()
        print("Capacity =", self.capacity)
    def calculate_parking_fee(self,hours):
        return 100*hours
    #demonstrated run time polymophism
li =[Bike("1","abc","honda","1234",True),Car("2","def","audi","5678",5),SUV("3","ghi","ford","9101",True),Truck("4","jkl","volvo","1121",10000)]
for i in li:
    i.display()
    print("-----")
    print("Parking fee for 3 hours:",i.calculate_parking_fee(3))
    print("-----")  
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
        
class CashPayment(Payment):
    def pay(self,amount):
        print("paid ",amount,"in cash")

class CardPayment(Payment):
    def pay(self,amount):
        print("paid ",amount,"through debit/credit card")

class UPIPayment(Payment):
    def pay(self,amount):
        print("paid ",amount,"through upi")


