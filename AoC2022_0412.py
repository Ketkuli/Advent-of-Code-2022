# coding utf-8

# Advent of code 5.12.2022

# First puzzle

range_fully_contains = 0
range_overlaps = 0
with open("AoC2022_0412.txt") as file:
    for row in file:
        row = row.replace("\n", "").split(",")
        # Finding the assignment places for each elf in pair by making list for sectors 
        # they work on
        first_elf = row[0].split("-")
        second_elf = row[1].split("-")

        # Creating lists for each elf designated sectors:
        first_elf_sectors = list(range(int(first_elf[0]),int(first_elf[1])+1))
        second_elf_sectors = list(range(int(second_elf[0]),int(second_elf[1])+1))

        # Finding which list is longer and then checking if shorter list is subset of longer list. 
        # If list lengths are same then checking if the lists are same.
        if len(first_elf_sectors) == len(second_elf_sectors):
            if first_elf_sectors == second_elf_sectors:
                range_fully_contains += 1
        elif len(first_elf_sectors) < len(second_elf_sectors):
            if set(first_elf_sectors).issubset(set(second_elf_sectors)) == True:
                range_fully_contains += 1
        else:
            if set(second_elf_sectors).issubset(set(first_elf_sectors)) == True:
                range_fully_contains += 1

        for number in first_elf_sectors:
            if number in second_elf_sectors:
                range_overlaps += 1
                break

print(f"There are {range_fully_contains} pairs that fully contains the other ones sectors")
print(f"There are {range_overlaps} pairs that overlap the other ones sectors")    





