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


def main():
    # This creates the rooms
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

    room = Room("You are in the attic.\nThere is a ladder under you.", None, None, None, None, None, 3, None, None, None,
                None)
    room_list.append(room)

    room = Room("You are in the party room.\nThere is a door southwest.", None, None, None, None, None, None, None,
                None, None, 5)
    room_list.append(room)

    room = Room("You are in the exit room.\nThere is a door to the southeast.", None, None, None, None, None, None,
                None, None, 0, None)
    room_list.append(room)

    # This creates the items
    item_list = []

    button = Item(0, "The tv is off but you can click the button to turn it on.", "button")
    item_list.append(button)

    lamp = Item(1, "There is a lamp with a chain to turn it on.", "chain")
    item_list.append(lamp)

    cheese = Item(4, "There is a fridge.", "fridge")
    item_list.append(cheese)

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

    beast_lives = 3
    dead = False
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
        user_choice = input("What is your command? ")
        command_words = user_choice.split(" ")

        if command_words[0].lower() == "n" or command_words[0].lower() == "north":
            next_room = room_list[current_room].north
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif command_words[0].lower() == "e" or command_words[0].lower() == "east":
            next_room = room_list[current_room].east
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif command_words[0].lower() == "s" or command_words[0].lower() == "south":
            next_room = room_list[current_room].south
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif command_words[0].lower() == "w" or command_words[0].lower() == "west":
            next_room = room_list[current_room].west
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif command_words[0].lower() == "u" or command_words[0].lower() == "up":
            next_room = room_list[current_room].up
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif command_words[0].lower() == "d" or command_words[0].lower() == "down":
            next_room = room_list[current_room].down
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif command_words[0].lower() == "ne" or command_words[0].lower() == "northeast":
            next_room = room_list[current_room].northeast
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif command_words[0].lower() == "nw" or command_words[0].lower() == "northwest":
            next_room = room_list[current_room].northwest
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif command_words[0].lower() == "se" or command_words[0].lower() == "southeast":
            next_room = room_list[current_room].southeast
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif command_words[0].lower() == "sw" or command_words[0].lower() == "southwest":
            next_room = room_list[current_room].southwest
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif command_words[0].lower() == "grab":
            grabbed = False
            if len(command_words) < 2:
                print("What do you want to grab?")
            else:
                target_item = command_words[1].lower()
                for item in item_list:
                    if target_item == item.short_name and item.room_number == current_room:
                        if item.short_name == "bone" or item.short_name == "cheese" or item.short_name == "sword" or \
                                item.short_name == "cake":
                            item.room_number = -1
                            print(f"You picked up the {target_item}.")
                            grabbed = True
                if not grabbed:
                    print(f"The {target_item} was not found.")

        elif command_words[0].lower() == "inventory" or command_words[0].lower() == "i":
            empty = True
            for item in item_list:
                if item.room_number == -1:
                    empty = False
                    print(f"You have picked up {item.short_name}.")
            if empty:
                print("There is nothing in your inventory.")

        elif command_words[0].lower() == "drop":
            dropped = False
            if len(command_words) < 2:
                print("What do you want to drop?")
            else:
                target_item = command_words[1].lower()
                for item in item_list:
                    if target_item == item.short_name and item.room_number == -1:
                        item.room_number = current_room
                        print(f"You dropped the {target_item}.")
                        dropped = True
                if not dropped:
                    print("You didn't drop it.")

        elif command_words[0].lower() == "push":
            pushed = False
            if len(command_words) < 2:
                print("What do you want to push?")
            else:
                target_item = command_words[1].lower()
                if target_item == "button" and current_room == 0:
                    pushed = True
                    print(f"You pushed the button.\nThe tv turned on and the numbers 3675 are on the screen.")
                if not pushed:
                    print("You can't push that.")

        elif command_words[0].lower() == "pull":
            pulled = False
            if len(command_words) < 2:
                print("What do you want to pull?")
            else:
                target_item = command_words[1].lower()
                if target_item == "Chain" and current_room == 2:
                    pulled = True
                    print(f"You pulled the Chain.")
                if not pulled:
                    print("You can't pull that.")

        elif command_words[0].lower() == "feed":
            fed = False
            if len(command_words) < 2:
                print("What do you want to feed?")
            else:
                target_item = command_words[1].lower()
                if current_room == 6:
                    if target_item == "cheese" or target_item == "cake" or target_item == "bone":
                        print(f"You fed the beast.\nHe will not bother you anymore.\nThe code can now be entered.")
                        fed = True
                if not fed:
                    print("You can't feed that to the beast.\nThe beast is still in your way.")

        elif command_words[0].lower() == "swing":
            swung = False
            if len(command_words) < 2:
                print("What do you want to swing?")
            else:
                target_item = command_words[1].lower()
                if target_item == "sword" and current_room == 6:
                    beast_lives = beast_lives - 1
                    print(f"You have swung at the beast.\nThe beast has", beast_lives, " lives left.")
                    swung = True
                elif beast_lives == 0:
                    dead = True
                    print("You have slayed killed the beast. You can enter the code now.")
                if not swung:
                    print("You cannot swing that.")

        elif command_words[0].lower() == "enter":
            entered = False
            if len(command_words) < 2:
                print("What do you want to enter?")
            else:
                target_item = command_words[1].lower()
                if target_item == "3675" and current_room == 6:
                    if dead == True or fed == True:
                        entered = True
                        print(f"You have entered the correct code.")
                if not entered:
                    print("Wrong code or the beast is still alive. Try again.")

        elif command_words[0].lower() == "open":
            opened = False
            if len(command_words) < 2:
                print("What do you want to open?")
            else:
                target_item = command_words[1].lower()
                if target_item == "door" and current_room == 9:
                    if entered == True:
                        print(f"You have successfully left the mansion.\nYou win!")
                        opened = True
                        done = True
                if not opened:
                    print("You cannot leave yet.")

        elif command_words[0].lower() == "quit":
            done = True
        else:
            print("I don't understand that command. Try something else.")

main()
