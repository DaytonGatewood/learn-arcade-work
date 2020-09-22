import random


def main():
    # Variables
    miles_traveled = 0
    thirst = 0
    dog_tiredness = 0
    distance_wolves_travelled = -20
    initial_drinks = 3
    igloo = 0

    print("Welcome to The Iditarod Game!")
    print("You have decided to compete in the Alaska Iditarod race.")
    print("A pack of wolves is chasing you and your dog sled team.")
    print("Escape to the finish line to win!")
    print()

    done = False
    while not done:
        distance_between = miles_traveled - distance_wolves_travelled
        full_speed_ahead = random.randrange(10, 21)
        ahead_moderate_speed = random.randrange(5, 13)

        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("F. Quit.")
        print()
        user_choice = input("What is your choice? ")
        print()

    # Quit
        if user_choice.upper() == "F":
            print("Goodbye.")
            done = True
    # Check Status
        elif user_choice.upper() == "E":
            print("You have traveled", miles_traveled, "miles.")
            print("The wolves are", distance_between, "miles behind you.")
            print("You have", initial_drinks, "drinks left.")
            print()

    # Stop for the night
        elif user_choice.upper() == "D":
            dog_tiredness = 0
            print("Your dogs are happy now.")
            distance_wolves_travelled += random.randrange(7, 15)
            print("The wolves are", distance_between, "miles behind you.")
            print()

    # Ahead full speed!
        elif user_choice.upper() == "C":
            print("You have traveled ", full_speed_ahead, "miles!")
            miles_traveled += full_speed_ahead
            thirst += 1
            dog_tiredness += random.randrange(1, 4)
            distance_wolves_travelled += random.randrange(7, 15)
            igloo = random.randrange(1, 21)
            print()

    # Ahead moderate speed!
        elif user_choice.upper() == "B":
            print("You have traveled", ahead_moderate_speed, "Miles!")
            miles_traveled += ahead_moderate_speed
            thirst += 1
            dog_tiredness += 1
            distance_wolves_travelled += random.randrange(7, 15)
            igloo = random.randrange(1, 21)
            print()

    # Drink canteen
        elif user_choice.upper() == "A":
            if initial_drinks == 0:
                print("Oh no! You're out of water!")
                print()
            else:
                initial_drinks -= 1
                thirst = 0
                print("You have", initial_drinks, "drinks left. You are no longer thirsty.")
                print()

    # Other important codes
        if distance_between <= 15:
            print("The wolves are near!")
            print()

        if miles_traveled >= 200 and not done:
            print("You made it to the finish line! You Win!")
            done = True

        if distance_wolves_travelled >= miles_traveled:
            print("The wolves caught and ate you!")
            print("You're dead!")
            break

        if thirst > 4 and thirst <= 6:
            print("You are thirsty!")
            print()

        if thirst > 6:
            print("You died of dehydration!")
            done = True

        if dog_tiredness > 5 and dog_tiredness <= 8:
            print("Your dogs are tired!")
            print()

        if dog_tiredness > 8:
            print("Your dogs died!")
            break
        if igloo == 20:
            print("You found an igloo!")
            dog_tiredness = 0
            thirst = 0
            initial_drinks = 3
            print()


main()