class Room:
    """
    This is a class to describe a room.
    """
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():
    room_list = []
    room = Room("You are in the living room. There is a couch and a tv. There is a door to the east.", None, 1, None, None)
    room_list.append(room)
    room = Room("You are in the Hallway. There is a lamp and a key.", 2, 4, 3, 0)
    room_list.append(room)
    room = Room("You are in the library. There is a book and a chair.", None, 5, 1, None)
    room_list.append(room)
    room = Room("You are in the bedroom. There is a closet and a bed.", 1, None, None, None)
    room_list.append(room)
    room = Room("You are in the kitchen. There is a fridge and a drawer.", None, None, 4, 2)
    room_list.append(room)
    room = Room("You are in the dining room. There is a banana and a chair.", 5, None, None, 1)
    room_list.append(room)

    current_room = 0
    done = False

    while done = False:
        print()
        print(room_list[current_room].description)
        user_choice = input("Which direction?")

    if user_choice.lower() == "n" or user_choice.upper()== "North":
        next_room = room_list[current_room].north
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room

    elif user_choice.lower() == "e" or user_choice.upper() == "East"
        next_room = room_list[current_room].east
        if next_room == None:
            print("You can't go that way.")

    elif user_choice.lower() == "s" or user_choice.upper() == "South"
        next_room = room_list[current_room].south
        if next_room == None:
            print("You can't go that way.")

    elif user_choice.lower() == "w" or user_choice.upper() == "West"
        next_room = room_list[current_room].west
        if next_room == None:
            print("You can't go that way.")
    else:
        print("I don't understand that command.")

main()