hotel_rooms = {
    101: "Available",
    102: "Available",
    103: "Available",
    201: "Available",
    202: "Available",
    203: "Available"
}
def display_rooms():
    print("\n--- Current Room Status ---")
    for room_num, status in hotel_rooms.items():
        print(f"Room {room_num}: {status}")
    print("--------------------------")
def book_room(room_num, guest_name):
    """Books a room for a guest."""
    if room_num not in hotel_rooms:
        print(f"\n Error: Room {room_num} does not exist.")
    elif hotel_rooms[room_num]=="Available":
        hotel_rooms[room_num]=guest_name
        print(f"\n Success: Room {room_num} booked for *{guest_name}*.")
    else:
        current_guest=hotel_rooms[room_num]
        print(f"\n Room {room_num} is currently occupied by *{current_guest}*. Cannot book.")
def check_out(room_num):
    """Checks out a guest and makes the room Available."""
    if room_num not in hotel_rooms:
        print(f"\nError: Room {room_num} does not exist.")
    elif hotel_rooms[room_num]!="Available":
        guest_name=hotel_rooms[room_num]
        hotel_rooms[room_num]="Available"
        print(f"\n Success: *{guest_name}* checked out from Room {room_num}. Room is now Available.")
    else:
        print(f"\n Room {room_num} is already Available. No one to check out.")
def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        print("\n=== Hotel Management System ===")
        print("1. Display All Room Status")
        print("2. Book a Room")
        print("3. Check Out Guest")
        print("4. Exit")
        choice=input("Enter your choice (1-4): ")        
        try:
            if choice=='1':
                display_rooms()
            elif choice=='2':
                room=int(input("Enter room number to book: "))
                name=input("Enter guest name: ").strip()
                if name: # Simple check to make sure name isn't empty
                    book_room(room, name)
                else:
                    print("\nError: Guest name cannot be empty.")
            elif choice=='3':
                room=int(input("Enter room number to check out: "))
                check_out(room)
            elif choice=='4':
                print("\nGoodbye! Thank you for using the Hotel Management System.")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number for the room.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
if __name__=="__main__":
    main_menu()
