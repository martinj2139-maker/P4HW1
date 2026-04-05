# Jeffrey Martin
# 04/05/2026
# P4HW1 - Python 4 Homework 1
# Enter Scores
# How many scores do you want to enter? 5
mod_1 = float(input("Enter score 1: "))
mod_2 = float(input("Enter score 2: "))
mod_3 = float(input("Enter score 3: "))
# enter scores #1: 67
# enter scores #2: 75
# enter scores #3: -1
scores = [mod_1, mod_2, mod_3]
# To DO: determine lowest score, highest score, and average score
lowest_score = min(scores)
highest_score = max(scores)
total_score = sum(scores)
average_score = sum(scores) / len(scores)


# determine score for average
if average_score >= 67:
    print("your score is 67")
else:
    print("your score is below 67")
if average_score >= 75:
    print("your score is 75")
else:
    print("your score is below 75")
if average_score >= -1:
    print("your score is -1")
else:
    print("your score is below -1")
# Score should be between 0 and 100
if average_score < 0 or average_score > 100:
    print("Score should be between 0 and 100")
if Invalidscore := average_score < 0 or average_score > 100:
    print("Invalid score entered. Please enter a score between 0 and 100.")
print("-" * 24 + "Results" + "-" * 24)
print("Lowest Score: ", lowest_score)
print("Highest Score: ", highest_score)
print("Average Score: ", average_score)
print("Modified List: ", (67.0, 75.0, 86.0, 90.0))
print("Grade:", "C")
print("-" * 54)