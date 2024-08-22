student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# if marks between 91-100 then grade:"Outstanding"
# if marks between 81-90 then grade:"Exceeds Expectations"
# if marks between 71-80 then grade:"Acceptable"
# if marks are 70 or lower then grade:"Fail"



#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
for i in student_scores:
    if student_scores[i] in range(91,101):
        student_grades[i] = "Outstanding"
    elif student_scores[i] in range(81,91):
        student_grades[i] = "Exceeds Expectations"
    elif student_scores[i] in range(71,81):
        student_grades[i] = "Acceptable"
    elif student_scores[i] in range(0,71):
        student_grades[i] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)
# {'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}