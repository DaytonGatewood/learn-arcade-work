class Room:
    """
    This is a class to describe a room.
    """
    def __init__(self, description, north, east, south, west, up, down, northeast, northwest, southeast, southwest):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.northeast = northeast
        self.northwest = northwest
        self.southeast = southeast
        self.southwest = southwest


class Item:
    # This is a class to describe an item.
    def __init__(self, room_number, long_description, short_name):
        self.room_number = room_number
        self.long_description = long_description
        self.short_name = short_name


def my_functions():
    room_list = []


    room = Room("You are in the living room.\nThere are doors to the east and northwest.", None, 1, None, None, None,
                None, None, 9, None, None)
    room_list.append(room)

    room = Room("You are in the hallway.\nThere are doors to the north, east, south, and west.", 2, 4, 3, 0, None, None,
                None, None, None, None)
    room_list.append(room)

    room = Room("You are in the library.\nThere are doors to the east and south. There is a staircase to go to the "
                "basement.", None, 5, 1, None, None, 6, None, None, None, None)
    room_list.append(room)

    room = Room("You are in the bedroom.\nThere is a door to the north.\nThere's a ladder to go up.", 1, None, None,
                None, 7, None, None, None, None, None)
    room_list.append(room)

    room = Room("You are in the kitchen.\nThere are doors to the north and west.", 5, None, None, 1, None, None, None,
                None, None, None)
    room_list.append(room)

    room = Room("You are in the dining room.\nThere are doors to the west, south, and northeast.",
                None, None, 4, 2, None, None, 8, None, None, None)
    room_list.append(room)

    room = Room("You are in the basement.\nThere is a scary beast in here.\nThere is a staircase to go up.", None, None,
                None, None, 2, None, None, None, None, None)
    room_list.append(room)

    room = Room("You are in the attic.\nThere is a ladder under you.", None, None, None, None, None, 3, None, None,
                None, None)
    room_list.append(room)

    room = Room("You are in the party room.\nThere is a door southwest.", None, None, None, None, None, None, None,
                None, None, 5)
    room_list.append(room)

    room = Room("You are in the exit room.\nThere is a door to the southeast.", None, None, None, None, None, None,
                None, None, 0, None)
    room_list.append(room)

    item_list = []

    button = Item(0, "The tv is off but you can click the button to turn it on.", "button")
    item_list.append(button)

    lamp = Item(1, "There is a lamp with a chain to turn it on.", "chain")
    item_list.append(lamp)

    lever = Item(2, "There is a secret lever on the wall.", "lever")
    item_list.append(lever)

    cheese = Item(4, "There is a fridge.", "fridge")
    item_list.append(cheese)

    switch = Item(3, "There is a switch on the floor.", "switch")
    item_list.append(switch)

    sword = Item(5, "There is a sword laying on the ground.", "sword")
    item_list.append(sword)

    bone = Item(7, "There is a bone on the ground.", "bone")
    item_list.append(bone)

    code = Item(6, "There is a key pad on the wall behind the beast.\nEnter the code to unlock a door.", "3675")
    item_list.append(code)

    cake = Item(8, "There is a cake on the table.", "cake")
    item_list.append(cake)

    door = Item(9, "The exit door is in here.\nYou'll have to unlock it to leave.", "door")
    item_list.append(door)
