import random


def selection_sort(my_list):
    """ Sort a list using the selection sort """
    outside_count = 0
    inside_count = 0
    # Loop through the entire array
    for cur_pos in range(len(my_list)):
        outside_count += 1
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos


        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(my_list)):
            inside_count += 1
            # Is this position smallest?
            if my_list[scan_pos] < my_list[min_pos]:
                # It is, mark this position as the smallest
                min_pos = scan_pos


        # Swap the two values
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp

    print(outside_count)
    print(inside_count)


def insertion_sort(my_list):
    """ Sort a list using the insertion sort """
    outside_count = 0
    inside_count = 0
    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_pos in range(1, len(my_list)):
        outside_count += 1
        # Get the value of the element to insert
        key_value = my_list[key_pos]

        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1

        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            inside_count += 1
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1


        # Everything's been moved out of the way, insert
        # the key into the correct location
        my_list[scan_pos + 1] = key_value
    print(outside_count)
    print(inside_count)


# This will point out a list
# For more information on the print formatting {:3}
# see the chapter on print formatting.
def print_list(my_list):
    for item in my_list:
        print(f"{item:3}", end="")
    print()


def main():
    # Create two lists of the same random numbers
    list_for_selection_sort = []
    list_for_insertion_sort = []
    list_size = 100
    for i in range(list_size):
        new_number = random.randrange(100)
        list_for_selection_sort.append(new_number)
        list_for_insertion_sort.append(new_number)

    # Print the original list
    print("Original List")
    print_list(list_for_selection_sort)

    # Use the selection sort and print the result
    print("Selection Sort")
    selection_sort(list_for_selection_sort)
    print_list(list_for_selection_sort)


    # Use the insertion sort and print the result
    print("Insertion Sort")
    insertion_sort(list_for_insertion_sort)
    print_list(list_for_insertion_sort)


main()
1. Write code to swap the values 25 and 40.

my_list = [55, 41, 52, 68, 45, 27, 40, 25, 37, 26]
temp = my_list[6]
my_list[6] = my_list[7]
my_list[7] = temp

2. Write code to swap the values 2 and 27.

my_list = [27, 32, 18,  2, 11, 57, 14, 38, 19, 91]
temp = my_list[0]
my_list[0] = my_list[3]
my_list[3] = temp

3. Why does the following code not work? Explain it, don't just list working code.

my_list = [70, 32, 98, 88, 92, 36, 81, 83, 87, 66]
temp = my_list[0]
my_list[1] = my_list[0]
my_list[0] = temp
my_list[1] = my_list[0] should be switched, because right now it is replacing [1] with [0], but [0] is already saved in the temp variable

4. Show how the following numbers can be sorted using the selection sort. Show the numbers after each iteration of the outer loop, similar to what is shown in the book. I am NOT looking for a copy of the code to do the sort. If you include any code for problems 4-7 you are doing it wrong.

97   74    8   98   47   62   12   11    0   60
 0   74    8   98   47   62   12   11   97   60
 0   8    74   98   47   62   12   11   97   60
 0   8    11   98   47   62   12   74   97   60
 0   8    11   12   47   62   98   74   97   60
 0   8    11   12   47   60   98   74   97   62
 0   8    11   12   47   60   62   74   97   98

5. Show how the following numbers can be sorted using the selection sort:

74   92   18   47   40   58    0   36   29   25
0   92   18   47   40   58    74   36   29   25
0   18   92   47   40   58    74   36   29   25
0   18   25   47   40   58    74   36   29   92
0   18   25   29   40   58    74   36   47   92
0   18   25   29   36   58    74   40   47   92
0   18   25   29   36   40    74   58   47   92
0   18   25   29   36   40    47   58   74   92

6. Show how the following numbers can be sorted using the INSERTION sort. (Note: If you think the 0 gets immediately sorted into position, you are doing it wrong. Go back and re-read how this sort works.)

74   92   18   47   40   58    0   36   29   25
18   74   92   47   40   58    0   36   29   25
18   47   74   92   40   58    0   36   29   25
0    18   47   74   92   40   58   36   29   25
0    18   40   47   74   92   58   36   29   25
0    18   40   47   58   74   92   36   29   25
0    18   36   40   47   58   74   92   29   25
0    18   29   36   40   47   58   74   92   25
0    18   25   29   36   40   47   58   74   92

7. Show how the following numbers can be sorted using the insertion sort:

37   11   14   50   24    7   17   88   99    9
11   37   14   50   24    7   17   88   99    9
11   14   37   50   24    7   17   88   99    9
11   14   24   37   50    7   17   88   99    9
 7   11   14   24   37   50   17   88   99    9
 7   11   14   17   24   37   50   88   99    9
 7    9   11   14   17   24   37   50   88   99

8. Explain what `min_pos` does in the selection sort.
min_pos is the smallest number
9. Explain what `cur_pos` does in the selection sort.
cur_pos is the number it is currently at
10. Explain what `scan_pos` does in the selection sort.
scan_pos is scanning the list from left to right
11. Explain what `key_pos` and `key_value` are in the insertion sort.
key_pos is the position, while the value is the number
12. Explain `scan_pos` in the insertion sort.
scanning from right to left
13.
import random


def selection_sort(my_list):
    """ Sort a list using the selection sort """
    outside_count = 0
    inside_count = 0
    # Loop through the entire array
    for cur_pos in range(len(my_list)):
        outside_count += 1
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos


        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(my_list)):
            inside_count += 1
            # Is this position smallest?
            if my_list[scan_pos] < my_list[min_pos]:
                # It is, mark this position as the smallest
                min_pos = scan_pos


        # Swap the two values
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp

    print(outside_count)
    print(inside_count)


def insertion_sort(my_list):
    """ Sort a list using the insertion sort """
    outside_count = 0
    inside_count = 0
    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_pos in range(1, len(my_list)):
        outside_count += 1
        # Get the value of the element to insert
        key_value = my_list[key_pos]

        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1

        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            inside_count += 1
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1


        # Everything's been moved out of the way, insert
        # the key into the correct location
        my_list[scan_pos + 1] = key_value
        print(outside_count)
        print(inside_count)


# This will point out a list
# For more information on the print formatting {:3}
# see the chapter on print formatting.
def print_list(my_list):
    for item in my_list:
        print(f"{item:3}", end="")
    print()


def main():
    # Create two lists of the same random numbers
    list_for_selection_sort = []
    list_for_insertion_sort = []
    list_size = 100
    for i in range(list_size):
        new_number = random.randrange(100)
        list_for_selection_sort.append(new_number)
        list_for_insertion_sort.append(new_number)

    # Print the original list
    print("Original List")
    print_list(list_for_selection_sort)

    # Use the selection sort and print the result
    print("Selection Sort")
    selection_sort(list_for_selection_sort)
    print_list(list_for_selection_sort)


    # Use the insertion sort and print the result
    print("Insertion Sort")
    insertion_sort(list_for_insertion_sort)
    print_list(list_for_insertion_sort)


main()
results:Original List
 79 71 84 56 84 81  8 57 25 10 13 37 99 89 33 72 60  2 75 56  1 28 12 47 67 74 70 67 88 24 72 91 21 94 40 87 62 46 53 72 40 19 79 17  1 18 16 25 64 26 10 67 31 74 55 70 66 74 95 22 85 91 13 17 11 21 52 38 96 26 36 94 45 90 83 84  4 14  4 94 66 71  0 61  2 38 52 65  5 57 34 54 94 48 62 25 41 77 30 93
Selection Sort
100
4950
  0  1  1  2  2  4  4  5  8 10 10 11 12 13 13 14 16 17 17 18 19 21 21 22 24 25 25 25 26 26 28 30 31 33 34 36 37 38 38 40 40 41 45 46 47 48 52 52 53 54 55 56 56 57 57 60 61 62 62 64 65 66 66 67 67 67 70 70 71 71 72 72 72 74 74 74 75 77 79 79 81 83 84 84 84 85 87 88 89 90 91 91 93 94 94 94 94 95 96 99
Insertion Sort
99
2541
  0  1  1  2  2  4  4  5  8 10 10 11 12 13 13 14 16 17 17 18 19 21 21 22 24 25 25 25 26 26 28 30 31 33 34 36 37 38 38 40 40 41 45 46 47 48 52 52 53 54 55 56 56 57 57 60 61 62 62 64 65 66 66 67 67 67 70 70 71 71 72 72 72 74 74 74 75 77 79 79 81 83 84 84 84 85 87 88 89 90 91 91 93 94 94 94 94 95 96 99
