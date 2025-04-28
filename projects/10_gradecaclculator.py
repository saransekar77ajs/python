print("📊 STUDENT GRADE CALCULATOR 📊")

student_name = input("Enter the student name: ")
student_id = input("Enter the student id: ")

count = 0
score = 0

while True:
    check = input("Do you want to enter your score? (yes or no) ").lower()
    if check != "yes":
        print("Thank you for visiting student grading site.")
        break
    else:
        try:
            score1 = int(input("Enter your score: "))
            if score1 < 1 or score1 > 100:
                print(" ⚠️ Please enter your score between 1 and 100.")
            else:
                count += 1
                score += score1
        except ValueError:
            print(" ⚠️ Enter valid score")
if count > 0:
    print("Student Grade: ")
    print(f"Student Name: {student_name} and Student ID: {student_id} ")
    print(f"Your total score is {score}")

    average_score = round(score / count, 2)
    print(f"Your average score is {average_score}")
    if average_score > 90:
        print("Grade: A")
    elif average_score > 80:
        print("Grade: B")
    elif average_score > 70:
        print("Grade: C")
    elif average_score > 60:
        print("Grade: D")
    else:
        print("Failed")
else:
    print(" ⚠️ No scores were entered.")
