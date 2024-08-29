# Write a code to find the highest score from the marks of the students entered by user, separated by comma.

marks = input("Enter the marks of all the students, separated with comma. (Note: Use Integers ONLY.):").split(',')

for i in range(0,len(marks)):
    marks[i] = int(marks[i])

highest_score = 0

for i in marks:
    if i>highest_score:
        highest_score = i

print(f"The highest score among the scores of all the students is: {highest_score}")