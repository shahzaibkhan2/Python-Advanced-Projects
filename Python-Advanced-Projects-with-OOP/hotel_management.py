# Importing necessary modules
import datetime

# Defining a class for managing hotel rooms
class Room:
    def __init__(self, number, limit, price, available=True):
        self.number = number
        self.limit = limit
        self.price = price
        self.available = available
        self.reservations = []

    # Function for reserving rooms
    def reserve(self, checkin, checkout):
        self.reservations.append(Reservation(checkin, checkout))
        self.available = False

    def checkout(self):
        self.available = True

    # String format magic method
    def __str__(self):
        return f"Room {self.number}, {self.capacity} people, ${self.price} per night"

# Define a class for managing hotel reservations
class Reservation:
    def __init__(self, checkin, checkout):
        self.checkin = checkin
        self.checkout = checkout

# Defining a class for managing the hotel
class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, number, capacity, price):
        room = Room(number, capacity, price)
        self.rooms.append(room)

    def find_available_rooms(self, checkin, checkout):
        available_rooms = []
        for room in self.rooms:
            if room.available:
                conflicts = False
                for reservation in room.reservations:
                    if (checkin >= reservation.checkin and checkin < reservation.checkout) or \
                       (checkout > reservation.checkin and checkout <= reservation.checkout) or \
                       (checkin < reservation.checkin and checkout > reservation.checkout):
                        conflicts = True
                        break
                if not conflicts:
                    available_rooms.append(room)
        return available_rooms

    def reserve_room(self, room_number, checkin, checkout):
        for room in self.rooms:
            if room.number == room_number:
                if room.available:
                    room.reserve(checkin, checkout)
                    return True
                else:
                    return False
        return False

# Example for usage
hotel = Hotel("International Pearl Hotel")
hotel.add_room(101, 2, 100)
hotel.add_room(102, 4, 200)
hotel.add_room(103, 4, 200)

available_rooms = hotel.find_available_rooms(datetime.date(2023, 5, 1), datetime.date(2023, 5, 3))
for room in available_rooms:
    print(room)

if hotel.reserve_room(101, datetime.date(2023, 5, 1), datetime.date(2023, 5, 3)):
    print("Reservation successful!")
else:
    print("Room not available.")

available_rooms = hotel.find_available_rooms(datetime.date(2023, 5, 1), datetime.date(2023, 5, 3))
for room in available_rooms:
    print(room)
