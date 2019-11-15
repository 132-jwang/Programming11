

grade_list = []
max_grade = 100
grade_counter = 0
grade_sum = 0
number= True
 

while number is True:
    grade = float(input("Enter a grade, type -2 to quit, -1 to calculate average: "))
    if grade == -1:
        average = grade_sum / grade_counter
        print(average)
    else:
        if grade <= max_grade:
            grade_sum += grade
            grade_list.append(grade)
            grade_counter += 1
        else:
            print("Invalid grade, please try again")

if grade==-2:
    number is False


