# Objective:
# This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker
# Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement:
# Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def new_ticket():
    customer_name= input("Please Enter Customer Name")
    issue= input("Please Enter the issue")
    new_ticket_num= len(service_tickets)+1
    if new_ticket_num<100:
        if new_ticket_num<10:
            service_tickets["Ticket"+"00"+str(new_ticket_num)]={"Customer": customer_name, "Issue": issue, "Status": "open"}
        else:
            service_tickets["Ticket"+"0"+str(new_ticket_num)]={"Customer": customer_name, "Issue": issue, "Status": "open"}
    else:
        service_tickets["Ticket"+str(new_ticket_num)]={"Customer": customer_name, "Issue": issue, "Status": "open"}

def update_ticket(ticket_num):
    if ticket_num in service_tickets:
        while True:
            status = input("Enter New Status (open/closed)")
            if status in ["open", "closed"]:
                service_tickets[ticket_num]["Status"] = status
                print(f"{ticket_num}'s status has been updated to {status}")
                break
            else:
                print("Invalid status. Please enter 'open' or 'closed'.")
    else:
        print(f"No ticket found")
    
def display_all():
    for ticket, info in service_tickets.items():
        print(f"{ticket} - {info}")

def display_filtered(status):
    for ticket, info in service_tickets.items():
        if info["Status"]==status:
            print(f"{ticket} - {info}")

