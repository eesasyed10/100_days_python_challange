from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for question in question_data:
    q_text= question["text"]
    q_answer= question["answer"]
    new_question=Question(q_text,q_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
# is_on=True
while quiz.still_has_questions():
    quiz.next_question()
    
print("You have completed the quiz.")
print(f"your final score is {quiz.score}\{quiz.question_number}. ")
