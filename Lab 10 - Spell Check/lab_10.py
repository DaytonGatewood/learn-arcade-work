import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

def main():
    """ Read in lines from a file """
    dictionary_file = open("dictionary.txt")


    dictionary_list = []


    for line in dictionary_file:

        line = line.strip()

        dictionary_list.append(line)


    dictionary_file.close()
    
    print("--- Linear Search ---")

    alice_in_wonderland_file = open("AliceInWonderLand200.txt")
    line_number = 0
    for line in alice_in_wonderland_file:
        word_list = split_line(line)
        line_number += 1
        for word in word_list:
            key = word.upper()
            current_list_position = 0
            while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != key:
                current_list_position += 1
                if current_list_position == len(dictionary_list):
                    print("Possible misspelling on line", line_number, ":", word)

    print("--- Binary Search ---")
    dictionary_file = open("dictionary.txt")

    dictionary_list = []

    for line in dictionary_file:
        line = line.strip()

        dictionary_list.append(line)

    dictionary_file.close()

    alice_in_wonderland_file = open("AliceInWonderLand200.txt")

    line_number = 0
    for line in alice_in_wonderland_file:
        word_list = split_line(line)
        line_number += 1
        for word in word_list:
            key = word.upper()
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False

            while lower_bound <= upper_bound and not found:

                middle_pos = (lower_bound + upper_bound) // 2

                if dictionary_list[middle_pos] < key:
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > key:
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print("Possible misspelling on line", line_number, ":", word)

main()