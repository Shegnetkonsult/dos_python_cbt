import random
import pandas
print("|---------------------------------------------------|")
response: str = input("|   Do you want to take CBT? Y[es] or N[o]: ")
print("|---------------------------------------------------|")

if response[0].upper() != 'Y':
    print("|---------------------------------------------------|")
    print("|             Byebye, do have a nice day            |")
    print("|---------------------------------------------------|")
    input()
    input()

while response[0].upper() == 'Y':
    # Open the exam info file
    with open("exam_info.txt", "r") as file:
        lines = file.readlines()
    file.close()

    # INSTRUCTIONS FOR WRITING TESTS
    print("|---------------------------------------------------|")
    print("|      ", lines[0].strip(), "     |")
    print("|          ", lines[1].strip(), "         |")
    print("|     ", lines[2].strip(), "      |")
    print("|---------------------------------------------------|")
    print("|                   INSTRUCTIONS                    |")
    print("|---------------------------------------------------|")
    print("|       Pick from the options A - D option          |")
    print("|      that best suite the current question         |")
    print("|     NOTE: FILL IN YOUR MATRICULATION NUMBER,      |")
    print("|     SEAT NUMBER(IF YOU HAVE, IF NOT PUT NIL)      |")
    print("|   AND ENTER YOUR FULL NAME AS YOU OFTEN USE IT    |")
    print("|     YOUR TOTAL SCORE IS ORIGINALLY SET TO 0       |")
    print("|---------------------------------------------------|")

    stud_record = {'matric_no': input("Enter your Matriculation Number: "),
                   'seat_no': input("Enter your Seat Number: "),
                   'stud_name': input("Enter your full name: "),
                   'score': 0, 'total_score': 0
                   }

    print("|---------------------------------------------------| \n")
    print("|       YOU HAVE 30 QUESTIONS TO ANSWER             | \n")
    print("|  GOOD LUCK, Press RETURN KEY (ENTER) to continue  | \n")
    print("|---------------------------------------------------| \n\n")
    print(stud_record)
    input()

    # Open the questions file and read lines
    with open("test_question.txt", "r") as file:
        lines = file.readlines()
    file.close()

    # Create an empty list to store the tuples
    questions_and_answers = []

    # Iterate over the lines, creating tuples for each question and its options
    for i in range(0, len(lines), 6):
        question = lines[i].strip()
        options = [lines[j].strip() for j in range(i + 1, i + 5)]
        correct_answer = lines[i + 5].strip()
        questions_and_answers.append((question, options, correct_answer))

    # Shuffle the list of tuples
    random.shuffle(questions_and_answers)

    # Now, you can access shuffled questions, options, and correct answers together
    shuffled_questions, shuffled_options, shuffled_correct_answers = zip(*questions_and_answers)

    # Print shuffled questions and options
    # To set Questions for users
    print("-"*55)
    print("-"*55)
    print("You have 30 questions to answer")
    print("-"*55)
    print("-"*55)
    answer = []
    i = 0
    for question, options in zip(shuffled_questions, shuffled_options):
        i = i+1
        if i <= 30:
            print("Question ", i, ":", question)
            option_type = ["A", "B", "C", "D"]
            for j in range(0, 4):
                print("Option ", option_type[j], ":", options[j])
            answer.append(input("Pick your choice: "))
            answer[i - 1] = answer[i-1].upper()
            if answer[i-1] == 'A':
                answer[i-1] = options[0]
            if answer[i-1] == 'B':
                answer[i-1] = options[1]
            if answer[i-1] == 'C':
                answer[i-1] = options[2]
            if answer[i-1] == 'D':
                answer[i-1] = options[3]
            input()

    count = 0
    for i in range(30):
        if answer[i] == shuffled_correct_answers[i]:
            count = count+1
    stud_record['score'] = count
    stud_record['total_score'] = 30
    print("|---------------------------------------------------|")
    print("|                   TEST RESULT                     |")
    print("|---------------------------------------------------|")
    print("|      Thank you, you score", count, "out of 30     |")
    print("|  CONGRATS, Press RETURN KEY (ENTER) to continue   |")
    print("|---------------------------------------------------|")
    input()

    # Open the registered students file and rewrite lines
    f = open('students_result.txt', 'a')
    f.write(stud_record['seat_no']+"\n")
    f.write(stud_record['matric_no']+"\n")
    f.write(stud_record['stud_name']+"\n")
    f.write(str(stud_record['score'])+"\n")
    f.write(str(stud_record['total_score'])+"\n")
    f.close()


    print("|---------------------------------------------------|")
    print("|                   SAVE RESULT                     |")
    print("|---------------------------------------------------|")
    print("|       YOUR RESULT HAS BEEN SAVED TO DATABASE      |")
    print("|---------------------------------------------------|")
    input()
    input()

    response = input("Do you want to take CBT? Y[es] or N[o]: ")
    if response[0].upper() != 'Y':
        print("|---------------------------------------------------|")
        print("|             Byebye, do have a nice day            |")
        print("|---------------------------------------------------|")
        input()
