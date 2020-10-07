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
    room = Room("You are in the living room. There is a couch and an unplugged tv playing a horror movie.\nThere is a door to the east.", None, 1, None, None)
    room_list.append(room)
    room = Room("You are in the hallway.\nThere is a floating lamp and a key.", 2, 4, 3, 0)
    room_list.append(room)
    room = Room("You are in the library.\nThere is a scary book and a chair.", None, 5, 1, None)
    room_list.append(room)
    room = Room("You are in the bedroom.\nThere is a closet full of skeletons and a coffin.", 1, None, None, None)
    room_list.append(room)
    room = Room("You are in the kitchen.\nThere is a fridge and butcher knives.", None, None, 4, 2)
    room_list.append(room)
    room = Room("You are in the dining room.\nThere is a banana and spiderwebs.", 5, None, None, 1)
    room_list.append(room)

    current_room = 0
    done = False
    print( "You are in a haunted castle.")
    while not done:
        print()
        print(room_list[current_room].description)
        user_choice = input("Which direction? ")

        if user_choice.lower() == "n" or user_choice.lower()== "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "e" or user_choice.lower() == "east":
            next_room = room_list[current_room].east
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "s" or user_choice.lower() == "South":
            next_room = room_list[current_room].south
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "w" or user_choice.lower() == "West":
            next_room = room_list[current_room].west
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room
        else:
            print("I don't understand that command.")

main()