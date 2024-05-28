# Objective:
# The aim of this assignment is to deepen your knowledge and practical skills in handling complex data structures using Python. You will work on real-world inspired tasks that require advanced manipulation of dictionaries, nested collections, and implementing custom functions for specific data processing needs.

# Task 1: Hotel Room Booking Tracker
# Enhance your ability to work with nested collections by developing a system to track room bookings for a hotel.

# Problem Statement:
# Develop a program that:

# Manages room bookings, where each room has details such as booking status (booked/available) and customer name.
# Implement functions to:
# Book a room (mark as booked and assign to a customer).
# Check-out a customer (mark room as available and remove customer name).
# Display the status of all rooms.
# Start with this initial hotel room structure:

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def display_all():
    for room, info in hotel_rooms.items():
        if info["customer"]:
            print(f"Room #{room}: {info["status"]} by {info["customer"]}")
        else:
            print(f"Room #{room}: is {info["status"]}")

def add_booking(room,customer_name):
    if room in hotel_rooms:
        if hotel_rooms[room]["status"]=="available":
            hotel_rooms[room]={"status":"booked", "customer":customer_name}
        else:
            print(f"Room #{room} is already booked")
    else:
        print(f"Room #{room} doesn't exist")

def check_out(room):
    if room in hotel_rooms:
        if hotel_rooms[room]["status"]=="booked":
            hotel_rooms[room]={"status":"available", "customer":""}
        else:
            print(f"Room #{room} is already vacant")
    else:
        print(f"Room #{room} doesn't exist")



display_all()
print()
add_booking("101","Josh")
display_all()
print()
check_out("101")
display_all()