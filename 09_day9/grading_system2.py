student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60,
    'goku': 20
}

grade_end=False
while not grade_end==True:
    student_grades={}
    user_input1=input("enter yes if you want to continue and enter no if you want to start again:\n").lower()
    if user_input1=="yes":
        user_input=input("enter the key value.\n")


        
        score=student_scores[user_input]

        if score>90:
            student_grades[user_input]="the student has outstanding performance."
        
        elif score>80:
            student_grades[user_input]="the student exceeds expectations."

        elif score > 70:
            student_grades[user_input]="the student has acceptable performance."

        else:
            student_grades[user_input]="the student has failed." 

        print(student_grades)
    elif user_input1=="no":
        print("thanks for using our program.")
        break
    else:
        ("you have entered the wrong input.")
        
