# codint utf-8

# Advent of Code 3.12.2022 

# Building a dictionary for item type and corresponding value
lower_case = "abcdefghijklmnopqrstuvwxyz" 
upper_case = lower_case.upper()

priority_numbers_lower = list(range(1,27))
priority_numbers_upper = list(range(27,53))

priority = {}

for i in range(len(lower_case)):
    priority[lower_case[i]] = priority_numbers_lower[i]

for i in range(len(upper_case)):
    priority[upper_case[i]] = priority_numbers_upper[i]

# First puzzle in its' own function. Using the priority dict as baseline.
def first():
    # Opening the input file for solving the puzzle:
    priority_letters = []
    with open("AoC2022_0312.txt") as file:
        for row in file:
            row = row.replace("\n", "")

            # Splitting the string in half
            half = int(len(row)/2)
            first_compartment = row[:half]
            second_compartment = row[half:]

            # Finding same item type in both compartments and adding only first occurence 
            # to priority_letters-list
            for item in first_compartment:
                if second_compartment.find(item) != -1:
                    priority_letters.append(item)
                    break

    # Calculating the sum for priority_letters
    priority_sum = 0
    for letter in priority_letters:
        priority_sum += priority[letter]

    print(f"Sum of priorities is: {priority_sum}")

# Second puzzle in its' own function. Using the priority dict as baseline.
def second():
    groups = [] 
    # Opening input file and creating groups including three elfs per group
    with open("AoC2022_0312.txt") as file:
        group = []
        for row in file:
            row = row.replace("\n", "")
            group.append(row)
            if len(group) >= 3:
                groups.append(group)
                group = []  

    # Finding which item is carried by all elfs in the group   
    group_priority_letter = []       
    for group in groups:
        for elf in group:
            for letter in elf:
                if group[1].find(letter) != -1 and group[2].find(letter) != -1:
                    group_priority_letter.append(letter)
                    break
            break

    # Calculating sum for group priority letters
    group_sum = 0
    for letter in group_priority_letter:
        group_sum += priority[letter]

    print(f"This is the sum of group priority items: {group_sum}")

first()
second()