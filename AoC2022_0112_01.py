# Coding utf-8
# Advent of Code 1.12.2022 first puzzle

elfs = []
sum_calories = 0

with open("AoC2022_0112_01.txt") as file:
    for row in file:
        row = row.replace("\n", "")
        if row == "":
            elfs.append(sum_calories)
            sum_calories = 0
        else:
            row = int(row)
            sum_calories += row

largest_amount = max(elfs)
print(f"Largest amount of calories carried: {largest_amount}")

# Advent of Code 1.12.2022 second puzzle 
 
sorted_elfs = sorted(elfs)
print(sorted_elfs)

top3 = sorted_elfs[-1] + sorted_elfs[-2] + sorted_elfs[-3]

print(f"Calories carried by top 3 of elves: {top3}")