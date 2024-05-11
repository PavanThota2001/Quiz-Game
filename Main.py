from question_model import Question
from data import question_data
from quiz_brain import QuizBrain



question_bank = []

for question in question_data:
    Q = question["question"]
    A = question["correct_answer"]
    question_bank_questions = Question(Q, A)
    question_bank.append(question_bank_questions)

quiz = QuizBrain(question_bank)
while quiz.has_any_questions():
    quiz.next_question()






# for question in Data:
#     question_bank = Question(Data[question], Data[answer])




