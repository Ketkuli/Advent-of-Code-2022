# coding utf-8

# Advent of Code 5.12.2022

# Create new dictionary to storage data from file
containers = {}
data = "AoC2022_0512.txt"
test = "test.txt"


# This creates keys for dictionary
for i in range(1,10):
    containers[i] = []

# This piece reads containers from file and adds those to relevant stack in reverse order 
with open(data) as file:
    rows = file.readlines()[:8]
    for row in rows:
        row = row.replace("\n", "")
        counter = 1
        for i in range(1,35,4):
            if row[i] != " ":
                containers[counter].append(row[i])
            counter += 1

# Reversing the list order
for key in containers:
    containers[key].reverse()

def first():
    # Jumping over the first 10 lines
    with open(data) as file:
        for _ in range(10):
            next(file)
        # Iterate each row to move containers
        for row in file:
            row = row.replace("\n", "").split(" ")
            amount = int(row[1])
            origin = int(row[3])
            endpoint = int(row[5])
            loop_number = 1
            # If amount of containers moved is more than one this moves containers as much needed
            while loop_number <= amount:
                containers[endpoint].append(containers[origin][-1])
                containers[origin].pop(-1)
                loop_number += 1

    # Creating string to include top container from each stack
    top_containers = ""

    for key in containers:
        top_containers += containers[key][-1]

    print(f"These are the containers at the top of the stacks with CrateMover 9000: {top_containers}")

def second():
    # Jumping over the first 10 lines
    with open(data) as file:
        for _ in range(10):
            next(file)
        # Iterate each row to move containers
        for row in file:
            row = row.replace("\n", "").split(" ")
            amount = int(row[1])
            origin = int(row[3])
            endpoint = int(row[5])
            while amount >= 1:
                containers[endpoint].append(containers[origin][(-1*amount)])
                containers[origin].pop((-1*amount))
                amount -= 1



    # Creating string to include top container from each stack
    top_containers = ""

    for key in containers:
        top_containers += containers[key][-1]
    
    print(f"These are the containers at the top of the stacks with CrateMover 9001: {top_containers}")  

# You can only run one of these, not both
first()
#second()  