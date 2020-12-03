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


def my_rooms():
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
