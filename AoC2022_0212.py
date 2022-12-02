# Coding utf-8

# Advent of Code 2.12.2022 first puzzle

#A = Rock
#B = Paper
#C = Scissors

#X = Rock = 1 point
#Y = Paper = 2 points
#Z = Scissors = 3 points

# Double dictionary for my choice and opponent choice with returned points depending on the outcome of game
def first(): 
    choices = {
    "X": {"A": 3, "B": 0, "C": 6}, 
    "Y": {"A": 6, "B": 3, "C": 0}, 
    "Z": {"A": 0, "B": 6, "C": 3}
    } 

    sum_of_points = 0

    with open("AoC2022_0212.txt") as file:
        for row in file:
            row = row.replace("\n", "").split(" ")
            choice1 = row[0]
            choice2 = row[1]
            if choice2 == "X":
                sum_of_points += 1
            elif choice2 == "Y":
                sum_of_points += 2
            else:
                sum_of_points += 3
        
            outcome_points = (choices[choice2][choice1])
            sum_of_points += outcome_points 

    print(f"This is the sum of points for first puzzle: {sum_of_points}")

# Advent of code 2.12.2022 second puzzle

#A = Rock = 1 point
#B = Paper = 2 points
#C = Scissors = 3 points

#X = Lose
#Y = Draw
#Z = Win

def second():
    sum_of_points = 0

    outcome_points = {"X":0, "Y":3, "Z":6} # These are the points for victory, draw or win

    shape_points = {"A":1, "B":2, "C":3}

    choices = {
    "X": {"A": "C", "B": "A", "C": "B"}, #Lose
    "Y": {"A": "A", "B": "B", "C": "C"}, #Draw
    "Z": {"A": "B", "B": "C", "C": "A"}  #Victory
    }

    with open("AoC2022_0212.txt") as file:
        for row in file:
            row = row.replace("\n", "").split(" ")
            choice1 = row[0]
            outcome = row[1]
            own_choice = choices[outcome][choice1]

            outcome_point = outcome_points[outcome]
            shape_point = shape_points[own_choice]
            sum_of_points += shape_point + outcome_point
    
    print(f"This is the sum of points for second puzzle: {sum_of_points}")

first()
second()