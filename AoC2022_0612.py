# coding utf-8

# Advent of Code 6.12.2022 First Puzzle:

def first(data: str):
    character_number = 4 # First marker can only be after fourth character
    for i in range(len(data)):
        subset = data[i:i+4]
        unique_markers = 0
        for char in subset:
            count = subset.count(char)
            if count != 1:
                character_number += 1
                break
            else:
                unique_markers += 1
        if unique_markers == 4:
            return character_number

# Advent of Code 6.12.2022 Second Puzzle:

def second(data: str):
    character_number = 14 # Start of message marker appers after 14 unique character
    for i in range(len(data)):
        subset = data[i:i+14]
        unique_markers = 0
        for char in subset:
            count = subset.count(char)
            if count != 1:
                character_number += 1
                break
            else:
                unique_markers += 1
        if unique_markers == 14:
            return character_number








# ------------------------------------------------------------
# Opening input data and storing it to a variable:
with open("AoC2022_0612.txt") as file:
    datastream = file.readline()


# For testing first function:
test_data1 = "bvwbjplbgvbhsrlpgdmjqwftvncz" # 5
test_data2 = "nppdvjthqldpwncqszvftbrmjlhg" # 6
test_data3 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" # 11
# For testing second function:
test_data4 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" # 19
test_data5 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" # 29

first_marker = first(datastream)
print(f"The first marker appears after: {first_marker}")

message_marker = second(datastream)
print(f"Message appears after character: {message_marker}")
