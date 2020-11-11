class Room:
    """
    This is a class to describe a room.
    """
    def __init__(self, description, north, east, south, west, up, down):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.northeast = north_east
        self.northwest = north_west
        self.southwest = south_west
        self.southwest = south_west




class Item:
    "This is a class to describe an item"
    def __init__(self, room_number, long_description, short_name):
        self.room_number = room_number
        self.long_description = long_description
        self.short_name = short_name


def main():
    # This creates the rooms
    room_list = []
    room = Room("You are in the living room. \nThere is a door to the east.", None, 1, None, None, None, None, None, 9, None, None)
    room_list.append(room)
    room = Room("You are in the hallway.\nThere are doors to the north, east, and south.", 2, 4, 3, 0, None, None, None, None, None, None)
    room_list.append(room)
    room = Room("You are in the library.\nThere is a scary book and a chair.\nThere are doors to the east and south.", None, 5, 1, None, None, 6, None, None, None, None)
    room_list.append(room)
    room = Room("You are in the bedroom.\nThere is a closet full of skeletons and a coffin.\nThere is a door to the north.", 1, None, None, None, 7, None, None, None, None, None)
    room_list.append(room)
    room = Room("You are in the kitchen.\nThere is a fridge and butcher knives.\nThere are doors to the south and west.", None, None, 4, 2, None, None, None, None, None, None)
    room_list.append(room)
    room = Room("You are in the dining room.\nThere is a banana and spiderwebs.\nThere is a door to the west.", None, None, None, 1, None, 6, None, None, None, None)
    room_list.append(room)
    room_list = Room("You are in the basement.\nThere is a staircase to go up.", None, None, None, None, 5, None, None, None, None, None)
    room_list.append(room)
    room_list = Room("You are in the attic. There is a ladder under you.", None, None, None, None, None, 3, None, None, None, None)
    room_list.append(room)
    room = Room("You are in the 8th room\nThere is a door southwest of you.", None, None, None, None, None, None, None, None, None, 5)
    room_list.append(room)
    room = Room("You are in the 9th room.\nThere is a door to the southeast.", None, None, None, None, None, None, None, 0, None, None)
    room_list.append(room)

    # This creates the items
    item_list = []
    tv = Item(0, "The tv is off but you can click the button to turn it on", "button")
    item_list.append(tv)
    lamp = Item(1, "There is a lamp with a chain to turn it on.", "chain")
    item_list.append(lamp)
    key = Item(1, "There is also a key on the ground", "key")
    item_list.append(key)
    lever = Item(2, "There is a secret lever on the wall", "lever")
    item_list.append(lever)
    door = Item(3, "There is a closet with the door ajar.", "door")
    item_list.append(door)
    cheese = Item(4, "There is a fridge.", "fridge")
    item_list.append(cheese)
    switch = Item(5, "There is a switch on the floor", "switch")
    item_list.append(switch)
    sword = Item(6, "There is a sword laying on the ground.", "sword")
    item_list.append(sword)



    current_room = 0
    done = False
    print("You are in a haunted castle. Find your way out or be stuck forever!")

    while not done:
        print()
        print(room_list[current_room].description)
        for item in item_list:
            if item.room_number == current_room:
                print(item.long_description)
                print()
        user_choice = input("Which direction? ")

        if user_choice.lower() == "n" or user_choice.lower() == "north":
            next_room = room_list[current_room].north
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "e" or user_choice.lower() == "east":
            next_room = room_list[current_room].east
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "s" or user_choice.lower() == "south":
            next_room = room_list[current_room].south
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "w" or user_choice.lower() == "west":
            next_room = room_list[current_room].west
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "u" or user_choice.lower() == "up":
            next_room = room_list[current_room].up
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "d" or user_choice.lower() == "down":
            next_room = room_list[current_room].down
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "ne" or user_choice.lower() == "northeast":
            next_room = room_list[current_room].north_east
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "nw" or user_choice.lower() == "northwest":
            next_room = room_list[current_room].north_west
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "se" or user_choice.lower() == "southeast":
            next_room = room_list[current_room].south_east
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice.lower() == "quit":
            done = True
        else:
            print("I don't understand that command.")



main()
